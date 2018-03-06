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



strain = (FD-FD(1))./(FD);
stress = FF ./ (aclwidth*FD);

stress2 = YM.*strain;



%--------------------Plots-------------------%
figure(1);
subplot(2,1,1);
graph1 = plot(strain,stress, 'r');
set(graph1,'LineWidth', 2);
title('Stress Strain curve');
xlabel('Strain');
ylabel('Stress');
axis([0 0.1 0 inf]);



subplot(2,1,2)
graph2 = plot(Time,stress); 
set(graph2, 'LineWidth', 2);
title('Time Stress curce');
xlabel('Time (sec)');
ylabel('Stress (NM^2)');
axis([0 inf -inf inf]);




