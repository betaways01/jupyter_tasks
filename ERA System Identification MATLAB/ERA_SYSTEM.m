load C7E_1.mat t acc dt;
rng('default');

% Add noise to excitation and response signals
X_vars = acc + randn(size(t)) / 1250;
Y_vars = t + randn(size(t)) / 1e11;

% Define inpusample_time and outpusample_time
p = (0:size(X_vars, 1) - 1) / dt';
X1 = 1e2 * X_vars;
Y1 = 1e2 * Y_vars;
X0 = X1(:, 1);
Y0 = Y1(:, 1);

% plotting
% acc versus the time
subplot(2, 1, 1)
plot(p, X0)
xlabel('Frequency (1/t)')
ylabel('Viration Force (Newtons)')
grid on;
title('Excitation and Response for a System Constrained on 3 degrees of freedom')
subplot(2, 1, 2)
plot(p, Y0)
xlabel('Frequency (1/t)')
ylabel('Displacement (in meters)')
grid on;

% APPLYING ERA
sample_time = 1 / dt; % sample time to apply on the estimation data
data_estimation = iddata(Y0(1:1000), X0(1:1000), 1 / dt);
% incase we need to validate and compare systems, we need the validation data:
data_validation = iddata(Y0(1001:2000), X0(1001:2000), 1 / dt);

% plot on the estimation data
figure
plot(data_estimation)

[~, inputDelay] = max(data_estimation.InputData);
data_estimation = data_estimation(inputDelay:end);

L = length(data_estimation.InputData);
t = seconds(data_estimation.Tstart + (0:L - 1)' * sample_time);
y1 = data_estimation.OutputData;
tt = timetable(t, y1);

% ERA SYSTEM PROPRETIES
% 6 orders (x1 - x6)
order = 6;
sys = era(tt, order, 'Feedthrough', true);
sys;
