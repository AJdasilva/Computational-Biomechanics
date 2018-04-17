%Computational biomechanics ODE group
%Richard Touret

%clear all; 
close all;
format long;

%************1:importing the data set****************************
%Add the .txt file to matlab current folder (left)
%Then code the following: 
%Datafile = 'MathDatatxt.txt';
%Data = load(Datafile);
%Run it. After a few seconds, right click on Data and "save as" a .mat file.
%Then use the bellow code:

filename = 'MathDatatxt.mat';
load(filename);

%-------------2: Variable definitions from the data------------%
% t = time (seconds)
% FDC = Frame Displacement Command (mm)
% FD = Frame Displacement (mm)
% FFC = Framce Force Command (N)
% FF = Frame Force (N)
% FC = Frame Count (cycles)
% CO = Camera Output (v)
% CC = Camera Count (cycles)


%t, FDC, FD, FFC, FF, FC, CO, CC variables from dataset
Time = Data(:,1);
FDC = Data(:,2);
FD = Data(:,3);
FFC = Data(:,4);
FF = Data(:,5);
FC = Data(:,6);
CO = Data(:,7);
CC = Data(:,8);


YM = 19.6; %Young's modulus
aclwidth = 2; %mm
acllength=12.86; %mm



strain = (FD-FD(1))./(FD(1));
stress = FF ./ (aclwidth*FD);
stress2 = YM.*strain;




%tspan = [min(Time) 3500];
tspan= [min(Time) 500];
y0 = stress(1);
func = @(t,y) (1/(aclwidth*stress(1)))*(y);
[t,y] = ode45(func, tspan, y0);

tspan= [min(Time) 500];
x0 = strain(100);
func2 = @(t1,x) (1/(aclwidth*strain(1)))*(x);
[t1,x] = ode45(func2, tspan, x0);


plot(x,y,'-o')




%%%%%%NEW STUFF%%%%%%
tspan= [min(Time) 3500];
y0 = stress(1);
func = @(t,y) (1/(aclwidth*stress(1)))*(y);
[t,y] = ode45(func, tspan, y0);
plot(t,y,'-o')

tspan= [min(Time) 3500];
x0 = strain(50);
func2 = @(t1,x) (1/(aclwidth*strain(50)))*(x);
[t1,x] = ode45(func2, tspan, x0);
plot(t1,x,'-o')

plot(x,y,'-o')






% def model(y,t):
%     dydt = (1/(aclwidth*FD))*(y)
%     return dydt
% 
% y0 = FD[1]
% t3 = np.linspace(min(t),max(t))
% y = odeint(model, y0,t3)








%--------------------Plots-------------------%
% figure(1);
% subplot(2,1,1);
% graph1 = plot(strain,stress, 'r');
% set(graph1,'LineWidth', 2);
% title('Stress Strain curve');
% xlabel('Strain');
% ylabel('Stress');
% axis([0 0.1 0 inf]);



% subplot(2,1,2)
% graph2 = plot(Time2,stress); 
% set(graph2, 'LineWidth', 2);
% title('Time Stress curce');
% xlabel('Time (sec)');
% ylabel('Stress (NM^2)');
% axis([0 inf -inf inf]);
