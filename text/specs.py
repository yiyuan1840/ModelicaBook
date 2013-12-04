import os
import sys

sys.path.append(os.path.join(".", "source", "_sphinxext"))

from xogeny.gen_utils import *

## Simple Examples
fovars = [Var("x", legend="x")]
add_case(["SimpleExample", "FirstOrder$"], res="FO", stopTime=10);
add_simple_plot(plot="FO", vars=fovars, title="Simulation of FirstOrder")

focvars = [Var("x", legend="x (FirstOrder)")]
foivars = [Var("x", legend="x (FirstOrderInitial)")]
add_case(["SimpleExample", "FirstOrderInitial"], stopTime=10, res="FOI")
add_compare_plot(plot="FOI",
                 res1="FOI", v1=foivars,
                 res2="FO", v2=focvars,
                 title="Specifying (non-zero) Initial Conditions")

fosvars = [Var("x", legend="x (FirstOrderSteady)")]
add_case(["SimpleExample", "FirstOrderSteady"], stopTime=10, res="FOS")
add_compare_plot(plot="FOS",
                 res1="FOS", v1=fosvars,
                 res2="FO", v2=focvars,
                 title="Steady State Solution (vs. Dynamic Response)")

## Cooling Example
add_case(["NewtonCoolingWithDefaults"], stopTime=1, res="NCWD")
add_simple_plot(plot="NCWD", vars=[Var("T")], title="Cooling to Ambient",
                legloc="upper right", ylabel="Temperature")

## RLC
add_case(["RLC1"], stopTime=2, res="RLC1")
add_simple_plot(plot="RLC1", vars=[Var("V", legend="Output Voltage [V]", style="-"),
                                   Var("Vb", legend="Battery Voltage [V]", style="-.")],
                title="Circuit Response")

## RotationalSMD
sosvars = [Var("phi1", legend="Position of inertia 1 [rad]"),
           Var("phi2", legend="Position of inertia 2 [rad]"),
           Var("omega1", legend="Velocity of inertia 1 [rad/s]"),
           Var("omega2", legend="Velocity of inertia 2 [rad/s]")]
add_case(["SecondOrderSystemInitParams"], stopTime=5, res="SOSIP")
add_simple_plot(plot="SOSIP", vars=sosvars, title="Mechanical System Response")

add_case(["SecondOrderSystemInitParams"], stopTime=5, res="SOSIP1",
         mods={"phi1": 1.0})
add_simple_plot(plot="SOSIP1", vars=sosvars, title="Mechanical Response; phi1(0)=0")

## LotkaVolterra
lvvars = [Var("x", legend="Prey population"),
          Var("y", legend="Predator population")]

add_case(["ClassicModel$"], stopTime=140, res="LVCM")
add_simple_plot(plot="LVCM", vars=lvvars, title="Classic Lotka-Volterra")

add_case(["QuiescientModel$"], stopTime=140, res="LVQM")
add_simple_plot(plot="LVQM", vars=lvvars, title="Queiscient Model (trivial solution)")

add_case(["QuiescientModelUsingStart"], stopTime=140, res="LVQMUS")
add_simple_plot(plot="LVQMUS", vars=lvvars,
                title="Queiscient Model (using start values)")

## Cooling Revisited
ncdvars = [Var("T", legend="Temperature"),
           Var("T_inf", legend="Ambient Temperature")]
add_case(["NewtonCoolingDynamic"], stopTime=1, res="NCD")
add_simple_plot(plot="NCD", vars=ncdvars,
                title="Cooling to Time-Varying Ambient",
                legloc="upper right", ylabel="Temperature [K]")

add_case(["NewtonCoolingSteadyThenDynamic"], stopTime=1, res="NCSTD")
add_simple_plot("NCSTD", vars=ncdvars,
                title="Equilibrium Initialization",
                legloc="lower left", ylabel="Temperature [K]")

## Bouncing Ball
bbvars = [Var("h", legend="Height")]
add_case(["\.BouncingBall$"], stopTime=3, res="BB1")
add_simple_plot(plot="BB1", vars=bbvars,
                title="Simple Bouncing Ball Model",
                legloc="upper right", ylabel="Height [m]")
add_case(["\.BouncingBall$"], stopTime=5, res="BB2")
add_simple_plot(plot="BB2", vars=bbvars,
                title="Consequences of Numerical Event Detection",
                legloc="upper right", ylabel="Height [m]")

## Switched RLC
srlc_vvars = [Var("Vs", legend="Source Voltage [V]"),
              Var("V", legend="Response Voltage [V]")]
srlc_ivars = [Var("i_R", legend="Resistor Current [A]"),
              Var("i_C", legend="Capacitor Current [A]"),
              Var("i_L", legend="Inductor Current [A]")]
add_case(["SwitchedRLC\.SwitchedRLC"], stopTime=2, res="SRLC")
add_simple_plot(plot="SRLC", vars=srlc_vvars,
                title="Switched RLC Voltage Response",
                legloc="lower right")

generate()
