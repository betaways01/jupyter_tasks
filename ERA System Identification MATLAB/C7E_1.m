load C7E_1.mat acc dt t
rng('default');

% Add noise to excitation and response signals
acc = acc + randn(size(dt))/1250;
dt = dt + randn(size(dt))/1e11;

% Define outputs from function
t = (0:size(acc,1)-1)/t';
X1 = 1e2*acc;
Y1 = 1e2*dt;
X0 = X1(:,1);
Y0 = Y1(:,1);

subplot(2,1,1)
plot(t,X0)
xlabel('Time (in seconds)')
ylabel('Force (in Newtons)')
grid on;
title('Excitation and Response for a 3DOF system')
subplot(2,1,2)
plot(t,Y0)
xlabel('Time (s)')
ylabel('Displacement (m)')
grid on;

% setting the sample time
Ts = 1/t;
data_estimation = iddata(Y0(1:1000), X0(1:1000), 1/t);
data_val = iddata(Y0(1001:2000), X0(1001:2000), 1/t);

figure
plot(data_estimation)

[~,inputDelay] = max(data_estimation.InputData);
data_estimation = data_estimation(inputDelay:end);

L = length(data_estimation.InputData);
t = seconds(data_estimation.Tstart + (0:L-1)'*Ts);
y1 = data_estimation.OutputData;
tt = timetable(t,y1);

order = 5;
system = era(tt, order, 'Feedthrough', true);

compare(data_val,system);

system2 = ssest(data_estimation, order, 'Feedthrough', true);

compare(data_val,system,system2);
legend('Validation data','ERA','SSEST');

% Model Evaluation
[~,f] = modalfrf(system);
[fd, zeta] = modalfit(system,f,3);

zeta;

fd;

[frf,f] = modalfrf(system2);
[fd, zeta] = modalfit(system2,f,3);

% Model Comparison for the lower order
% lower order here is 4
order = 4;
system = era(tt, order, 'Feedthrough', true);
system2 = ssest(data_estimation, order, 'Feedthrough', true);

%model comparison with higher order = 6
compare(data_val,system,system2);
legend('Validation data','ERA','SSEST');
