% code online at https://github.com/tsbertalan-homework/504hw7

beta = 0.1;
initialSlope = -.5;
x0 = [initialSlope 1];
tSpan = [0, 1];
phi_list =  [.1 .5 1.5, 2.0];

slowness = 10;  % larger values converge more slowly and carefully on the right initialSlope

for index=[1   2  3   4]
    phi = phi_list(index);
    disp(strcat('phi=', num2str(phi)))
    %varargout = ode45(ode,tspan,y0,options,varargin)
    [t, X] = ode45(@(t, y)evalfcn(t, y, phi), tSpan, x0);
    while abs(X(end, 2) - 0) > 0.0001
        initialSlope = initialSlope - (X(end, 2)) / slowness;
        x0 = [initialSlope 1];
        [t, X] = ode45(@(t, y)evalfcn(t, y, phi), tSpan, x0);
    end
    disp(strcat('initialSlope=', num2str(initialSlope)))
    figureHandle = figure(index);

    %     t is position, first column of X is m, second column of X is u
    plot(t, X(:, 2), '-');
    textHandle = xlabel('$z$');
    set(textHandle,'FontSize',14, 'Interpreter', 'latex');
    textHandle = ylabel('$u$ or $v$', 'Interpreter', 'latex');
    set(textHandle,'FontSize',14, 'Interpreter', 'latex');
    
    n = length(t);
    eta = 0;
    for i = 1:(n-1)
        eta = eta + t(i) * (X(i+1, 1) - X(i,1));
    end
    disp(strcat('eta=', num2str(eta)))

    hold on
    v = beta+1 - beta*X(:,1);
    plot(t, v, '--')
    textHandle = legend('$u$ (dimensionless concentration)', '$v$ (dimensionless temperature)');
    set(textHandle,'FontSize',14, 'Interpreter', 'latex');
    hold off
    title(strcat('\phi^2=', num2str(phi), ', \eta=', num2str(eta)))
    saveas(figureHandle,strcat('hw7-2f-phi_', num2str(phi), '.png'))
    disp(' ')
end