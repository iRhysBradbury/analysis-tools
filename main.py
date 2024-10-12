import io

import matplotlib
from flask import Flask, request, Response, send_file
from matplotlib import pyplot as plt
from static import constant
from static.constant import labelsData
from std import std
from vwap import vwap
from integrations import yfinance_integration
import seaborn as sns


app = Flask(__name__)


@app.route("/vwap", methods=["GET"])
def vwap_route():
    try:
        ticker = str(request.args.get("ticker"))
        interval = int(request.args.get("interval"))
        start = str(request.args.get("start"))
        end = str(request.args.get("end"))

        data = yfinance_integration.data(
            tickers=[ticker],
            start=start,
            end=end
        )

        dataWVWAP = vwap.append_vwap(
            dataframe=data,
            window=interval,
            labels=constant.labelsData
        )

        dataMutated = std.append_standard_deviations(
            dataframe=dataWVWAP,
            window=interval,
            labels=constant.labelsData
        )

        dataNoNaN = dataMutated.dropna()
        jsonData = dataNoNaN.to_json(orient="records")

        return Response(jsonData, mimetype="application/json")

    except Exception as e:
        return str(e), 500


@app.route('/plot')
def plot():
    # Configure matplotlib for off-screen rendering
    matplotlib.use('Agg')

    # Generate your plot here
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 2, 3, 5]
    ax.plot(x, y)

    # Save the figure to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Close the figure to free up resources
    plt.close(fig)

    # Send the image as a response
    resp = send_file(
        img,
        mimetype='image/png',
        as_attachment=True,
        download_name='plot.png'
    )
    return resp


@app.route("/vwap/graph", methods=["GET"])
def vwap_route_graph():
    try:
        ticker = str(request.args.get("ticker"))
        interval = int(request.args.get("interval"))
        start = str(request.args.get("start"))
        end = str(request.args.get("end"))

        data = yfinance_integration.data(
            tickers=[ticker],
            start=start,
            end=end
        )

        dataWVWAP = vwap.append_vwap(
            dataframe=data,
            window=interval,
            labels=constant.labelsData
        )

        dataMutated = std.append_standard_deviations(
            dataframe=dataWVWAP,
            window=interval,
            labels=constant.labelsData
        )

        dataNoNaN = dataMutated.dropna()
        jsonData = dataNoNaN.to_json(orient="records")

        sns.set_theme()

        tips = sns.load_dataset("tips")

        # Create a visualization
        sns.relplot(
            data=tips,
            x="total_bill", y="tip", col="time",
            hue="smoker", style="smoker", size="size",
        )

        # ## plot and draw
        # dataNoNaN[labelsData.vwap].plot(color=labelsData.colors.light_grey)
        # dataNoNaN[labelsData.std_p1].plot(color=labelsData.colors.dark_grey)
        # dataNoNaN[labelsData.std_p2].plot(color=labelsData.colors.dark_grey)
        # dataNoNaN[labelsData.std_m1].plot(color=labelsData.colors.dark_grey)
        # dataNoNaN[labelsData.std_m2].plot(color=labelsData.colors.dark_grey)
        # dataNoNaN[labelsData.close].plot(color=labelsData.colors.blue)
        #
        # plt.legend()
        # plt.title("Close Prices VWAP")
        # plt.xlabel("Days")
        # plt.ylabel("VWAP ($)")
        # plt.show()
        #
        # img_buffer = io.BytesIO()
        # fig.savefig(img_buffer, format='png')
        # img_buffer.seek(0)
        #
        response = Response(jsonData, mimetype="application/json")
        # response.headers["Content-Disposition"] = "attachment; filename=vwap_plot.png"
        # response.headers["X-SendFile"] = "vwap_plot.png"

        return response
    except Exception as e:
        return str(e), 500



if __name__ == "__main__":
    app.run(debug=False)
