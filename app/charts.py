import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, name):
    fig, ax = plt.subplots() # Creating a figure and an axis.
    ax.bar(labels, values) # Creating a bar chart.
    plt.savefig(f'./imgs/{name}_bar.png')
    plt.close()
    
    
def generate_pie_chart(labels, values, name):
    # Creating a figure and an axis.
    fig, ax = plt.subplots()
    # Creating a pie chart.
    ax.pie(values, labels=labels)
    # Making the pie chart look like a circle.
    ax.axis('equal')
    plt.savefig(f'./imgs/{name}_pie.png')
    plt.close()
    
    
def generate_linear_chart(labels, values, name):
    # Plotting a line graph.
    plt.plot(labels, values)
    # Setting the label of the y-axis.
    plt.ylabel('Letters')
    # Setting the label of the x-axis.
    plt.ylabel('Numbers')
    plt.savefig(f'./imgs/{name}_linear.png')
    plt.close()
    

# if __name__ == "__main__":
    
#     labels = ['a', 'b', 'c', 'd']
#     values = [80, 100, 90, 115]
    
#     generate_bar_chart(labels, values)
#     generate_bar_chart(labels, values)
#     generate_pie_chart(labels, values)