close all
clc

% Specify the path to your CSV file
csvFilePath = 'D:\_benchmark.csv';

% Read the CSV file using the `readtable` function
dataTable = readtable(csvFilePath);

% % Display the contents of the table
% disp(dataTable);

% Extract data from columns 1
xData = dataTable(:, 1);
xArray = table2array(xData);

% Create a figure
figure;
hold on;

% Add labels and title
xlabel('Data input size');
ylabel('Compute time (s)');
% title('Benchmark performance');

% Set x and y axes to logarithmic scale
set(gca, 'XScale', 'log');
set(gca, 'YScale', 'log');

% Customize the grid by adjusting line properties
grid on;
grid(gca, 'minor'); % Display minor grid lines

% Extract data from columns 2
yData = dataTable(:, 2);
yArray = table2array(yData);

% Create a scatter plot with filled dots
% scatter(xArray, yArray, 'filled', 'MarkerFaceColor',"#0072BD");
plot(xArray, yArray, '-o', 'MarkerFaceColor',"#0072BD", 'LineWidth',1, 'MarkerSize',4)

% Connect the scatter dots with lines
% line(xArray, yArray, 'LineWidth', 1, color="#0072BD");

% Extract data from columns 4
yData = dataTable(:, 4);
yArray = table2array(yData);

% Create a scatter plot with filled dots
% scatter(xArray, yArray, 'filled', 'MarkerFaceColor',"#D95319");
plot(xArray, yArray, '-o', 'MarkerFaceColor',"#D95319", 'LineWidth',1, 'MarkerSize',4)

% Connect the scatter dots with lines
% line(xArray, yArray, 'LineWidth', 1, color="#D95319");

% Extract data from columns 6
yData = dataTable(:, 6);
yArray = table2array(yData);

% Create a scatter plot with filled dots
% scatter(xArray, yArray, 'filled', 'MarkerFaceColor',"#EDB120");
plot(xArray, yArray, '-o', 'MarkerFaceColor',"#EDB120", 'LineWidth',1, 'MarkerSize',4)

% Connect the scatter dots with lines
% line(xArray, yArray, 'LineWidth', 1, color=	"#EDB120");

% Extract data from columns 9
yData = dataTable(:, 9);
yArray = table2array(yData);

% Create a scatter plot with filled dots
% scatter(xArray, yArray, 'filled', 'MarkerFaceColor',"#7E2F8E");
plot(xArray, yArray, '-o', 'MarkerFaceColor',"#7E2F8E", 'LineWidth',1, 'MarkerSize',4)

% Connect the scatter dots with lines
% line(xArray, yArray, 'LineWidth', 1, color="#7E2F8E");

% Add a legend
legend('Pure Python','Numpy with Python','Numba with Python','Numba with Nuitka', 'Location', 'northwest');
hold off;

% Show the plot
shg;

saveas(gcf,'plot.svg');
exportgraphics(gcf,'plot.png','Resolution',300)