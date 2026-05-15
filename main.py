@app.route('/index/cars')
def car_blog():
    title = "KashKash's Global Supercar Gallery"
    date = "May 14th, 2026"
    
    text = ("From the 795 HP supercharged heart of the Mustang Dark Horse SC to the refined 1,015 CV hybrid "
            "soul of the Lamborghini Revuelto, this gallery represents the absolute peak of 2026 performance. "
            "Whether it's the roar of the Ferrari V12 or the silent speed of the 1,025 HP Rivian R1S, "
            "every car here is a piece of engineering history.")

    with open("templates/index.html", "r") as f:
        page = f.read()

    page = page.replace("{title}", title).replace("{date}", date).replace("{text}", text)
    return page