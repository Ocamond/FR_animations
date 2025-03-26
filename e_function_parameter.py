from manim import *


class ExponentialFunctionWithParameterVariations(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        a = Variable(1, label="a").set_color(BLACK)
        b = Variable(1, label="b").set_color(BLACK)
        d = Variable(0, label="d").set_color(BLACK)
        y = Variable(0, label="y").set_color(BLACK)

        axes = (
            Axes(
                x_range=[-3, 3, 1],
                y_range=[0, 10, 1],
                axis_config={"include_numbers": True},
                x_length=10,
            )
            .set_color(BLACK)
            .scale(0.75)
            .to_corner(DL)
        )

        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)

        ValueTracker(1).get_value()

        # Funktion mit always_redraw
        e_func = always_redraw(
            lambda: axes.plot(
                lambda x: a.tracker.get_value()
                * np.exp(b.tracker.get_value() * x - d.tracker.get_value())
                + y.tracker.get_value(),
                x_range=[-3, 2],
                color=BLUE,
            )
        )

        e_func_label = (
            MathTex(
                r"f(x) = a \cdot e^{\left( b \cdot x - d \right)} + y",
                color=BLUE,
            )
            .scale(1.25)
            .to_corner(UL)
        )

        sliders = VGroup()

        line_a = NumberLine(x_range=[-5, 5, 1], length=4, color=BLACK)
        a.next_to(line_a, UP, buff=0.25)
        knob_a = Circle(radius=0.1, color=GREEN, fill_opacity=1)
        knob_a.move_to(line_a.get_start())
        knob_a.add_updater(lambda m: m.move_to(line_a.n2p(a.tracker.get_value())))
        a.add_updater(lambda m: m.set_value(a.tracker.get_value()))
        slider_group_a = VGroup(line_a, knob_a, a).shift(UP * 1.5)

        line_b = NumberLine(x_range=[-5, 5, 1], length=4, color=BLACK)
        b.next_to(line_b, UP, buff=0.25)
        knob_b = Circle(radius=0.1, color=GREEN, fill_opacity=1)
        knob_b.move_to(line_b.get_start())
        knob_b.add_updater(lambda m: m.move_to(line_b.n2p(b.tracker.get_value())))
        b.add_updater(lambda m: m.set_value(b.tracker.get_value()))
        slider_group_b = VGroup(line_b, knob_b, b)

        line_d = NumberLine(x_range=[-5, 5, 1], length=4, color=BLACK)
        d.next_to(line_d, UP, buff=0.25)
        knob_d = Circle(radius=0.1, color=GREEN, fill_opacity=1)
        knob_d.move_to(line_d.get_start())
        knob_d.add_updater(lambda m: m.move_to(line_d.n2p(d.tracker.get_value())))
        d.add_updater(lambda m: m.set_value(d.tracker.get_value()))
        slider_group_d = VGroup(line_d, knob_d, d).shift(DOWN * 1.5)

        line_y = NumberLine(x_range=[-5, 5, 1], length=4, color=BLACK)
        y.next_to(line_y, UP, buff=0.25)
        knob_y = Circle(radius=0.1, color=GREEN, fill_opacity=1)
        knob_y.move_to(line_y.get_start())
        knob_y.add_updater(lambda m: m.move_to(line_y.n2p(y.tracker.get_value())))
        y.add_updater(lambda m: m.set_value(y.tracker.get_value()))
        slider_group_y = VGroup(line_y, knob_y, y).shift(DOWN * 3)
        sliders.add(slider_group_a, slider_group_b, slider_group_d, slider_group_y)
        sliders.to_edge(RIGHT, buff=1)
        self.add(axes, axes_labels, e_func, e_func_label, sliders)
        self.play(
            a.tracker.animate.set_value(2),
            run_time=2,
        )

        self.wait()

        self.play(
            b.tracker.animate.set_value(2),
            run_time=2,
        )
        self.wait()

        self.play(
            d.tracker.animate.set_value(-1),
            run_time=2,
        )
        self.wait()

        self.play(
            y.tracker.animate.set_value(1),
            run_time=2,
        )

        self.wait(2)
