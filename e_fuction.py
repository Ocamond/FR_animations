from manim import *


class ExponentialFunction(Scene):
    CONFIG = {
        "camera_config": {"background_color": WHITE},
        "example_inputs": [1, 2],
    }

    def construct(self):
        self.camera.background_color = WHITE
        example_inputs = [1, 2]

        x = ValueTracker(1)
        dx = ValueTracker(0.5)

        # Koordinatensystem
        axes = Axes(
            x_range=[-3, 3, 1], y_range=[0, 10, 1], axis_config={"color": BLACK}
        )

        # Beschriftungen
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)

        # Funktionsgraph
        e_func = axes.plot(lambda x: np.exp(x), color=BLUE)
        e_func_label = axes.get_graph_label(
            e_func, label="f(x)=e^x", direction=LEFT, color=BLUE
        )

        tangent = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=e_func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="dx",
                dy_label="df",
                secant_line_color=GREEN,
                secant_line_length=8,
            )
        )

        v_lines = [
            axes.get_vertical_lines_to_graph(e_func, [x, x], num_lines=1, color=BLACK)
            for x in example_inputs
        ]

        height_labels = [
            MathTex("e^%d" % x)
            .next_to(v1, RIGHT * DOWN, 0.2)
            .shift(0.4 * RIGHT)
            .set_color(BLACK)
            for v1, x in zip(v_lines, example_inputs)
        ]

        slope_labels = [
            Tex("Steigung = $e^%d$" % x)
            .scale(0.9)
            .next_to(v1.get_top(), RIGHT)
            .set_color(BLACK)
            for v1, x in zip(v_lines, example_inputs)
        ]

        dot1 = always_redraw(
            lambda: Dot()
            .move_to(axes.c2p(x.get_value(), e_func.underlying_function(x.get_value())))
            .set_color(RED)
        )

        dot2 = always_redraw(
            lambda: Dot()
            .move_to(
                axes.c2p(
                    x.get_value() + dx.get_value(),
                    e_func.underlying_function(x.get_value() + dx.get_value()),
                )
            )
            .set_color(RED)
        )

        areas = [
            axes.get_area(
                e_func,
                x_range=(-3, x),
                color=(GREEN_B, GREEN_D),
                opacity=0.8,
            )
            for x in example_inputs
        ]

        area_labels = [
            MathTex("e^%d" % x)
            .move_to(area.get_corner(DR))
            .shift(UP * 0.5 + LEFT * 0.5)
            .set_color(GREEN)
            .scale(1.25)
            for x, area in zip(example_inputs, areas)
        ]

        self.add(axes, labels, e_func, e_func_label)

        self.play(Create(VGroup(dot1, dot2, tangent)), run_time=3)
        self.wait(1)
        self.play(dx.animate.set_value(0.0001), run_time=3)

        self.wait(1)

        self.play(Write(slope_labels[0]))
        self.play(Create(v_lines[0]))
        self.play(Write(height_labels[0]))
        slope_labels[0].save_state()
        height_labels[0].save_state()
        v_lines[0].save_state()

        self.wait(1)
        self.play(
            x.animate.set_value(2),
            Transform(
                slope_labels[0],
                slope_labels[1],
            ),
            Transform(v_lines[0], v_lines[1]),
            Transform(
                height_labels[0],
                height_labels[1],
            ),
        )
        self.wait(1)

        self.play(
            x.animate.set_value(1),
            Restore(slope_labels[0]),
            Restore(v_lines[0]),
            Restore(height_labels[0]),
        )

        self.play(Write(areas[0]), run_time=2)
        self.play(Write(area_labels[0]), run_time=2)

        self.play(
            x.animate.set_value(2),
            Transform(areas[0], areas[1]),
            Transform(area_labels[0], area_labels[1]),
            Transform(
                slope_labels[0],
                slope_labels[1],
            ),
            Transform(v_lines[0], v_lines[1]),
            Transform(
                height_labels[0],
                height_labels[1],
            ),
        )

        self.wait(1)

        # self.wait(2)
