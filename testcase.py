try:
    import turtle
except ImportError:
    print("Turtle is not supported in this environment. Please run on a desktop Python interpreter.")
    exit(1)


class TestCase:
    def __init__(self):
        self.t = turtle.Turtle()
        screen = turtle.Screen()
        screen.setup(width=1.0, height=1.0)

        with open('prompt.txt') as f:
            self.prompt = f.read()

    def run(self):
        self.t.pencolor("bisque")

        self.t.fillcolor("bisque")
        self.t.begin_fill()
        self.t.circle(50)
        self.t.end_fill()

        self.t.penup()
        self.t.setpos(100, 0)
        self.t.pendown()

        self.t.fillcolor("bisque")
        self.t.begin_fill()
        self.t.circle(50)
        self.t.end_fill()

        self.t.left(90)
        self.t.forward(250)

        self.t.fillcolor("brown")
        self.t.begin_fill()
        self.t.circle(50)
        self.t.end_fill()

        self.t.fillcolor("bisque")
        self.t.begin_fill()
        self.t.left(90)
        self.t.forward(100)

        self.t.left(90)
        self.t.forward(200)

        self.t.left(90)
        self.t.forward(100)
        self.t.end_fill()

        self.t.backward(45)
        self.t.left(90)
        self.t.forward(250)

        self.t.color("green")
        self.t.write(self.prompt, font=("Arial", 16, "normal"))

        turtle.done()


if __name__ == '__main__':
    test_case = TestCase()
    test_case.run()
