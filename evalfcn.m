function ode=evalfcn(t, Y, phi)
    m = Y(1);
    u = Y(2);
    b = .1;
    g = 15;
    ode = [0;0];
    ode(1) = phi^2 * u * exp(g * b * (1-u) / (1 + b * (1-u)));
    ode(2) = m;