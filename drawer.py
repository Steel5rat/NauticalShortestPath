import matplotlib.pyplot as pyplot


def show_plot(gates, path):
    for left_gate_border, right_gate_border in gates:
        pyplot.plot([left_gate_border.x, right_gate_border.x], [left_gate_border.y, right_gate_border.y], color='black', linewidth=1)
        pyplot.scatter([left_gate_border.x, right_gate_border.x], [left_gate_border.y, right_gate_border.y], color='black')


    x_path = [p.x for p in path]
    y_path = [p.y for p in path]
    pyplot.scatter(x_path, y_path, color='blue')
    pyplot.plot(x_path, y_path, color='blue')
    pyplot.grid(True, linestyle='--', alpha=0.5)
    pyplot.axis("equal")
    pyplot.show()
