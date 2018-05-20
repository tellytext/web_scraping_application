from flask import Flask, flash, render_template, request, url_for, redirect
import scraper

app = Flask(__name__)


@app.route('/homepage/')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/selfhosting/')
def selfhosting():
    return render_template("selfhosting.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/search/', methods=['GET', 'POST'])
def search():
    error = None
    try:
        if request.method == "POST":
            query = request.form['searchquery']
            if len(query) > 0:
                results = scraper.form_search_results.parse_desktop_search_results(query, scraper.form_search_results.get_search_results(query))
                print(results)
                if len(results) == 0:
                    results = "No paid search results found"
                    return render_template("results.html", results=results, query=query)
                else:
                    return render_template("results.html", results=results, query=query)
            else:
                error = "Please enter search criteria."

        return render_template("search.html", error=error)

    except Exception as e:
        return render_template("search.html", error=error)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/contact/')
def contact():
    try:
        return render_template("contact.html")
    except Exception as e:
        return (str(e))


if __name__ == "__main__":
    app.run()