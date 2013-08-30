within ModelicaByExample.Functions.Nonlinearities;
model ExplicitEvaluation
  "Model that uses evaluates quadratic function explicitly"
  Real y;
equation
  y = Quadratic(2.0, 3.0, 1.0, time);
end ExplicitEvaluation;
