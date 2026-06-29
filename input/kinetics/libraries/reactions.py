#!/usr/bin/env python
# encoding: utf-8

name = "Think"
shortDesc = u"Think"
longDesc = u"""
P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002


 Hydrocarbon subset:

H. Hashemi, J.M. Christensen, S. Gersen, H. Levinsky, S.J. Klippenstein, P. Glarborg,
“High-Pressure Oxidation of Methane”, Combust. Flame 172 (2016) 349-364.

J. Gimenez-Lopez, C.T. Rasmussen, H. Hashemi, M.U. Alzueta, Y. Gao, P. Marshall, C.F. Goldsmith, P. Glarborg,
“Experimental and Kinetic Modeling Study of C2H2 Oxidation at High Pressure, Int. J. Chem. Kinet. 48 (2016) 724-738.

H. Hashemi, J.G. Jacobsen, C.T. Rasmussen, J.M. Christensen, P. Glarborg, S. Gersen, M. van Essen, H.B. Levinsky, S.J. Klippenstein, 
“High-Pressure Oxidation of Ethane”, Combust. Flame 182 (2017) 150-166.

 Nitrogen subset

P. Glarborg, J.A. Miller, B. Ruscic, S.J. Klippenstein
Modeling nitrogen chemistry in combustion
Progress in Energy and Combustion Science
Volume 67, July 2018, Pages 31-68
https://doi.org/10.1016/j.pecs.2018.01.002

Note: Reaxtion CHCHNO <=> C2H2 + NO was commented out since its rate violates the TST limit at 1000 K, 1 bar.
"""
entry(
    index = 1,
    label = "H + H <=> H2",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6.520e+17, 'cm^6/(mol^2*s)'),
        n = -1.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = { 'O': 14.0, '[H][H]': 0.0, 'O=C=O': 3.0 },
    ),
    duplicate = True,
)

# default units are cm, mole, sec, K, and cal/mole
# DH = Delta H_0(0 K) for the reaction in kcal/mol - for the direction written - when
# positive they are placed according to the type of reaction for the reverse reaction.
# *****************************************************************************
#    H2 subset                                                                *
#    O2 subset                                                                *
# *****************************************************************************
# Fuel Radicals: H, O
# New Radicals Formed: HO2, OH
# New Fuels: H2O
# *** Fuel Decomposition
entry(
    index = 2,
    label = "H + H + H2 <=> H2 + H2",
    kinetics = Arrhenius(
        A = (1.010e+17, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 3,
    label = "O + O <=> O2",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.890e+13, 'cm^6/(mol^2*s)'),
        n = 0.0,
        Ea = (-1788.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = { 'O': 5.0, '[C-]#[O+]': 2.0, 'O=C=O': 3.0, '[H][H]': 2.0 },
    ),
    
)

# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -103.3
entry(
    index = 4,
    label = "H + O2 <=> HO2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1310000000000.0, 'cm^3/(mol*s)'), n=0.572, Ea=(-203.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(7.2e+20, 'cm^6/(mol^2*s)'), n=-1.73, Ea=(536.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.9,
        T3 = (1e-30, 'K'),
        T1 = (2300.0, 'K'),
        efficiencies = { '[Ar]': 0.5, 'O': 14.0, 'O=C=O': 2.0, '[H][H]': 3.0 }
    ),
)

entry(
    index = 5,
    label = "H + O <=> OH",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.700e+18, 'cm^6/(mol^2*s)'),
        n = -1.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = { 'O': 5.0 },
    ),
    duplicate = True,
)

# SR Sellevag, Y Georgievskii, JA Miller, JPCA 112:5085 (2008).
# Replaced constant Fc with temperature dependent form.
# DH = -48.1
# *** Fuel Radical + Radical
entry(
    index = 6,
    label = "O + H2 <=> OH + H",
    kinetics = Arrhenius(
        A = (5.060e+04, 'cm^3/(mol*s)'),
        n = 2.67,
        Ea = (6290.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -101.7
entry(
    index = 7,
    label = "H + H + O2 <=> H2 + O2",
    kinetics = Arrhenius(
        A = (8.800e+22, 'cm^6/(mol^2*s)'),
        n = -1.835,
        Ea = (800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# JW Sutherland, JV Michael, AN Pirraglia, FL Nesbitt, RB Klemm, PCI 21:929 (1986).
# $$ Baulch 2005
# DH = 1.6
# *** Chemically Termolecular
entry(
    index = 8,
    label = "H + H + O2 <=> OH + OH",
    kinetics = Arrhenius(
        A = (4.000e+22, 'cm^6/(mol^2*s)'),
        n = -1.835,
        Ea = (800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# MP Burke, SJ Klippenstein, NC 9:1078 (2017).
# DH = -103.3
entry(
    index = 9,
    label = "H + O2 + O <=> OH + O2",
    kinetics = Arrhenius(
        A = (7.350e+22, 'cm^6/(mol^2*s)'),
        n = -1.835,
        Ea = (800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# MP Burke, SJ Klippenstein, NC 9:1078 (2017).
# DH = -85.3
entry(
    index = 10,
    label = "H + OH <=> H2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(25100000000000.0, 'cm^3/(mol*s)'), n=0.234, Ea=(-114.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.53e+21, 'cm^6/(mol^2*s)'), n=-1.81, Ea=(499.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.73,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = { '[Ar]': 0.5, 'O': 10.0, 'O=C=O': 2.0 }
    ),
)

entry(
    index = 11,
    label = "OH + H2 <=> H2O + H",
    kinetics = Arrhenius(
        A = (2.140e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (3449.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SR Sellevag, Y Georgievskii, JA Miller, JPCA 112:5085 (2008).
# DH = -117.8
# *** Fuel + Radical
# H2O + H is endothermic
# H2O + O is endothermic
# H2O + OH is an identity
# H2O + O2 is endothermic
# *** Fuel Radical Decomposition
# Included in H2/O2 submechanism
# *** Fuel Radical + Stable
entry(
    index = 12,
    label = "O + OH <=> O2 + H",
    kinetics = Arrhenius(
        A = (2.630e+18, 'cm^3/(mol*s)'),
        n = -1.783,
        Ea = (855.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# JV Michael, PECS 18:327 (1992).
# DH = -14.5
# *** Fuel Radical + Radical
# O2 + OH is endothermic
entry(
    index = 13,
    label = "O + OH <=> O2 + H",
    kinetics = Arrhenius(
        A = (1.610e+18, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (8662.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 14,
    label = "OH + OH <=> H2O2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5030000000000.0, 'cm^3/(mol*s)'), n=0.058, Ea=(-634.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.68e+25, 'cm^6/(mol^2*s)'), n=-3.358, Ea=(576.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.55,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = { 'N#N': 2.0, '[He]': 0.4, 'O': 10.0, 'O=C=O': 3.0 }
    ),
)

entry(
    index = 15,
    label = "OH + OH <=> O + H2O",
    kinetics = Arrhenius(
        A = (2.830e+13, 'cm^3/(mol*s)'),
        n = -0.764,
        Ea = (-460.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# SR Sellevag, Y Georgievskii, JA Miller, JPCA 113:4457 (2009).
# DH = -48.9
entry(
    index = 16,
    label = "OH + OH <=> O + H2O",
    kinetics = Arrhenius(
        A = (1.260e+04, 'cm^3/(mol*s)'),
        n = 2.531,
        Ea = (-1622.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 17,
    label = "H + O2 + OH <=> H2O + O2",
    kinetics = Arrhenius(
        A = (2.560e+22, 'cm^6/(mol^2*s)'),
        n = -1.835,
        Ea = (800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# MP Burke, SJ Klippenstein, LB Harding, PCI 34:547 (2013).
# DH = -16.1
# *** Chemically Termolecular
entry(
    index = 18,
    label = "H2O2 + H <=> H2O + OH",
    kinetics = Arrhenius(
        A = (3.350e+07, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (3654.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# MP Burke, SJ Klippenstein, NC 9:1078 (2017).
# DH = -117.8
# *****************************************************************************
#    H2O2 subset                                                              *
# *****************************************************************************
# Fuel Radicals: HO2
# New Radicals Formed: None
# New Fuels: None
# *** Fuel Decomposition
# Included in H2O submechanism
# *** Fuel + Radical
# H2O2 + O2 is endothermic
entry(
    index = 19,
    label = "H2O2 + H <=> HO2 + H2",
    kinetics = Arrhenius(
        A = (4.400e+01, 'cm^3/(mol*s)'),
        n = 3.45,
        Ea = (712.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJK, unpublished (2021).
# DH = -69.9
entry(
    index = 20,
    label = "H2O2 + O <=> HO2 + OH",
    kinetics = Arrhenius(
        A = (9.600e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (3970.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJK, unpublished (2021).
# DH = -17.2
entry(
    index = 21,
    label = "H2O2 + OH <=> HO2 + H2O",
    kinetics = Arrhenius(
        A = (1.510e+14, 'cm^3/(mol*s)'),
        n = -1.055,
        Ea = (-761.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# DH = -15.6
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
entry(
    index = 22,
    label = "H2O2 + OH <=> HO2 + H2O",
    kinetics = Arrhenius(
        A = (2.100e+03, 'cm^3/(mol*s)'),
        n = 2.957,
        Ea = (-1358.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 23,
    label = "HO2 + H <=> H2 + O2",
    kinetics = Arrhenius(
        A = (1.120e+07, 'cm^3/(mol*s)'),
        n = 1.941,
        Ea = (-645.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# MP Burke, SJ Klippenstein, LB Harding, PCI 34:547 (2013).
# DH = -31.7
# *** Fuel Radical Decomposition
# Included in H2/O2 submechanism
# *** Fuel Radical + Stable
# Nothing New
# *** Fuel Radical + Radical
# HO2 + O2 is identity or endothermic to O3 + OH
entry(
    index = 24,
    label = "HO2 + H <=> OH + OH",
    kinetics = Arrhenius(
        A = (6.670e+12, 'cm^3/(mol*s)'),
        n = 0.295,
        Ea = (-126.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJK 7/2011 fit by Mike Burke
# DH = -55.2
entry(
    index = 25,
    label = "HO2 + O <=> O2 + OH",
    kinetics = Arrhenius(
        A = (2.850e+10, 'cm^3/(mol*s)'),
        n = 1.0,
        Ea = (-724.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJK unpublished by Mike Burke
# DH = -37.2
entry(
    index = 26,
    label = "HO2 + OH <=> H2O + O2",
    kinetics = Arrhenius(
        A = (1.930e+20, 'cm^3/(mol*s)'),
        n = -2.488,
        Ea = (583.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# A Fernandez-Ramos, AJC Varandas, JPCA 106:4077-4083 (2002)
# Scaled by 0.60 to match experimental data at low T's
# $$ Hong et al. (2013)
# DH = -53.6
entry(
    index = 27,
    label = "HO2 + OH <=> H2O + O2",
    kinetics = Arrhenius(
        A = (1.210e+09, 'cm^3/(mol*s)'),
        n = 1.239,
        Ea = (-1307.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 28,
    label = "HO2 + HO2 <=> H2O2 + O2",
    kinetics = Arrhenius(
        A = (1.930e-02, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (-4960.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# MP Burke, SJ Klippenstein, LB Harding, PCI 34:547 (2013).
# DH = -69.7
entry(
    index = 29,
    label = "HO2 + HO2 <=> OH + OH + O2",
    kinetics = Arrhenius(
        A = (6.410e+17, 'cm^3/(mol*s)'),
        n = -1.54,
        Ea = (8540.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, R Sivaramakrishnan, U. Burke, KP Somers, HJ Curran, L Cai, H Pitsch, M Pelucchi, T Faravelli, P Glarborg, US Comb. 2019
# DH = -38.0
entry(
    index = 30,
    label = "CO2 <=> CO + O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.300e+23, 's^-1'),
        n = -4.335,
        Ea = (137445.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.400e+24, 's^-1'),
        n = -4.344,
        Ea = (137492.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (5.020e+24, 's^-1'),
        n = -4.352,
        Ea = (137524.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.600e+25, 's^-1'),
        n = -4.359,
        Ea = (137566.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (4.240e+25, 's^-1'),
        n = -4.333,
        Ea = (137444.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.780e+26, 's^-1'),
        n = -4.371,
        Ea = (137670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (5.530e+26, 's^-1'),
        n = -4.362,
        Ea = (137731.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.190e+26, 's^-1'),
        n = -4.293,
        Ea = (137671.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (4.290e+27, 's^-1'),
        n = -4.331,
        Ea = (138373.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.850e+27, 's^-1'),
        n = -4.242,
        Ea = (138781.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (6.730e+27, 's^-1'),
        n = -4.129,
        Ea = (139543.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (1.450e+26, 's^-1'),
        n = -3.577,
        Ea = (138771.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 300.0 atm
        Arrhenius(
            A = (3.820e+24, 's^-1'),
        n = -3.061,
        Ea = (138265.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# SJ Klippenstein, R Sivaramakrishnan, U. Burke, KP Somers, HJ Curran, L Cai, H Pitsch, M Pelucchi, T Faravelli, P Glarborg, US Comb. 2019
# DH = ??
# *****************************************************************************
#    CO subset                                                                *
#    CO2 subset                                                               *
# *****************************************************************************
# Fuel Radicals: None
# New Radicals Formed: HCO, OCOH
# New Fuels: None
# *** Fuel Decomposition

entry(
    index = 31,
    label = "CO + O2 <=> CO2 + O",
    kinetics = Arrhenius(
        A = (4.700e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (60500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, JPCA 119:7339 (2015)
# AW Jasper - unpublished
# DH = 125.9
# CO decomposition to C + O is too endothermic to be important
# *** Fuel + Radical
entry(
    index = 32,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(37900000000.0, 's^-1'), n=1.079, Ea=(18390.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2760000000000000.0, 'cm^3/(mol*s)'), n=-0.504, Ea=(15295.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.09,
        T3 = (1e-20, 'K'),
        T1 = (-2200.0, 'K'),
        T2 = (1e+20, 'K'),
        efficiencies = { '[He]': 0.71, '[Ar]': 0.61, '[H][H]': 1.5, 'C': 3.0, 'O=C=O': 2.0, 'O': 7.0 }
    ),
)

entry(
    index = 33,
    label = "CO + OH <=> OCOH",
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.660e+15, 'cm^3/(mol*s)'),
        n = -2.68,
        Ea = (859.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (5.890e+18, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (887.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (2.570e+20, 'cm^3/(mol*s)'),
        n = -3.5,
        Ea = (1309.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (7.080e+20, 'cm^3/(mol*s)'),
        n = -3.32,
        Ea = (1763.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (1.120e+20, 'cm^3/(mol*s)'),
        n = -2.78,
        Ea = (2056.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# Unpublished data from SJ Klippenstein - closely related to
# NJ Labbe, R Sivaramakrishnan, CF Goldsmith, Y Georgievskii, JA Miller, SJ Klippenstein, JPCL 7:85 (2016).
# DH = 14.7

entry(
    index = 34,
    label = "CO + OH <=> CO2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.0132, 0.132, 1.31, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.140e+05, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (-1064.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (2.450e+05, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (-1043.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (8.710e+05, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (-685.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.31 atm
        Arrhenius(
            A = (6.760e+06, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (48.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (2.340e+07, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (974.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, PCI 30:945 (2005).
# DH = -25.2

entry(
    index = 35,
    label = "CO + HO2 <=> CO2 + OH",
    kinetics = Arrhenius(
        A = (1.570e+05, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17943.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, PCI 30:945 (2005).
# DH = -24.2
entry(
    index = 36,
    label = "OCOH <=> CO2 + H",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(820000000000.0, 's^-1'), n=0.413, Ea=(35335.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6e+26, 'cm^3/(mol*s)'), n=-3.148, Ea=(37116.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.39,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K')
    ),
)
#  DM Golden GP Smith AB McEwen C-L Yu B Eiteneer M Frenklach GL Vaghjiani AR Ravishankara FP Tully JPCA 102:8598 (1998).
#  DH = 1.0
#  *** Fuel Radical Decomposition
#  *** Fuel Radical + Stable
#  *** Fuel Radical + Radical
#  *****************************************************************************
#     CH2O subset                                                              *
#     includes CHOH, CHOH(T)                                                   *
#  *****************************************************************************
#  Fuel Radicals: HCO
#  New Radicals Formed: None
#  New Fuels: None
#  *** Fuel Decomposition
# FNEMECHGEN: This reaction has had fne factor applied

entry(
    index = 38,
    label = "CH2O <=> H + CO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.712e+31, 's^-1'),
        n = -6.366,
        Ea = (110768.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (7.525e+31, 's^-1'),
        n = -6.358,
        Ea = (110578.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (2.312e+32, 's^-1'),
        n = -6.349,
        Ea = (110388.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.558e+32, 's^-1'),
        n = -6.342,
        Ea = (110228.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (3.011e+33, 's^-1'),
        n = -6.377,
        Ea = (110400.2, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.488e+34, 's^-1'),
        n = -6.431,
        Ea = (110669.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (8.859e+34, 's^-1'),
        n = -6.495,
        Ea = (110926.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.153e+35, 's^-1'),
        n = -6.632,
        Ea = (111206.5, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (7.375e+37, 's^-1'),
        n = -6.995,
        Ea = (112026.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.733e+39, 's^-1'),
        n = -7.221,
        Ea = (112661.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (9.829e+39, 's^-1'),
        n = -7.264,
        Ea = (113349.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

entry(
    index = 39,
    label = "CH2O <=> CO + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.280e+24, 's^-1'),
        n = -4.659,
        Ea = (77800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (5.650e+24, 's^-1'),
        n = -4.628,
        Ea = (78630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (1.530e+25, 's^-1'),
        n = -4.595,
        Ea = (79540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.790e+25, 's^-1'),
        n = -4.564,
        Ea = (80370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (1.120e+26, 's^-1'),
        n = -4.543,
        Ea = (81320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.820e+26, 's^-1'),
        n = -4.517,
        Ea = (82170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (5.470e+26, 's^-1'),
        n = -4.449,
        Ea = (83040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.030e+26, 's^-1'),
        n = -4.351,
        Ea = (83760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (5.530e+26, 's^-1'),
        n = -4.194,
        Ea = (84380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.720e+26, 's^-1'),
        n = -3.951,
        Ea = (84680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.290e+25, 's^-1'),
        n = -3.535,
        Ea = (84650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

entry(
    index = 40,
    label = "CHOH(T) <=> CHOH",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = None,
    ),
    
)


entry(
    index = 42,
    label = "CH2O + H <=> H + CO + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.251e+08, 'cm^3/(mol*s)'),
        n = 1.853,
        Ea = (11734.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03947 atm
        Arrhenius(
            A = (5.144e+07, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (11525.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.168e+09, 'cm^3/(mol*s)'),
        n = 1.812,
        Ea = (13164.2, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

entry(
    index = 43,
    label = "CH3O <=> H + CH2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.32e+16, 's^-1'), n=-0.588, Ea=(26772.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.33e+25, 'cm^3/(mol*s)'), n=-2.981, Ea=(22465.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.1698,
        T3 = (1e-09, 'K'),
        T1 = (807456.9, 'K'),
        T2 = (7029.4, 'K'),
        efficiencies = { '[Ar]': 0.7, '[H][H]': 2.0, 'C': 3.0, 'C#C': 3.0, 'C=C': 3.0, 'CC': 3.0, 'CCC': 3.0, 'C=CC': 3.0, 'CC#C': 3.0, 'C=C=C': 3.0, 'O': 5.0 }
    ),
)

entry(
    index = 44,
    label = "CH2OH <=> H + CH2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(0.006404, 's^-1'), n=4.764, Ea=(32482.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.97e+29, 'cm^3/(mol*s)'), n=-4.038, Ea=(33743.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.1739,
        T3 = (1e-06, 'K'),
        T1 = (3302.0, 'K'),
        T2 = (10570.9, 'K'),
        efficiencies = { '[Ar]': 0.7, '[H][H]': 2.0, 'C': 3.0, 'C#C': 3.0, 'C=C': 3.0, 'CC': 3.0, 'CCC': 3.0, 'C=CC': 3.0, 'CC#C': 3.0, 'C=C=C': 3.0, 'O': 5.0 }
    ),
)

entry(
    index = 46,
    label = "CH2O + O <=> H + CO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.744e+20, 'cm^3/(mol*s)'),
        n = -1.789,
        Ea = (21560.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03947 atm
        Arrhenius(
            A = (2.490e+21, 'cm^3/(mol*s)'),
        n = -1.903,
        Ea = (22678.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.262e+21, 'cm^3/(mol*s)'),
        n = -1.982,
        Ea = (23601.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -15.0

entry(
    index = 48,
    label = "CH2O + OH <=> H + CO + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.301e+11, 'cm^3/(mol*s)'),
        n = 0.711,
        Ea = (8708.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03947 atm
        Arrhenius(
            A = (2.587e+11, 'cm^3/(mol*s)'),
        n = 0.692,
        Ea = (9372.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.737e+11, 'cm^3/(mol*s)'),
        n = 0.679,
        Ea = (9905.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

entry(
    index = 49,
    label = "CH2OCHO <=> CH2O + HCO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3680.0, 's^-1'), n=3.093, Ea=(27639.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.24e+30, 'cm^3/(mol*s)'), n=-4.192, Ea=(28490.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.012,
        T3 = (633.8, 'K'),
        T1 = (628.2, 'K'),
        T2 = (5541.6, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)


#  Fit by R. Sivaramakrishnan to unpublished results from SJK
#  The low pressure limit has been scaled by 1.42 to set N2 as the bath gas (3.688E+30 x 1.42 = 5.237E+30)
#  DH = -20.2
#  *** Fuel Radical Decomposition
#  Included in CO submechanism
#  *** Fuel Radical + Stable
# FNEMECHGEN: This reaction has had fne factor applied

entry(
    index = 51,
    label = "CH2O + HO2 <=> H + CO + H2O2",
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.618e+13, 'cm^3/(mol*s)'),
        n = 0.141,
        Ea = (29011.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03947 atm
        Arrhenius(
            A = (2.454e+14, 'cm^3/(mol*s)'),
        n = 0.027,
        Ea = (30129.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.187e+14, 'cm^3/(mol*s)'),
        n = -0.052,
        Ea = (31052.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# FNEMECHGEN: CONTINUED for CH2O+HO2=HCO+H2O2

entry(
    index = 52,
    label = "HCO + O2 <=> HO2 + CO",
    kinetics = Arrhenius(
        A = (7.830e+10, 'cm^3/(mol*s)'),
        n = 0.521,
        Ea = (-521.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## J. PHYS. CHEM. A 109, 12027-12035, 2005
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 0.6
# *** Fuel Radical + Radical
entry(
    index = 53,
    label = "HCO + H <=> CO + H2",
    kinetics = Arrhenius(
        A = (1.250e+13, 'cm^3/(mol*s)'),
        n = 0.267,
        Ea = (-386.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished calculation, 2011.
# DH = -33.4
entry(
    index = 54,
    label = "HCO + O <=> CO2 + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, LB Harding, unpublished (2021).
# DH = -88.6
entry(
    index = 55,
    label = "HCO + O <=> CO + OH",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, P Glarborg - estimate
# $$ Baulch (2005).
# DH = -111.2
entry(
    index = 56,
    label = "HCO + OH <=> H2 + CO2",
    kinetics = Arrhenius(
        A = (2.630e+12, 'cm^3/(mol*s)'),
        n = -0.021,
        Ea = (-169.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, P Glarborg - estimate
# $$ Baulch (2005).
# DH = -87.0
entry(
    index = 57,
    label = "HCO + OH <=> H2O + CO",
    kinetics = Arrhenius(
        A = (4.610e+13, 'cm^3/(mol*s)'),
        n = 0.011,
        Ea = (-115.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished calculation, 2013.
# DH = -112.8
entry(
    index = 58,
    label = "HCO + HO2 <=> CO + H2O2",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished calculation, 2013.
# abstraction + addition/elimination
# DH = -103.1

entry(
    index = 60,
    label = "CH2O + O2 <=> H + CO + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.696e+25, 'cm^3/(mol*s)'),
        n = -2.359,
        Ea = (72215.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03947 atm
        Arrhenius(
            A = (4.831e+25, 'cm^3/(mol*s)'),
        n = -2.473,
        Ea = (73333.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.021e+26, 'cm^3/(mol*s)'),
        n = -2.552,
        Ea = (74256.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# FNEMECHGEN: CONTINUED for CH2O+O2=HCO+HO2

entry(
    index = 61,
    label = "OCHCHO <=> CH2O + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.00987, 0.0494, 0.0987, 0.494, 0.987, 4.94, 9.87], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.200e+53, 's^-1'),
        n = -12.5,
        Ea = (70845.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm
        Arrhenius(
            A = (5.100e+54, 's^-1'),
        n = -12.6,
        Ea = (73012.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0494 atm
        Arrhenius(
            A = (1.000e+55, 's^-1'),
        n = -12.6,
        Ea = (73877.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm
        Arrhenius(
            A = (4.500e+55, 's^-1'),
        n = -12.6,
        Ea = (75869.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.494 atm
        Arrhenius(
            A = (8.000e+55, 's^-1'),
        n = -12.6,
        Ea = (76713.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm
        Arrhenius(
            A = (1.100e+56, 's^-1'),
        n = -12.2,
        Ea = (77643.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 4.94 atm
        Arrhenius(
            A = (5.500e+56, 's^-1'),
        n = -12.6,
        Ea = (79964.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm
        ],
    ),
)

# NK Srinivasan, MC Su, JW Sutherland, JV Michael, JPCA 109:7902 (2005).
# DH = 38.6

entry(
    index = 62,
    label = "OCHCHO <=> CHOH + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.00987, 0.0494, 0.0987, 0.494, 0.987, 4.94, 9.87], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.400e+52, 's^-1'),
        n = -12.6,
        Ea = (72393.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm
        Arrhenius(
            A = (8.300e+54, 's^-1'),
        n = -12.9,
        Ea = (75113.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0494 atm
        Arrhenius(
            A = (4.400e+55, 's^-1'),
        n = -13.0,
        Ea = (76257.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm
        Arrhenius(
            A = (1.300e+57, 's^-1'),
        n = -13.2,
        Ea = (78851.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.494 atm
        Arrhenius(
            A = (2.600e+57, 's^-1'),
        n = -13.2,
        Ea = (79754.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm
        Arrhenius(
            A = (1.000e+57, 's^-1'),
        n = -12.9,
        Ea = (81161.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 4.94 atm
        Arrhenius(
            A = (5.700e+59, 's^-1'),
        n = -13.3,
        Ea = (83539.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm
        ],
    ),
)

# G Friedrichs, M Colberg, J Dammeier, T Bentz, M Olzmann PCCP 10:6520 (2008).
# DH = ??

entry(
    index = 63,
    label = "OCHCHO <=> CO + CO + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.00987, 0.0494, 0.0987, 0.494, 0.987, 4.94, 9.87], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.000e+51, 's^-1'),
        n = -12.1,
        Ea = (71854.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm
        Arrhenius(
            A = (1.400e+54, 's^-1'),
        n = -12.5,
        Ea = (74751.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0494 atm
        Arrhenius(
            A = (1.800e+55, 's^-1'),
        n = -12.7,
        Ea = (76137.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm
        Arrhenius(
            A = (1.300e+57, 's^-1'),
        n = -13.0,
        Ea = (78972.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.494 atm
        Arrhenius(
            A = (6.100e+57, 's^-1'),
        n = -13.1,
        Ea = (80147.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm
        Arrhenius(
            A = (5.800e+57, 's^-1'),
        n = -12.9,
        Ea = (81871.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 4.94 atm
        Arrhenius(
            A = (3.400e+59, 's^-1'),
        n = -13.3,
        Ea = (84294.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm
        ],
    ),
)

# G Friedrichs, M Colberg, J Dammeier, T Bentz, M Olzmann PCCP 10:6520 (2008).
# DH = ??

entry(
    index = 64,
    label = "OCHCHO <=> HCO + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.00987, 0.0494, 0.0987, 0.494, 0.987, 4.94, 9.87], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.000e+42, 's^-1'),
        n = -9.7,
        Ea = (73534.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm
        Arrhenius(
            A = (6.000e+48, 's^-1'),
        n = -11.1,
        Ea = (77462.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0494 atm
        Arrhenius(
            A = (1.700e+51, 's^-1'),
        n = -11.6,
        Ea = (79111.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm
        Arrhenius(
            A = (5.300e+55, 's^-1'),
        n = -12.5,
        Ea = (82774.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.494 atm
        Arrhenius(
            A = (1.900e+57, 's^-1'),
        n = -12.8,
        Ea = (84321.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm
        Arrhenius(
            A = (2.200e+59, 's^-1'),
        n = -13.1,
        Ea = (87258.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 4.94 atm
        Arrhenius(
            A = (3.000e+60, 's^-1'),
        n = -13.3,
        Ea = (88993.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm
        ],
    ),
)

# G Friedrichs, M Colberg, J Dammeier, T Bentz, M Olzmann PCCP 10:6520 (2008).
# DH = ??

entry(
    index = 65,
    label = "HCO + HCO <=> CO + CH2O",
    kinetics = Arrhenius(
        A = (2.700e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# G Friedrichs, M Colberg, J Dammeier, T Bentz, M Olzmann PCCP 10:6520 (2008).
# DH = ??
# OCHCHO+M=HCO+HCO+M                       	1.00E+17    0.000   58000
# JA Miller - estimate
# DH = 69.2
entry(
    index = 66,
    label = "CHOH + H <=> HCO + H2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# G Friedrichs, JT Herbon, DF Davidson, RK Hanson, PCCP 4:5778 (2002).
# DH = -72.0
# *** CHOH + Radical
# CHOH+O2=CO2+H+OH
# ## Missing
# CHOH+O2=CO2+H2O
# ## Missing
entry(
    index = 67,
    label = "CHOH + H <=> CH2O + H",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -68.8
entry(
    index = 68,
    label = "CHOH + O <=> CO + H + OH",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -52.1
entry(
    index = 69,
    label = "CHOH + OH <=> HCO + H2O",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -52.5
# CHOH+O=CO2+H+H
# ## Missing
entry(
    index = 70,
    label = "CHOH(T) + O2 <=> CO2 + H2O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -83.3
# *** CHOH(T) + Radical
entry(
    index = 71,
    label = "CHOH(T) + O2 <=> CO2 + H + OH",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 72,
    label = "OCHOH <=> CO + H2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(750000000000000.0, 's^-1'), n=0.0, Ea=(68710.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4100000000000000.0, 'cm^3/(mol*s)'), n=0.0, Ea=(52980.0, 'cal/mol'), T0=(1, 'K'))
    ),
)

entry(
    index = 73,
    label = "OCHOH <=> CO2 + H2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(45000000000000.0, 's^-1'), n=0.0, Ea=(68240.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1700000000000000.0, 'cm^3/(mol*s)'), n=0.0, Ea=(51110.0, 'cal/mol'), T0=(1, 'K'))
    ),
)

entry(
    index = 74,
    label = "OCHOH + H <=> OCOH + H2",
    kinetics = Arrhenius(
        A = (2.300e+02, 'cm^3/(mol*s)'),
        n = 3.272,
        Ea = (4858.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JG Chang, HT Chen, S Xu, M Lin, JPCA 111:6789 (2007).
# DH = ??
entry(
    index = 75,
    label = "OCHOH + H <=> CO2 + H + H2",
    kinetics = Arrhenius(
        A = (4.200e+05, 'cm^3/(mol*s)'),
        n = 2.255,
        Ea = (14091.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 76,
    label = "OCHOH + O <=> OCOH + OH",
    kinetics = Arrhenius(
        A = (5.100e+01, 'cm^3/(mol*s)'),
        n = 3.422,
        Ea = (4216.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 77,
    label = "OCHOH + O <=> CO2 + H + OH",
    kinetics = Arrhenius(
        A = (1.700e+05, 'cm^3/(mol*s)'),
        n = 2.103,
        Ea = (9880.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 78,
    label = "OCHOH + OH <=> OCOH + H2O",
    kinetics = Arrhenius(
        A = (7.800e-06, 'cm^3/(mol*s)'),
        n = 5.57,
        Ea = (-2365.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 79,
    label = "OCHOH + OH <=> CO2 + H + H2O",
    kinetics = Arrhenius(
        A = (4.900e-05, 'cm^3/(mol*s)'),
        n = 4.91,
        Ea = (-5067.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JM Anglada, JACS 126:9809 (2004).
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 80,
    label = "OCHOH + HO2 <=> OCOH + H2O2",
    kinetics = Arrhenius(
        A = (4.700e-01, 'cm^3/(mol*s)'),
        n = 3.975,
        Ea = (16787.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JM Anglada, JACS 126:9809 (2004).
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 81,
    label = "OCHOH + HO2 <=> CO2 + H + H2O2",
    kinetics = Arrhenius(
        A = (3.900e+01, 'cm^3/(mol*s)'),
        n = 3.08,
        Ea = (25206.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 82,
    label = "OCHOH + O2 <=> CO2 + H + HO2",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (63000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Marshall, P Glarborg, PCI 35:153 (2015).
entry(
    index = 83,
    label = "OCOH + O2 <=> CO2 + HO2",
    kinetics = Arrhenius(
        A = (4.000e+09, 'cm^3/(mol*s)'),
        n = 1.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)


entry(
    index = 84,
    label = "OCOH + H <=> CO2 + H2",
    kinetics = Arrhenius(
        A = (3.100e+17, 'cm^3/(mol*s)'),
        n = -1.348,
        Ea = (555.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# Fit of the data from
# HG Yu, JT Muckerman, JPC A 110:5312 (2006).
# by
# P Marshall, P Glarborg, PCI 35:153 (2015).
# DH = -47.1
entry(
    index = 85,
    label = "OCOH + H <=> CO + H2O",
    kinetics = Arrhenius(
        A = (6.000e+15, 'cm^3/(mol*s)'),
        n = -0.525,
        Ea = (2125.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# Fit of the data from
# HG Yu, JS Francisco, JCP 128:244315 (2008).
# over the 300 - 1000 K range by
# P Marshall, P Glarborg, PCI 35:153 (2015).
# DH = -102.3
entry(
    index = 86,
    label = "OCOH + O <=> CO2 + OH",
    kinetics = Arrhenius(
        A = (9.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# Fit of the data from
# HG Yu, JS Francisco, JCP 128:244315 (2008).
# over the 300 - 1000 K range by
# P Marshall, P Glarborg, PCI 35:153 (2015).
# DH = -92.6
entry(
    index = 87,
    label = "OCOH + OH <=> CO2 + H2O",
    kinetics = Arrhenius(
        A = (4.560e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-89.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# HG Yu, JT Muckerman, JS Francisco, JCP 127:094302 (2007).
# DH = -100.7
entry(
    index = 88,
    label = "OCOH + OH <=> CO2 + H2O",
    kinetics = Arrhenius(
        A = (9.550e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (-89.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 89,
    label = "CO + H2O2 <=> OCOH + OH",
    kinetics = Arrhenius(
        A = (3.600e+04, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (28662.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# HG Yu, JT Muckerman, JS Prancisco, JPCA 109:5230 (2005).
# DH = -116.8
entry(
    index = 90,
    label = "OCOH + HO2 <=> CO2 + H2O2",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Glarborg, P Marshall, CPL 475:40 (2009).
# DH = 23.7
entry(
    index = 91,
    label = "OCOH + HO2 <=> OCHOH + O2",
    kinetics = Arrhenius(
        A = (4.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# HG Yu, G Poggi, JS Francisco, JT Muckerman, JCP 129:214307 (2008).
# DH = -85.1
entry(
    index = 92,
    label = "CH3 + H <=> CH4",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(79270000000000.0, 'cm^3/(mol*s)'), n=0.148, Ea=(-3.8, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.227e+32, 'cm^6/(mol^2*s)'), n=-4.406, Ea=(2231.1, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.3497,
        T3 = (253.65, 'K'),
        T1 = (1840000000.0, 'K'),
        T2 = (5487.17, 'K'),
        efficiencies = { '[H][H]': 4.5, 'O': 6.3, 'N#N': 1.45, '[O][O]': 1.45, '[C-]#[O+]': 1.45, 'O=C=O': 5.6, 'C': 5.6, 'CC': 5.6 }
    ),
)

entry(
    index = 93,
    label = "CH4 + OH <=> CH3 + H2O",
    kinetics = Arrhenius(
        A = (1.000e+06, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (2446.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CH3+H(+M)=CH4(+M)                         	6.93E+13    0.180       0
#   LOW /  1.134E+31    -4.115   2238/
#   TROE / 7.0000E-01      1.0063E+04      4.5610E+02/
#     H2/2.86/ H2O/8.57/ CH4/2.86/ CO/2.14/ CO2/2.86/ C2H6/4.29/ N2/1.43/
#  High P limit from LB Harding, Y Georgievskii, SJ Klippenstein, JPCA 109: 4646 (2005).
#  Low P from  NJ Labbe 2/2016 (improvement at high and low T)
#  Falloff in Ar (alpha=115*(T/300)^.75) from trajectories of AW Jasper, JA Miller, unpublished (2010).
#  Very good agreement with the empirical alpha of JA Miller, SJ Klippenstein, C Raffy, JPCA 106: 4904 (2002).
#  DH = -103.4
#  *** Fuel + Radical
#  CH4 + O2 is endothermic
#  CH4 + H is endothermic by 0.1 kcal/mol
#  CH4 + O is endothermic by 0.7 kcal/mol
entry(
    index = 94,
    label = "CH2 + H <=> CH3",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.200e+23, 'cm^6/(mol^2*s)'),
        n = -2.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = { '[H][H]': 2.86, 'O': 8.57, 'C': 4.23, '[C-]#[O+]': 2.14, 'O=C=O': 2.86, 'CC': 4.23, 'N#N': 1.43, '[He]': 1.0 },
    ),
    
)

# NK Srinivasan, MC Su, JW Sutherland, JV Michael, JPCA 109:1857 (2005).
# DH = -66.1
# CH4 + HO2 is endothermic
# CH4 + HCO is endothermic
# *** Fuel Radical Decompositions
entry(
    index = 95,
    label = "CH + H2 <=> CH3",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.200e+23, 'cm^6/(mol^2*s)'),
        n = -2.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = { '[H][H]': 2.86, 'O': 8.57, 'C': 4.23, '[C-]#[O+]': 2.14, 'O=C=O': 2.86, 'CC': 4.23, 'N#N': 1.43, '[He]': 1.0 },
    ),
    
)

# KP Lim, JV Michael, PCI 25:713 (1994)
# (2000 - 2500 K, reverse), 298 K est as CH3+H+M
# DH = -109.2
entry(
    index = 96,
    label = "CH4 + H <=> CH3 + H2",
    kinetics = Arrhenius(
        A = (4.080e+03, 'cm^3/(mol*s)'),
        n = 3.16,
        Ea = (8755.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# KP Lim, JV Michael, PCI 25:713 (1994)
# (2000 - 2500 K, reverse), 298 K est as CH3+H+M
# DH = -105.9
# *** Fuel Radical + Stable
entry(
    index = 97,
    label = "CH4 + HO2 <=> CH3 + H2O2",
    kinetics = Arrhenius(
        A = (4.700e+04, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (21003.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JW Sutherland, MC Su, JV Michael, IJCK 33:669 (2001).
# $$ Baulch (2005).
# DH = 0.1
entry(
    index = 98,
    label = "CH3CO <=> CH3 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.880e+14, 's^-1'),
        n = -1.97,
        Ea = (14585.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.400e+15, 's^-1'),
        n = -2.0,
        Ea = (14805.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.960e+16, 's^-1'),
        n = -2.09,
        Ea = (15197.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.450e+18, 's^-1'),
        n = -2.52,
        Ea = (16436.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.180e+19, 's^-1'),
        n = -2.55,
        Ea = (17263.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.260e+20, 's^-1'),
        n = -2.32,
        Ea = (18012.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# ## J. AGUILERA-IPARRAGUIRRE ET AL. J PHYS CHEM A (2008) 112(30): 7047-7054.
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 17.3

entry(
    index = 99,
    label = "CH2CHO <=> CH3 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.160e+30, 's^-1'),
        n = -6.07,
        Ea = (41332.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.540e+31, 's^-1'),
        n = -6.27,
        Ea = (42478.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (6.370e+32, 's^-1'),
        n = -6.57,
        Ea = (44282.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.510e+34, 's^-1'),
        n = -6.87,
        Ea = (47191.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.150e+35, 's^-1'),
        n = -6.76,
        Ea = (49548.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.230e+33, 's^-1'),
        n = -5.97,
        Ea = (50448.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# k_inf             1.07E+12       0.630       16895
# JP Senosiain, SJ Klippenstein, JA Miller 110:5772 (2006).
# DH = 9.69

entry(
    index = 100,
    label = "CH3OCO <=> CH3 + CO2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3560000000000.0, 's^-1'), n=0.306, Ea=(13500.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(322000000000000.0, 'cm^3/(mol*s)'), n=0.225, Ea=(7221.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.217,
        T3 = (94.0, 'K'),
        T1 = (2363.1, 'K'),
        T2 = (4091.5, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 101,
    label = "CH3CH2O <=> CH3 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.05, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.770e+21, 's^-1'),
        n = -3.915,
        Ea = (16890.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.440e+22, 's^-1'),
        n = -4.017,
        Ea = (17386.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (5.020e+23, 's^-1'),
        n = -4.213,
        Ea = (17883.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.660e+25, 's^-1'),
        n = -4.589,
        Ea = (19274.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.840e+27, 's^-1'),
        n = -4.839,
        Ea = (20864.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.050e+26, 's^-1'),
        n = -4.18,
        Ea = (21460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# Fit to unpublished results SJK
# DH = -22.0

entry(
    index = 103,
    label = "CH2O + CH3 <=> H + CO + CH4",
    kinetics = PDepArrhenius(
        pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.705e+10, 'cm^3/(mol*s)'),
        n = 1.001,
        Ea = (23110.9, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03947 atm
        Arrhenius(
            A = (1.910e+11, 'cm^3/(mol*s)'),
        n = 0.887,
        Ea = (24228.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.035e+11, 'cm^3/(mol*s)'),
        n = 0.808,
        Ea = (25151.1, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# FNEMECHGEN: CONTINUED for CH2O+CH3=HCO+CH4

entry(
    index = 104,
    label = "CH3 + O2 <=> CH3OO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7810000000.0, 'cm^3/(mol*s)'), n=0.9, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.86e+24, 'cm^6/(mol^2*s)'), n=-3.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.33,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = { '[H][H]': 2.86, 'O': 8.57, 'C': 4.23, '[C-]#[O+]': 2.14, 'O=C=O': 2.86, 'CC': 4.23, 'N#N': 1.0, '[He]': 1.0 }
    ),
)

entry(
    index = 105,
    label = "CH3 + O2 <=> CH2O + OH",
    kinetics = Arrhenius(
        A = (6.390e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (13514.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# RX Fernandes, K Luther, J Troe, JPCA 110:4442 (2006).
# DH = -30.4
entry(
    index = 106,
    label = "CH3 + O <=> CO + H2 + H",
    kinetics = Arrhenius(
        A = (8.310e+12, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (-136.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NK Srinivasan, MC Su, JV Michael, JPCA 111:11589 (2007).
# DH = -52.1
entry(
    index = 107,
    label = "CH3 + O <=> CH2O + H",
    kinetics = Arrhenius(
        A = (4.710e+13, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (-136.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# LB Harding, SJ Klippenstein, Y Georgievskii, PCI 30:985 (2005).
# JA Miller - 15% branching from roaming
# DH = -70.5
entry(
    index = 108,
    label = "CH3 + OH <=> CH3OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.930e+30, 'cm^3/(mol*s)'),
        n = -6.638,
        Ea = (2829.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (1.050e+32, 'cm^3/(mol*s)'),
        n = -6.637,
        Ea = (3364.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (1.490e+32, 'cm^3/(mol*s)'),
        n = -6.361,
        Ea = (3954.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (5.690e+30, 'cm^3/(mol*s)'),
        n = -5.648,
        Ea = (4213.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (1.380e+27, 'cm^3/(mol*s)'),
        n = -4.333,
        Ea = (3685.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (1.300e+22, 'cm^3/(mol*s)'),
        n = -2.664,
        Ea = (2451.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# LB Harding, SJ Klippenstein, Y Georgievskii, PCI 30:985 (2005).
# DH = -68.5

entry(
    index = 109,
    label = "CH3 + OH <=> H2 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.890e+09, 'cm^3/(mol*s)'),
        n = 0.254,
        Ea = (-1221.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (1.990e+10, 'cm^3/(mol*s)'),
        n = 0.06,
        Ea = (-624.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (2.810e+11, 'cm^3/(mol*s)'),
        n = -0.25,
        Ea = (498.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (3.550e+12, 'cm^3/(mol*s)'),
        n = -0.532,
        Ea = (2042.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (2.190e+12, 'cm^3/(mol*s)'),
        n = -0.432,
        Ea = (3415.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (2.360e+09, 'cm^3/(mol*s)'),
        n = 0.453,
        Ea = (3791.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# k_inf                6.20E+13      -0.018         -33
# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# DH = -90.3
# ## Missing collider efficiencies

entry(
    index = 110,
    label = "CH3 + OH <=> H2 + CHOH",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.210e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (-2322.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (6.400e+09, 'cm^3/(mol*s)'),
        n = 0.633,
        Ea = (-1701.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (8.000e+10, 'cm^3/(mol*s)'),
        n = 0.34,
        Ea = (-565.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (6.530e+11, 'cm^3/(mol*s)'),
        n = 0.112,
        Ea = (932.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (2.060e+11, 'cm^3/(mol*s)'),
        n = 0.295,
        Ea = (2200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (9.400e+07, 'cm^3/(mol*s)'),
        n = 1.286,
        Ea = (2424.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# DH = -70.1

entry(
    index = 111,
    label = "CH3 + OH <=> CH2 + H2O",
    kinetics = Arrhenius(
        A = (4.300e+04, 'cm^3/(mol*s)'),
        n = 2.568,
        Ea = (3997.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# High P limit for H2+HCOH: 4.523e4 2.27 8196 (cis) 2.460e3 2.621 8896 (trans)
# DH = -18.0
entry(
    index = 112,
    label = "CH4 + O <=> CH3 + OH",
    kinetics = Arrhenius(
        A = (4.400e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (6577.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
#  AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# DH = -8.5
entry(
    index = 113,
    label = "CH3 + HO2 <=> CH4 + O2",
    kinetics = Arrhenius(
        A = (1.190e+05, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3022.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 1.7
entry(
    index = 114,
    label = "CH3 + HO2 <=> CH3O + OH",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.269,
        Ea = (-688.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NK Srinivasan, JV Michael, LB Harding, SJ Klippenstein, CF 149:104 (2007).
# DH = -55.3
entry(
    index = 115,
    label = "CH3CHO <=> CH3 + HCO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.72e+22, 's^-1'), n=-1.74, Ea=(86355.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+59, 'cm^3/(mol*s)'), n=-11.3, Ea=(95912.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.183,
        T3 = (462.0, 'K'),
        T1 = (167730.0, 'K'),
        T2 = (1580000.0, 'K'),
        efficiencies = { '[H][H]': 2.86, 'O': 8.57, 'C': 4.23, '[C-]#[O+]': 2.14, 'O=C=O': 2.86, 'CC': 4.23, 'N#N': 1.43, '[He]': 1.0, '[Ar]': 1.0 }
    ),
)

entry(
    index = 116,
    label = "CH3 + HCO <=> CH4 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.1, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.920e+18, 'cm^3/(mol*s)'),
        n = -1.84,
        Ea = (2134.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (8.740e+18, 'cm^3/(mol*s)'),
        n = -1.97,
        Ea = (2684.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.850e+20, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (4781.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.130e+21, 'cm^3/(mol*s)'),
        n = -2.45,
        Ea = (7417.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# R Sivaramakrishnan, JV Michael, SJ Klippenstein, JPCA 114:755 (2010).
# Fc refit to chemkin form
# DH = 82.6

entry(
    index = 117,
    label = "CH3OCHO <=> CH3 + OCOH",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(187000.0, 's^-1'), n=2.433, Ea=(70850.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.84e+34, 'cm^3/(mol*s)'), n=-5.267, Ea=(70796.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.159,
        T3 = (1646.9, 'K'),
        T1 = (1647.4, 'K'),
        T2 = (138988.0, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 118,
    label = "CH3OCHO <=> CH3 + H + CO2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.35e+22, 's^-1'), n=-1.509, Ea=(91520.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.5e+41, 'cm^3/(mol*s)'), n=-6.472, Ea=(93044.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.683,
        T3 = (19999.9, 'K'),
        T1 = (71.4, 'K'),
        T2 = (726.1, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 119,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.88e+16, 'cm^3/(mol*s)'), n=-1.16, Ea=(774.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(3.74e+50, 'cm^6/(mol^2*s)'), n=-9.93, Ea=(7389.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.7548,
        T3 = (32828.0, 'K'),
        T1 = (158.0, 'K'),
        T2 = (46564.0, 'K'),
        efficiencies = { '[H][H]': 2.0, '[C-]#[O+]': 2.0, 'O=C=O': 3.0, 'O': 5.0 }
    ),
)

entry(
    index = 120,
    label = "H + O2 + CH3 <=> CH4 + O2",
    kinetics = Arrhenius(
        A = (2.160e+22, 'cm^6/(mol^2*s)'),
        n = -1.73,
        Ea = (536.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JH Kiefer, S Santhanam, NK Srinivasan, RS Tranter, SJ Klippenstein, M Oehlschlaeger, PCI 30:1129 (2005).
# XL Yang, AW Jasper, JH Kiefer, RS Tranter, JPCA 113, 8318 (2009).
# The newer paper has lower-T (1200-1500 K) experimental data than the older paper (1500+ K).
# The ME parameters (alpha) obtained in the first study were re-optimized in the 2nd study to fit data from both papers.
# DH = -88.1
# *** Chemically Termolecular
entry(
    index = 121,
    label = "CH2 + O2 <=> CO2 + H + H",
    kinetics = Arrhenius(
        A = (5.130e+08, 'cm^3/(mol*s)'),
        n = 0.993,
        Ea = (-269.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# MP Burke, SJ Klippenstein, estimate
# DH = -103.3
# *****************************************************************************
#    CH2 subset                                                               *
#    includes C                                                               *
# *****************************************************************************
# Fuel Radicals: CH
# New Radicals Formed: C, C2H3, C2H
# New Fuels: C2H4, CH2CO, C2H2
# *** Fuel Decomposition
# *** Fuel + Radical
entry(
    index = 122,
    label = "CH2 + O2 <=> CO2 + H2",
    kinetics = Arrhenius(
        A = (5.130e+08, 'cm^3/(mol*s)'),
        n = 0.993,
        Ea = (-269.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimated products; 2015.
# DH = -84.1
# ???
entry(
    index = 123,
    label = "CH2 + O2 <=> CO + H + OH",
    kinetics = Arrhenius(
        A = (5.130e+08, 'cm^3/(mol*s)'),
        n = 0.993,
        Ea = (-269.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimated products; 2015.
# DH = -187.4
# need to update ??
entry(
    index = 124,
    label = "CH2 + O2 <=> HCO + OH",
    kinetics = Arrhenius(
        A = (5.130e+08, 'cm^3/(mol*s)'),
        n = 0.993,
        Ea = (-269.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimated products; 2015.
# DH = -59.9
# need to update ??
entry(
    index = 125,
    label = "CH2 + O2 <=> CH2O + O",
    kinetics = Arrhenius(
        A = (2.150e+09, 'cm^3/(mol*s)'),
        n = 1.08,
        Ea = (1196.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimated products; 2015.
# DH = -74.6
# need to update ??
entry(
    index = 126,
    label = "CH2 + H <=> CH + H2",
    kinetics = Arrhenius(
        A = (1.200e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimated products.
# SJ Klippenstein - unpublished calculations.
# DH = -59.5
# need to update ??
entry(
    index = 127,
    label = "CH2 + O <=> CO + H + H",
    kinetics = Arrhenius(
        A = (1.230e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (537.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -3.4
entry(
    index = 128,
    label = "CH2 + O <=> CO + H2",
    kinetics = Arrhenius(
        A = (8.190e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (537.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -76.4
entry(
    index = 129,
    label = "CH2 + OH <=> CH2O + H",
    kinetics = Arrhenius(
        A = (2.860e+13, 'cm^3/(mol*s)'),
        n = 0.123,
        Ea = (-162.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -179.7
entry(
    index = 130,
    label = "CH2 + OH <=> CH + H2O",
    kinetics = Arrhenius(
        A = (8.630e+05, 'cm^3/(mol*s)'),
        n = 2.019,
        Ea = (6776.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, JPCA 111:8699 (2007).
# capture rate
# DH = -76.0
entry(
    index = 131,
    label = "CH2 + CH3 <=> C2H4 + H",
    kinetics = Arrhenius(
        A = (1.200e+15, 'cm^3/(mol*s)'),
        n = -0.343,
        Ea = (153.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, JPCA 111:8699 (2007).
# abstraction to 4CH + H2O
# DH = -17.8
entry(
    index = 132,
    label = "CH2 + CH2 <=> C2H2 + H + H",
    kinetics = Arrhenius(
        A = (7.090e+13, 'cm^3/(mol*s)'),
        n = 0.002,
        Ea = (9.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, JPCA 111:8699 (2007).
# capture rate
# DH = -63.2
entry(
    index = 133,
    label = "CH2 + CH2 <=> C2H2 + H2",
    kinetics = Arrhenius(
        A = (1.770e+13, 'cm^3/(mol*s)'),
        n = 0.002,
        Ea = (9.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, JPCA 111:8699 (2007).
# assume 80% C2H2+H+H products
# DH = -63.3
entry(
    index = 134,
    label = "CH3 + H <=> CH2 + H2",
    kinetics = Arrhenius(
        A = (1.220e+06, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (11941.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, JPCA 111:8699 (2007).
# assume 20% C2H2+H2 products                   {2010}
# DH = -132.4
# *** Fuel + Stable
entry(
    index = 135,
    label = "CH2 + CO <=> CH2CO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(810000000000.0, 'cm^3/(mol*s)'), n=0.5, Ea=(4510.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.88e+33, 'cm^6/(mol^2*s)'), n=-5.11, Ea=(7095.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5907,
        T3 = (275.0, 'K'),
        T1 = (1226.0, 'K'),
        T2 = (5185.0, 'K'),
        efficiencies = { '[H][H]': 2.0, '[C-]#[O+]': 2.0, 'O=C=O': 3.0, 'O': 8.58, 'N#N': 1.43 }
    ),
)

entry(
    index = 136,
    label = "CH2 + CO2 <=> CH2O + CO",
    kinetics = Arrhenius(
        A = (2.350e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## LASKIN ET AL. IJCK 32 589-614 2000
# GRIMech, 2.11
# DH = -77.1
entry(
    index = 137,
    label = "CH2 + CH4 <=> CH3 + CH3",
    kinetics = Arrhenius(
        A = (4.300e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (10030.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -51.8
entry(
    index = 138,
    label = "CH + H2O <=> CH2O + H",
    kinetics = Arrhenius(
        A = (8.480e+08, 'cm^3/(mol*s)'),
        n = 1.144,
        Ea = (-2051.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# T Bohland, S Dobe, F Temps, HGg Wagner, BBPC 89:1110 (1985).
# DH = -5.8
# CH2+CH3OH=CH3+CH3O
# $$ Missing Reaction
# DH = ??
# CH2+CH3OH=CH3+CH2OH
# $$ Missing Reaction
# DH = ??
# *** Fuel Radical + Stable
entry(
    index = 139,
    label = "CH + CO <=> HCCO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1050000000000000.0, 'cm^3/(mol*s)'), n=-0.4, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.29e+24, 'cm^6/(mol^2*s)'), n=-2.5, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.4,
        T3 = (1000000.0, 'K'),
        T1 = (1e-06, 'K'),
        efficiencies = { 'O': 10.0, 'O=C=O': 3.0, '[H][H]': 2.0, '[C-]#[O+]': 2.0 }
    ),
)

entry(
    index = 140,
    label = "CH + CO2 <=> HCO + CO",
    kinetics = Arrhenius(
        A = (8.800e+06, 'cm^3/(mol*s)'),
        n = 1.75,
        Ea = (-1040.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -72.2
entry(
    index = 141,
    label = "CH + CH2O <=> CH2CO + H",
    kinetics = Arrhenius(
        A = (4.590e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-767.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Glarborg, LLB Bentzen, EF 22: 291 (2008).
# DH = -65.1
entry(
    index = 142,
    label = "CH + CH4 <=> C2H4 + H",
    kinetics = Arrhenius(
        A = (1.330e+16, 'cm^3/(mol*s)'),
        n = -0.94,
        Ea = (58.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# HMT Nguyen, HT Nguyen, TN Nguyen, HV Hoang, L Vereecken, JPCA 118:8861 (2014).
# DH = -75.6
entry(
    index = 143,
    label = "CH + O2 <=> CO2 + H",
    kinetics = Arrhenius(
        A = (2.530e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -59.7
# CH+CH2CO=C2H3+CO
# Missing Reaction
# *** Fuel Radical + Radical
entry(
    index = 144,
    label = "CH + O2 <=> CO + H + O",
    kinetics = Arrhenius(
        A = (2.530e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -184.0
entry(
    index = 145,
    label = "CH + O2 <=> CO + OH",
    kinetics = Arrhenius(
        A = (1.690e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -58.2
entry(
    index = 146,
    label = "CH + O2 <=> HCO + O",
    kinetics = Arrhenius(
        A = (1.690e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## KATHROTIA ET AL. COMB & FLAME 2010
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -159.9
entry(
    index = 147,
    label = "CH + H <=> C + H2",
    kinetics = Arrhenius(
        A = (1.200e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -72.9
entry(
    index = 148,
    label = "CH + O <=> CO + H",
    kinetics = Arrhenius(
        A = (3.980e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -23.4
entry(
    index = 149,
    label = "CH + OH <=> HCO + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -176.3
entry(
    index = 150,
    label = "CH + OH <=> C + H2O",
    kinetics = Arrhenius(
        A = (4.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (3000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, P Glarborg, estimate.
# DH = -89.3
entry(
    index = 151,
    label = "CH + CH3 <=> C2H3 + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, estimate.
# DH = -37.9
entry(
    index = 152,
    label = "CH + CH2 <=> C2H2 + H",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, P Glarborg, estimate.
# DH = -54.0
entry(
    index = 153,
    label = "C + O2 <=> CO + O",
    kinetics = Arrhenius(
        A = (6.630e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (636.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, P Glarborg, estimate.
# DH = -129.0
# *** C Atom Reactions
entry(
    index = 154,
    label = "C + OH <=> CO + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -138.2
entry(
    index = 155,
    label = "C + CH3 <=> C2H2 + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, Thorne, estimate.
# DH = -154.6
entry(
    index = 156,
    label = "C + CH2 <=> C2H + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, P Glarborg, estimate.
# DH = -99.7
entry(
    index = 157,
    label = "CH2(S) <=> CH2",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = {'O': 0.0, 'C#C': 0.0, 'c1ccccc1': 0.0, 'N#N': 0.0, '[Ar]': 0.0, '[O][O]': 0.0 },
    ),
    
)

# JA Miller, P Glarborg, estimate.
# DH = - 77.3
# *****************************************************************************
#    CH2(S) subset                                                            *
# *****************************************************************************
# Fuel Radicals: None
# New Radicals Formed: HCCO, CH2CCH
# New Fuels: C2H2, (CHCOH)
# *** Fuel Decomposition
entry(
    index = 158,
    label = "CH2(S) + H <=> CH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -9.1
entry(
    index = 159,
    label = "CH2(S) + N2 <=> CH2 + N2",
    kinetics = Arrhenius(
        A = (1.260e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (430.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -9.1
entry(
    index = 160,
    label = "CH2(S) + AR <=> CH2 + AR",
    kinetics = Arrhenius(
        A = (1.450e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (884.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# F Hayes, WD Lawrance, WS Staker, KD King,  JPC 100:11314 (1996).
# DH = -9.1
entry(
    index = 161,
    label = "CH2(S) + O2 <=> CH2 + O2",
    kinetics = Arrhenius(
        A = (4.500e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# F Hayes, WD Lawrance, WS Staker, KD King,  JPC 100:11314 (1996).
# DH = -9.1
entry(
    index = 162,
    label = "CH2(S) + H2O <=> CH2 + H2O",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AO Langford, H Petek, CB Moore, JCP, 78:6650 (1983). for the rate
# MA Blitz, KW McKee, MJ Pilling, PW Seakins, CPL, 372:295 (2003). for products
# DH = -9.1
entry(
    index = 163,
    label = "CH2(S) + C2H4 <=> CH2 + C2H4",
    kinetics = Arrhenius(
        A = (1.130e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-556.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Hack, HGg Wagner, A Wilms,  BBPC 92:620 (1988); HH Carstensen, HGg Wagner, BBPC 99:1539 (1995).
# DH = -9.1
entry(
    index = 164,
    label = "CH2(S) + C2H2 <=> CH2 + C2H2",
    kinetics = Arrhenius(
        A = (8.550e+14, 'cm^3/(mol*s)'),
        n = -0.624,
        Ea = (-231.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -9.1
entry(
    index = 165,
    label = "CH2(S) + C6H6 <=> CH2 + C6H6",
    kinetics = Arrhenius(
        A = (7.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -9.1
entry(
    index = 166,
    label = "CH2(S) + H2 <=> CH3 + H",
    kinetics = Arrhenius(
        A = (2.060e+13, 'cm^3/(mol*s)'),
        n = 0.096,
        Ea = (-415.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Hack, M Koch, HGg Wagner, A Wilms,  BBPC 92:674 (1988)
# DH = -9.1
# *** Fuel + Stable
entry(
    index = 167,
    label = "CH3OH <=> CH2(S) + H2O",
    kinetics = PDepArrhenius(
        pressures = ([1.3e-05, 0.000132, 0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0, 1320.0, 13200.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.330e+42, 's^-1'),
        n = -9.885,
        Ea = (107109.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.3e-05 atm
        Arrhenius(
            A = (1.490e+44, 's^-1'),
        n = -10.146,
        Ea = (104274.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000132 atm
        Arrhenius(
            A = (1.120e+47, 's^-1'),
        n = -10.61,
        Ea = (103386.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (5.330e+48, 's^-1'),
        n = -10.777,
        Ea = (103702.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (2.020e+49, 's^-1'),
        n = -10.687,
        Ea = (104280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (8.680e+48, 's^-1'),
        n = -10.357,
        Ea = (104953.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (1.080e+47, 's^-1'),
        n = -9.6,
        Ea = (105252.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (3.950e+42, 's^-1'),
        n = -8.144,
        Ea = (104167.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        Arrhenius(
            A = (1.320e+35, 's^-1'),
        n = -5.876,
        Ea = (100854.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1320.0 atm
        Arrhenius(
            A = (2.090e+26, 's^-1'),
        n = -3.297,
        Ea = (96056.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13200.0 atm
        ],
    ),
)

# KL Gannon, MA Blitz, MJ Pilling, PW Seakins, SJ Klippenstein, LB Harding JPCA 112:9575 (2008).
# DH = 15.1

entry(
    index = 168,
    label = "CH3 + OH <=> CH2(S) + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.130e+14, 'cm^3/(mol*s)'),
        n = -0.458,
        Ea = (-496.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (2.230e+14, 'cm^3/(mol*s)'),
        n = -0.538,
        Ea = (-220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (1.160e+15, 'cm^3/(mol*s)'),
        n = -0.727,
        Ea = (600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (4.280e+15, 'cm^3/(mol*s)'),
        n = -0.86,
        Ea = (1887.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (4.380e+14, 'cm^3/(mol*s)'),
        n = -0.539,
        Ea = (2932.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (6.090e+10, 'cm^3/(mol*s)'),
        n = 0.596,
        Ea = (2923.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# DH = 90.9

entry(
    index = 169,
    label = "HCCO + H <=> CH2(S) + CO",
    kinetics = Arrhenius(
        A = (1.220e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# reverse k fit to two arr. expressions: 8.407e9   0.8750 1428   3.915e19 -2.182   325.1
# DH = 0.5
entry(
    index = 170,
    label = "CH2(S) + CO2 <=> CH2O + CO",
    kinetics = Arrhenius(
        A = (1.100e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -18.7
entry(
    index = 171,
    label = "CH2(S) + CH4 <=> CH3 + CH3",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# M Koch, F Temps, R Wagener, HGg Wagner, BBPC 94:645 (1990).
# DH = -18.7
entry(
    index = 172,
    label = "CH2(S) + H <=> CH + H2",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# $$ Baulch (2005).
# DH = -14.9
# CH2(S)+CH3OH=CH3+CH3O
# $$ Missing Reaction
# DH = ??
# CH2(S)+CH3OH=CH3+CH2OH
# $$ Missing Reaction
# DH = ??
# *** Fuel + Radical
entry(
    index = 173,
    label = "CH2(S) + O <=> CO + H + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -12.4
entry(
    index = 174,
    label = "CH2(S) + OH <=> CH2O + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -85.6
entry(
    index = 175,
    label = "CH2(S) + CH3 <=> C2H4 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -85.2
entry(
    index = 176,
    label = "CH2(S) + CH2(S) <=> C2H2 + H + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -72.4
entry(
    index = 177,
    label = "CH3OH + H <=> CH2OH + H2",
    kinetics = Arrhenius(
        A = (6.560e+04, 'cm^3/(mol*s)'),
        n = 2.728,
        Ea = (4451.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -47.3
# *****************************************************************************
#    CH3OH subset                                                             *
# *****************************************************************************
# Fuel Radicals: CH2OH, CH3O
# New Radicals Formed:
# New Fuels: CH3OOH
# *** Fuel Decomposition
# *** Fuel + Radical
entry(
    index = 178,
    label = "CH3OH + O <=> CH2OH + OH",
    kinetics = Arrhenius(
        A = (2.470e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5305.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JI Moses, C Visscher, JJ Fortney, AP Showman, NK Lewis, et al., APJ 737:15 (2011).
# DH = -8.7
entry(
    index = 179,
    label = "CH3OH + OH <=> CH2OH + H2O",
    kinetics = Arrhenius(
        A = (1.500e+08, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (113.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
#  DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
#  DH = -7.1
# CH3OH+O=CH3O+OH
#  ## Missing
#  $$ Missing
#  DH = ??
entry(
    index = 180,
    label = "CH3OH + OH <=> CH3O + H2O",
    kinetics = Arrhenius(
        A = (2.780e+07, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (113.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NK Srinivasan, MC Su, JV Michael, JPCA 111:3951 (2007); branching 0.85
# There is a lot more known about this reaction in recent literature - SJK
# DH = -23.2
entry(
    index = 181,
    label = "CH3OH + CH3 <=> CH2OH + CH4",
    kinetics = Arrhenius(
        A = (7.360e-01, 'cm^3/(mol*s)'),
        n = 3.781,
        Ea = (7183.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NK Srinivasan, MC Su, JV Michael, JPCA 111:3951 (2007); branching = 0.15
# There is a lot more known about this reaction in recent literature - SJK
# ??
# DH = -13.6
entry(
    index = 182,
    label = "CH3OH + CH3O <=> CH3OH + CH2OH",
    kinetics = Arrhenius(
        A = (3.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (40600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# IM Alecu, DG Truhlar, JPCA 115:14599 (2011).
# DH = -8.8
entry(
    index = 183,
    label = "CH3OH + HO2 <=> CH2OH + H2O2",
    kinetics = Arrhenius(
        A = (2.280e-05, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (10213.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 16:471 (1987).
# DH = -9.6
# *** Fuel Radical + Stable
entry(
    index = 184,
    label = "CH3OH + HCO <=> CH2OH + CH2O",
    kinetics = Arrhenius(
        A = (9.640e+03, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (13100.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## Needs to be updated to ~1/3 this value
# SJ Klippenstein, LB Harding, MJ Davis, AS Tomlin, RT Skodje, PCI 33:351 (2011).
# DH = ??
entry(
    index = 185,
    label = "CH3O + CH2O <=> CH3OH + HCO",
    kinetics = Arrhenius(
        A = (6.600e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2285.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 16:471 (1987).
# DH = ??
entry(
    index = 186,
    label = "CH3OH + H <=> CH3O + H2",
    kinetics = Arrhenius(
        A = (4.110e+04, 'cm^3/(mol*s)'),
        n = 2.658,
        Ea = (9226.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# C Fittschen, B Delcroix, N Gomez, P Devolder,  JChimP 95:2129 (1998).
# DH = ??
entry(
    index = 187,
    label = "CH3OH + HO2 <=> CH3O + H2O2",
    kinetics = Arrhenius(
        A = (3.340e-02, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (16234.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JI Moses, C Visscher, JJ Fortney, AP Showman, NK Lewis, et al., APJ 737:15 (2011).
# DH = 0.9
entry(
    index = 188,
    label = "CH3OCO <=> CH3O + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 5.0, 20.0, 50.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.240e+10, 's^-1'),
        n = -1.168,
        Ea = (29865.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.310e+02, 's^-1'),
        n = 1.406,
        Ea = (24454.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.740e+05, 's^-1'),
        n = 0.789,
        Ea = (21991.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.740e+11, 's^-1'),
        n = -0.759,
        Ea = (21410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 5.0 atm
        Arrhenius(
            A = (2.000e+16, 's^-1'),
        n = -1.949,
        Ea = (21757.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 20.0 atm
        Arrhenius(
            A = (2.120e+20, 's^-1'),
        n = -2.966,
        Ea = (22820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 50.0 atm
        Arrhenius(
            A = (3.280e+22, 's^-1'),
        n = -3.466,
        Ea = (23613.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# ## Needs to be updated to ~1/3 this value
# SJ Klippenstein, LB Harding, MJ Davis, AS Tomlin, RT Skodje, PCI 33:351 (2011).
# DH = 18.1

entry(
    index = 189,
    label = "CH3OH + CH3 <=> CH3O + CH4",
    kinetics = Arrhenius(
        A = (2.840e+03, 'cm^3/(mol*s)'),
        n = 2.439,
        Ea = (8541.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished calculations, fit by R Sivaramakrishnan, NJ Labbe
# DH = 16.0
# CH3O+CO=CH3+CO2
# $$ Missing Reaction
# Lissi E, Massiff G, Villa A. Oxidation of carbon monoxide by methoxy-radicals. J Chem Soc, Faraday Trans I. 1973;69:346-51
# Hidaka Y, Sato K, Yamane M. High-temperature pyrolysis of dimethyl ether in shock waves. Combust Flame. 2000;123:1-22.
entry(
    index = 190,
    label = "CH2OH + O2 <=> CH2O + HO2",
    kinetics = Arrhenius(
        A = (8.130e+09, 'cm^3/(mol*s)'),
        n = 0.89,
        Ea = (-866.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# IM Alecu, DG Truhlar, JPCA 115:14599 (2011).
# DH = 0.8
# *** Fuel Radical + Radical
entry(
    index = 191,
    label = "CH2OH + H <=> CH2O + H2",
    kinetics = Arrhenius(
        A = (4.000e+06, 'cm^3/(mol*s)'),
        n = 1.86,
        Ea = (147.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Shocker, M Uetake, N Kanno, M Koshi, K Tonokura, JPCA 111:6622 (2007).
# Fit by R Sivaramakrishnan
# Used the low temperature (250-550 K) rate constants determined
# In the high temperature range (550-2500 K), the rate constant of the HCO+O2=CO+HO2 reaction (Hsu and Mebel)
# were scaled by a factor of 1.3 (this factor was chosen to have continuity between the two sets at 550 K). Finally, a non-Ahrenius fitting was performed.
# DH = -19.1
entry(
    index = 192,
    label = "CH3 + OH <=> H + CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.440e+09, 'cm^3/(mol*s)'),
        n = 0.963,
        Ea = (3230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (8.440e+09, 'cm^3/(mol*s)'),
        n = 0.963,
        Ea = (3230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (1.010e+10, 'cm^3/(mol*s)'),
        n = 0.942,
        Ea = (3295.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (5.600e+10, 'cm^3/(mol*s)'),
        n = 0.74,
        Ea = (3971.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (5.530e+11, 'cm^3/(mol*s)'),
        n = 0.486,
        Ea = (5443.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (2.520e+10, 'cm^3/(mol*s)'),
        n = 0.909,
        Ea = (6402.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# K Xu, ZF Xu, MC Lin, Mol Phys 105:2763 (2007).
# DH = -74.4

entry(
    index = 193,
    label = "CH2OH + O <=> CH2O + OH",
    kinetics = Arrhenius(
        A = (6.600e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-693.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# DH = 4.3
# CH2OH+H(+M)=CH3OH(+M)
# Missing Reaction - FFCM; 128
# $$
# DH = ??
# CH2OH+H=CH2(S)+H2O
# Missing Reaction - FFCM; 131
# $$
# DH = ??
entry(
    index = 194,
    label = "CH2OH + OH <=> H2O + CH2O",
    kinetics = Arrhenius(
        A = (2.400e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Seetula, IJ Kalinovski, IR Slagle, D Gutman, CPL 224:533 (1994).
# DH = -72.8
entry(
    index = 195,
    label = "CH2OH + HO2 <=> CH2O + H2O2",
    kinetics = Arrhenius(
        A = (1.810e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 16:471 (1987).
# DH = -88.9
entry(
    index = 196,
    label = "CH3OH + O2 <=> CH2OH + HO2",
    kinetics = Arrhenius(
        A = (3.580e+05, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42760.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH= -30.9
entry(
    index = 197,
    label = "CH2OH + HCO <=> CH3OH + CO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, LB Harding, MJ Davis, AS Tomlin, RT Skodje, PCI 33:351 (2011).
# DH = 46.6
entry(
    index = 198,
    label = "CH2OH + HCO <=> CH2O + CH2O",
    kinetics = Arrhenius(
        A = (1.500e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang JPCRD 16:471 (1987).
# G Friedrichs, JT Herbon, DF Davidson, RK Hanson, IJCK 36:157 (2004).
# DH = ??
entry(
    index = 199,
    label = "CH3CH2OH <=> CH3 + CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.180e+59, 's^-1'),
        n = -13.98,
        Ea = (99906.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.620e+66, 's^-1'),
        n = -15.3,
        Ea = (105390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.550e+64, 's^-1'),
        n = -14.47,
        Ea = (107099.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.550e+58, 's^-1'),
        n = -12.29,
        Ea = (105768.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.780e+47, 's^-1'),
        n = -8.96,
        Ea = (101059.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# W Tsang JPCRD 16:471 (1987).
# G Friedrichs, JT Herbon, DF Davidson, RK Hanson, IJCK 36:157 (2004).
# DH = ??
# CH3OH+O2=CH3O+HO2				            1.40E11     0.000       0
# SH Mousaviour, Z Homayoon, JPCA 115:3291 (2011).
# DH = ??

entry(
    index = 200,
    label = "CH3 + CH2OH <=> C2H4 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.320e+24, 'cm^3/(mol*s)'),
        n = -3.713,
        Ea = (2798.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.160e+25, 'cm^3/(mol*s)'),
        n = -3.787,
        Ea = (3001.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.230e+27, 'cm^3/(mol*s)'),
        n = -4.45,
        Ea = (5345.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.250e+29, 'cm^3/(mol*s)'),
        n = -5.034,
        Ea = (9245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.710e+27, 'cm^3/(mol*s)'),
        n = -4.184,
        Ea = (11152.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.930e+17, 'cm^3/(mol*s)'),
        n = -1.369,
        Ea = (8978.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# DH = 85.3

entry(
    index = 201,
    label = "CH2OH + CH3 <=> CH2O + CH4",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# DH = -76.0
entry(
    index = 202,
    label = "CH2CH2OH + H <=> CH3 + CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.490e+17, 'cm^3/(mol*s)'),
        n = -0.903,
        Ea = (3023.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.930e+17, 'cm^3/(mol*s)'),
        n = -0.935,
        Ea = (3120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.540e+18, 'cm^3/(mol*s)'),
        n = -1.243,
        Ea = (4062.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.930e+22, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (7692.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.790e+25, 'cm^3/(mol*s)'),
        n = -3.1,
        Ea = (12454.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.470e+20, 'cm^3/(mol*s)'),
        n = -1.693,
        Ea = (13429.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# T Koike, M Kudo, I Madea, H Yamada, IJCK 32:1 (2000); estimate.
# DH = -74.5

entry(
    index = 203,
    label = "CH2OH + CH2 <=> CH2O + CH3",
    kinetics = Arrhenius(
        A = (1.210e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = 9.0
entry(
    index = 204,
    label = "CH2OH + CH2OH <=> CH3OH + CH2O",
    kinetics = Arrhenius(
        A = (9.040e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 16:471 (1987).
# DH = -80.4
entry(
    index = 205,
    label = "CH3O + O2 <=> CH2O + HO2",
    kinetics = Arrhenius(
        A = (4.800e-01, 'cm^3/(mol*s)'),
        n = 3.567,
        Ea = (-1055.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -65.7
entry(
    index = 206,
    label = "CH3O + H <=> CH2O + H2",
    kinetics = Arrhenius(
        A = (7.600e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-519.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# V Aranda, JM Christensen, MU Alzueta, AD Jensen, P Glarborg, S Gersen, Y Gao, P Marshall, IJCK 45:283 (2013).
# DH = -28.6
entry(
    index = 207,
    label = "CH3 + OH <=> H + CH3O",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0132, 0.132, 1.32, 13.2, 132.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.890e+08, 'cm^3/(mol*s)'),
        n = 1.065,
        Ea = (11858.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (7.890e+08, 'cm^3/(mol*s)'),
        n = 1.065,
        Ea = (11858.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0132 atm
        Arrhenius(
            A = (7.890e+08, 'cm^3/(mol*s)'),
        n = 1.065,
        Ea = (11858.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm
        Arrhenius(
            A = (7.930e+08, 'cm^3/(mol*s)'),
        n = 1.065,
        Ea = (11859.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.32 atm
        Arrhenius(
            A = (1.030e+09, 'cm^3/(mol*s)'),
        n = 1.034,
        Ea = (11970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 13.2 atm
        Arrhenius(
            A = (3.070e+09, 'cm^3/(mol*s)'),
        n = 0.922,
        Ea = (12980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 132.0 atm
        ],
    ),
)

# K Xu, ZF Xu, MC Lin, MP 105:2763 (2007).
# DH = -84.0
# CH3O+H(+M)=CH3OH(+M)
# Missing Reaction - FFCM; 117
# $$
# DH = ??
# CH3O+H=CH2(S)+H2O
# Missing Reaction - FFCM; 121
# $$
# DH = ??

entry(
    index = 208,
    label = "CH3 + O2 <=> CH3O + O",
    kinetics = Arrhenius(
        A = (7.550e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (28297.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AW Jasper, SJ Klippenstein, LB Harding, B Ruscic, JPCA 111:3932 (2007).
# DH = 13.8
entry(
    index = 209,
    label = "CH3O + O <=> CH2O + OH",
    kinetics = Arrhenius(
        A = (6.020e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NK Srinivasan, MC Su, JW Sutherland, JV Michael, JPCA 109:7902 (2005).
# DH = 30.4
entry(
    index = 210,
    label = "CH3OOH <=> CH3O + OH",
    kinetics = Arrhenius(
        A = (6.300e+14, 's^-1'),
        n = 0.0,
        Ea = (42300.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# $$ Baulch (2005).
# DH = -82.3
entry(
    index = 211,
    label = "CH3O + OH <=> CH2O + H2O",
    kinetics = Arrhenius(
        A = (1.810e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# PD Lightfoot, P Roussel, F Caralp, R Lesclaux, JCSFT 87:3213 (1991).
# DH = 43.5
entry(
    index = 212,
    label = "CH3O + HO2 <=> CH2O + H2O2",
    kinetics = Arrhenius(
        A = (3.010e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -98.4
entry(
    index = 213,
    label = "CH3OCHO <=> CH3O + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.040e+27, 's^-1'),
        n = -4.723,
        Ea = (104329.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.260e+38, 's^-1'),
        n = -7.66,
        Ea = (105519.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (6.320e+41, 's^-1'),
        n = -8.361,
        Ea = (106245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.070e+43, 's^-1'),
        n = -8.551,
        Ea = (106683.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 2.0 atm
        Arrhenius(
            A = (9.070e+42, 's^-1'),
        n = -8.314,
        Ea = (106983.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 5.0 atm
        Arrhenius(
            A = (6.310e+41, 's^-1'),
        n = -7.827,
        Ea = (106901.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (9.340e+39, 's^-1'),
        n = -7.16,
        Ea = (106574.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 20.0 atm
        Arrhenius(
            A = (4.790e+34, 's^-1'),
        n = -5.371,
        Ea = (105300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -66.8

entry(
    index = 214,
    label = "CH3O + HCO <=> CH3OH + CO",
    kinetics = Arrhenius(
        A = (9.040e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished calculations, fit by R Sivaramakrishnan, NJ Labbe
# DH = 99.3
entry(
    index = 215,
    label = "H + CH2OCHO <=> CH3O + HCO",
    kinetics = Arrhenius(
        A = (2.410e+12, 'cm^3/(mol*s)'),
        n = 0.477,
        Ea = (2005.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## Friedrichs, G.; Davidson, D. F.; Hanson, R. K. Int J. Chem. Kinet. 2004, 36, 157.
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -115.6
entry(
    index = 216,
    label = "CH3O + CH3 <=> CH2O + CH4",
    kinetics = Arrhenius(
        A = (2.410e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = 0.9
entry(
    index = 217,
    label = "CH3O + CH2 <=> CH2O + CH3",
    kinetics = Arrhenius(
        A = (1.810e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -84.1
entry(
    index = 218,
    label = "CH2OH + CH3O <=> CH3OH + CH2O",
    kinetics = Arrhenius(
        A = (2.400e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -89.9
entry(
    index = 219,
    label = "CH3O + CH3O <=> CH3OH + CH2O",
    kinetics = Arrhenius(
        A = (6.020e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## NORTON, T.S ET AL., IJCK. (1991).
# W Tsang, JPCRD 16:471 (1987).
# DH = -75.2
entry(
    index = 220,
    label = "CH3OOH + H <=> CH3OO + H2",
    kinetics = Arrhenius(
        A = (8.800e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1860.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -84.8
# *****************************************************************************
#    CH3OOH subset                                                            *
# *****************************************************************************
# Fuel Radicals: CH3OO
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition
# Included in CH3OH mechanism
# *** Fuel + Radical
entry(
    index = 221,
    label = "CH3OOH + H <=> CH3O + H2O",
    kinetics = Arrhenius(
        A = (8.200e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1860.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# F Slemr, P Warneck, IJCK 9:267 (1977).
# DH = -18.8
entry(
    index = 222,
    label = "CH3OOH + O <=> CH3OO + OH",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (3000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# F Slemr, P Warneck, IJCK 9:267 (1977).
# DH = -74.3
entry(
    index = 223,
    label = "CH3OOH + O <=> CH2O + OH + OH",
    kinetics = Arrhenius(
        A = (2.470e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4888.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# GL Vaghjiani, AR Ravishankara, IJCK 22:351 (1990).
# DH = -17.2
entry(
    index = 224,
    label = "CH3OOH + OH <=> CH3OO + H2O",
    kinetics = Arrhenius(
        A = (1.080e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-437.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# Set CH2OOH = CH2O+OH
# DH = -38.9
entry(
    index = 225,
    label = "CH3OOH + OH <=> CH2O + OH + H2O",
    kinetics = Arrhenius(
        A = (7.230e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-258.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -33.3
entry(
    index = 226,
    label = "CH3OO + H2O2 <=> CH3OOH + HO2",
    kinetics = Arrhenius(
        A = (2.400e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (9940.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# Set CH2OOH = CH2O+OH
# DH = -54.9
entry(
    index = 227,
    label = "CH3OO + CH4 <=> CH3OOH + CH3",
    kinetics = Arrhenius(
        A = (1.800e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (18500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = 1.6
entry(
    index = 228,
    label = "CH3OO + CH2O <=> CH3OOH + HCO",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (11665.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = 18.9
entry(
    index = 229,
    label = "CH3OO + CH3OH <=> CH3OOH + CH2OH",
    kinetics = Arrhenius(
        A = (1.800e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (13700.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = 2.2
entry(
    index = 230,
    label = "CH3OO + H <=> CH3O + OH",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = 10.1
# *** Fuel Radical Decomposition
# Included in CH4 submechanism
# *** Fuel Radical + Radical
entry(
    index = 231,
    label = "CH3OO + O <=> CH3O + O2",
    kinetics = Arrhenius(
        A = (3.600e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## LIGHTFOOT ET AL. J. CHEM. SOC. FARA TRANS. 1991, 87(19), 3213--3220.
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -41.0
entry(
    index = 232,
    label = "CH3OO + OH <=> CH3OH + O2",
    kinetics = Arrhenius(
        A = (6.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## LIGHTFOOT ET AL. J. CHEM. SOC. FARA TRANS. 1991, 87(19), 3213--3220.
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -57.5
entry(
    index = 233,
    label = "CH3OO + HO2 <=> CH3OOH + O2",
    kinetics = Arrhenius(
        A = (2.500e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-1490.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## LIGHTFOOT ET AL. J. CHEM. SOC. FARA TRANS. 1991, 87(19), 3213--3220.
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -60.0
entry(
    index = 234,
    label = "CH3OO + CH3 <=> CH3O + CH3O",
    kinetics = Arrhenius(
        A = (5.100e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-1411.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# GS Tyndall, RA Cox, C Granier, R Lesclaux, GK Moortgat, MJ Pilling, AR Ravishankara, TJ Wallington, JGR 106:12157 (2001).
# DH = -36.5
entry(
    index = 235,
    label = "CH3OO + CH3O <=> CH2O + CH3OOH",
    kinetics = Arrhenius(
        A = (3.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# M Keiffer, AJ Miscampbell, MJ Pilling JCSFT 2, 84:505 (1988).
# DH=-27.2
entry(
    index = 236,
    label = "CH3OO + CH2OH <=> CH2O + CH3OOH",
    kinetics = Arrhenius(
        A = (1.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -65.1
entry(
    index = 237,
    label = "CH3OO + CH3OO <=> CH3O + CH3O + O2",
    kinetics = Arrhenius(
        A = (5.720e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-775.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -55.6
entry(
    index = 238,
    label = "CH3OO + CH3OO <=> CH3OH + CH2O + O2",
    kinetics = Arrhenius(
        A = (2.180e+09, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-3785.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 3.2

entry(
    index = 240,
    label = "C2H6 + H <=> C2H5 + H2",
    kinetics = Arrhenius(
        A = (7.350e+03, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (5340.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# SJ Klippenstein, unpublished calculations (2014).
# DH = 99.5
# *** Fuel + Radical
entry(
    index = 241,
    label = "C2H6 + H <=> C2H5 + H2",
    kinetics = Arrhenius(
        A = (3.260e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (13667.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 242,
    label = "C2H6 + O <=> C2H5 + OH",
    kinetics = Arrhenius(
        A = (1.810e+05, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (5802.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, JV Michael, B Ruscic, IJCK 44:194 (2012).
# DH = -3.8
entry(
    index = 243,
    label = "C2H6 + OH <=> C2H5 + H2O",
    kinetics = Arrhenius(
        A = (1.900e+05, 'cm^3/(mol*s)'),
        n = 2.51,
        Ea = (880.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# Baulch (2005).
# DH = -2.2
entry(
    index = 244,
    label = "C2H6 + CH3 <=> C2H5 + CH4",
    kinetics = Arrhenius(
        A = (3.450e+01, 'cm^3/(mol*s)'),
        n = 3.44,
        Ea = (10390.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# LN Krasnoperov, JV Michael, JPCA 108:5643 (2004).
# Baulch (2005).
# DH = -18.3
entry(
    index = 245,
    label = "CH2(S) + C2H6 <=> CH3 + C2H5",
    kinetics = Arrhenius(
        A = (1.200e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SL Peukert, NJ Labbe, R Sivaramakrishnan, JV Michael JPCA 117:10228 (2013).
# DH = -3.9
# C2H6+CH
# ## Missing Reaction
# $$ Missing Reaction
# C2H6+CH3O
# ## Missing Reaction
# C2H6+CH3OO
# ## Missing Reaction
# C2H6+CH3OO
# ## Missing Reaction
entry(
    index = 246,
    label = "H + C2H4 <=> C2H5",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1370000000.0, 'cm^3/(mol*s)'), n=1.463, Ea=(1355.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.03e+39, 'cm^6/(mol^2*s)'), n=-6.642, Ea=(5769.0, 'cal/mol'), T0=(1, 'K')),
        alpha = -0.569,
        T3 = (299.0, 'K'),
        T1 = (-9147.0, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = { 'N#N': 1.2, '[C-]#[O+]': 1.5, '[H][H]': 2.0, 'O=C=O': 3.0, 'O': 10.0 }
    ),
)

entry(
    index = 247,
    label = "C2H6 + HO2 <=> C2H5 + H2O2",
    kinetics = Arrhenius(
        A = (2.610e+02, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (15900.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein, PCCP 6:1192 (2004).
# DH = -34.6
# *** Fuel Radical + Stable
entry(
    index = 248,
    label = "CH3CH2CO <=> C2H5 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.710e+04, 's^-1'),
        n = 2.24,
        Ea = (57900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (7.500e+19, 's^-1'),
        n = -3.79,
        Ea = (13100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (1.030e+34, 's^-1'),
        n = -8.02,
        Ea = (17220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (2.960e+32, 's^-1'),
        n = -6.92,
        Ea = (24420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (2.120e+34, 's^-1'),
        n = -7.75,
        Ea = (17700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (3.760e+38, 's^-1'),
        n = -8.36,
        Ea = (28690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (5.840e+33, 's^-1'),
        n = -7.2,
        Ea = (18180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.530e+61, 's^-1'),
        n = -14.6,
        Ea = (43220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (5.820e+31, 's^-1'),
        n = -6.2,
        Ea = (18470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.390e+151, 's^-1'),
        n = -40.33,
        Ea = (99390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (2.800e+12, 's^-1'),
        n = 0.0,
        Ea = (13150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (2.220e+37, 's^-1'),
        n = -7.65,
        Ea = (21720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# ## J. AGUILERA-IPARRAGUIRRE ET AL. J PHYS CHEM A (2008) 112(30): 7047-7054.
# H-H Carstensen, AM Dean, PCI 30:995 (2005).
# $$ Baulch (2005).
# DH = 14.0

entry(
    index = 249,
    label = "CH3CHCHO <=> C2H5 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.190e+24, 's^-1'),
        n = -4.69,
        Ea = (41610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (0.000e+00, 's^-1'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.150e+48, 's^-1'),
        n = -11.6,
        Ea = (54470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (9.020e+17, 's^-1'),
        n = -3.22,
        Ea = (38140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (4.350e+47, 's^-1'),
        n = -11.06,
        Ea = (55840.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (1.230e+17, 's^-1'),
        n = -2.75,
        Ea = (38550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (7.950e+43, 's^-1'),
        n = -9.64,
        Ea = (56040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (9.890e+13, 's^-1'),
        n = -1.61,
        Ea = (38180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (5.140e+23, 's^-1'),
        n = -3.52,
        Ea = (46870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (9.510e+00, 's^-1'),
        n = -7.24,
        Ea = (1184.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.700e+28, 's^-1'),
        n = -4.59,
        Ea = (51600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (3.950e+05, 's^-1'),
        n = 1.31,
        Ea = (36590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 8.3

entry(
    index = 250,
    label = "CH2CHCHOH <=> C2H5 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.970e+93, 's^-1'),
        n = -26.12,
        Ea = (65310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (2.220e+41, 's^-1'),
        n = -17.8,
        Ea = (18980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (5.290e+40, 's^-1'),
        n = -9.39,
        Ea = (48060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (9.490e+16, 's^-1'),
        n = -4.28,
        Ea = (32480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (6.890e+49, 's^-1'),
        n = -11.74,
        Ea = (56000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (4.200e+25, 's^-1'),
        n = -4.98,
        Ea = (42860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (2.140e+45, 's^-1'),
        n = -10.06,
        Ea = (58310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (2.690e+21, 's^-1'),
        n = -3.63,
        Ea = (43090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (4.100e+30, 's^-1'),
        n = -5.55,
        Ea = (54520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (5.670e+17, 's^-1'),
        n = -2.74,
        Ea = (42430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (7.470e+30, 's^-1'),
        n = -5.45,
        Ea = (60120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (3.880e+03, 's^-1'),
        n = 1.87,
        Ea = (40080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 7.6

entry(
    index = 251,
    label = "CH3CH2CHOH <=> C2H5 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.390e+22, 's^-1'),
        n = -4.8,
        Ea = (28700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.810e+31, 's^-1'),
        n = -6.76,
        Ea = (35800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.160e+37, 's^-1'),
        n = -8.17,
        Ea = (41900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.300e+40, 's^-1'),
        n = -8.78,
        Ea = (46800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.570e+38, 's^-1'),
        n = -7.85,
        Ea = (48600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 3.5

entry(
    index = 252,
    label = "CH2CH2CH2OH <=> C2H5 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.960e+23, 's^-1'),
        n = -4.84,
        Ea = (30000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (2.880e+32, 's^-1'),
        n = -6.84,
        Ea = (36700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.100e+41, 's^-1'),
        n = -9.13,
        Ea = (44800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.630e+42, 's^-1'),
        n = -8.86,
        Ea = (47700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.900e+36, 's^-1'),
        n = -6.88,
        Ea = (47100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 19.5

entry(
    index = 253,
    label = "CH3CH2CH2O <=> C2H5 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.220e+32, 's^-1'),
        n = -7.45,
        Ea = (17000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.190e+35, 's^-1'),
        n = -7.95,
        Ea = (18400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.460e+35, 's^-1'),
        n = -7.69,
        Ea = (19200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.180e+31, 's^-1'),
        n = -6.18,
        Ea = (19100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (9.110e+23, 's^-1'),
        n = -3.44,
        Ea = (17700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 13.5

entry(
    index = 254,
    label = "C2H5 + CH2O <=> C2H6 + HCO",
    kinetics = Arrhenius(
        A = (5.500e+03, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5860.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 8.9
entry(
    index = 255,
    label = "C2H5 + O2 <=> CH3CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.280e+42, 'cm^3/(mol*s)'),
        n = -11.12,
        Ea = (5137.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (1.950e+43, 'cm^3/(mol*s)'),
        n = -11.3,
        Ea = (5485.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (1.220e+44, 'cm^3/(mol*s)'),
        n = -11.36,
        Ea = (5850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (3.230e+44, 'cm^3/(mol*s)'),
        n = -11.32,
        Ea = (6198.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (1.310e+45, 'cm^3/(mol*s)'),
        n = -11.33,
        Ea = (6761.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.200e+45, 'cm^3/(mol*s)'),
        n = -11.15,
        Ea = (7163.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (4.340e+44, 'cm^3/(mol*s)'),
        n = -10.83,
        Ea = (7564.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.870e+43, 'cm^3/(mol*s)'),
        n = -10.37,
        Ea = (7810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (3.980e+42, 'cm^3/(mol*s)'),
        n = -9.86,
        Ea = (8124.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.240e+40, 'cm^3/(mol*s)'),
        n = -8.95,
        Ea = (7857.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (2.160e+37, 'cm^3/(mol*s)'),
        n = -7.95,
        Ea = (7525.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.590e+34, 'cm^3/(mol*s)'),
        n = -6.88,
        Ea = (6913.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.590e+30, 'cm^3/(mol*s)'),
        n = -5.56,
        Ea = (5909.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -12.8
# C2H5+CH3OH=C2H6+CH2OH
# $$ Missing Reaction
# *** Fuel Radical + Radical

entry(
    index = 256,
    label = "C2H5 + O2 <=> CH2CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.230e+21, 'cm^3/(mol*s)'),
        n = -5.53,
        Ea = (-83.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (4.600e+23, 'cm^3/(mol*s)'),
        n = -6.12,
        Ea = (586.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (2.860e+25, 'cm^3/(mol*s)'),
        n = -6.6,
        Ea = (1279.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (2.900e+24, 'cm^3/(mol*s)'),
        n = -6.19,
        Ea = (1229.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (5.880e+25, 'cm^3/(mol*s)'),
        n = -6.49,
        Ea = (2026.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.900e+25, 'cm^3/(mol*s)'),
        n = -6.26,
        Ea = (2449.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (4.630e+26, 'cm^3/(mol*s)'),
        n = -6.47,
        Ea = (3598.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.740e+26, 'cm^3/(mol*s)'),
        n = -6.29,
        Ea = (4518.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (3.590e+26, 'cm^3/(mol*s)'),
        n = -6.03,
        Ea = (5715.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.320e+25, 'cm^3/(mol*s)'),
        n = -5.58,
        Ea = (6793.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (6.630e+23, 'cm^3/(mol*s)'),
        n = -4.74,
        Ea = (7756.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.710e+20, 'cm^3/(mol*s)'),
        n = -3.63,
        Ea = (8319.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.900e+15, 'cm^3/(mol*s)'),
        n = -1.72,
        Ea = (8034.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = -32.7

entry(
    index = 257,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    kinetics = Arrhenius(
        A = (7.280e+01, 'cm^3/(mol*s)'),
        n = 3.22,
        Ea = (14942.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# SJ Klippenstein, PCI 36:77 (2017).
# DH = -15.7
entry(
    index = 258,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    kinetics = Arrhenius(
        A = (9.720e-08, 'cm^3/(mol*s)'),
        n = 5.19,
        Ea = (8087.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 259,
    label = "C2H5 + O2 <=> C2H4 + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.100e+00, 'cm^3/(mol*s)'),
        n = 2.87,
        Ea = (-5099.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (1.180e+01, 'cm^3/(mol*s)'),
        n = 2.84,
        Ea = (-5029.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (2.820e+01, 'cm^3/(mol*s)'),
        n = 2.73,
        Ea = (-4780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.100e+02, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (-4380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (9.570e+02, 'cm^3/(mol*s)'),
        n = 2.3,
        Ea = (-3735.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.320e+04, 'cm^3/(mol*s)'),
        n = 1.98,
        Ea = (-2933.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (4.900e+05, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (-1790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.410e+07, 'cm^3/(mol*s)'),
        n = 1.07,
        Ea = (-498.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (2.470e+09, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (1157.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.360e+11, 'cm^3/(mol*s)'),
        n = 0.04,
        Ea = (2789.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (3.130e+12, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (4501.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.290e+12, 'cm^3/(mol*s)'),
        n = -0.33,
        Ea = (5728.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.890e+11, 'cm^3/(mol*s)'),
        n = 0.14,
        Ea = (6373.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True
)

# JD DeSain, SJ Klippenstein, JA Miller, CA Taatjes, JPCA 107:4415 (2003).
# DH = -13.3

entry(
    index = 260,
    label = "C2H5 + O2 <=> c-CH2CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.370e-05, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-5618.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (1.850e-05, 'cm^3/(mol*s)'),
        n = 4.16,
        Ea = (-5537.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (4.960e-05, 'cm^3/(mol*s)'),
        n = 4.04,
        Ea = (-5260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (2.270e-04, 'cm^3/(mol*s)'),
        n = 3.85,
        Ea = (-4825.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (2.590e-03, 'cm^3/(mol*s)'),
        n = 3.55,
        Ea = (-4121.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.180e-02, 'cm^3/(mol*s)'),
        n = 3.18,
        Ea = (-3238.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (4.060e+00, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (-1928.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.080e+02, 'cm^3/(mol*s)'),
        n = 2.04,
        Ea = (-371.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (4.860e+05, 'cm^3/(mol*s)'),
        n = 1.22,
        Ea = (1802.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.990e+08, 'cm^3/(mol*s)'),
        n = 0.39,
        Ea = (4218.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (8.780e+11, 'cm^3/(mol*s)'),
        n = -0.49,
        Ea = (7190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.690e+14, 'cm^3/(mol*s)'),
        n = -1.09,
        Ea = (9936.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (9.680e+14, 'cm^3/(mol*s)'),
        n = -1.22,
        Ea = (12500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = -13.3

entry(
    index = 261,
    label = "C2H5 + H <=> C2H4 + H2",
    kinetics = Arrhenius(
        A = (2.490e+11, 'cm^3/(mol*s)'),
        n = 0.628,
        Ea = (-675.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, PCI 36:77 (2017).
# DH = -31.8
# C2H5+O2=CH3CHO+OH
# ## Missing Reaction
entry(
    index = 262,
    label = "C2H5 + H <=> CH3 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.900e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (67.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm (term 1)
        Arrhenius(
            A = (7.250e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (2220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm (term 2)
        Arrhenius(
            A = (3.900e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (67.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm (term 1)
        Arrhenius(
            A = (7.250e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (2220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm (term 2)
        Arrhenius(
            A = (3.900e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (67.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (7.250e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (2220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.900e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (67.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 1)
        Arrhenius(
            A = (7.250e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (2220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 2)
        Arrhenius(
            A = (3.970e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (81.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (7.250e+14, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (2241.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.510e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (199.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 1)
        Arrhenius(
            A = (5.570e+14, 'cm^3/(mol*s)'),
        n = -0.21,
        Ea = (2260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 2)
        Arrhenius(
            A = (1.620e+59, 'cm^3/(mol*s)'),
        n = -16.67,
        Ea = (7216.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (5.180e+14, 'cm^3/(mol*s)'),
        n = -0.13,
        Ea = (731.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.580e+18, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (3057.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 1)
        Arrhenius(
            A = (3.700e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (-233.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 2)
        Arrhenius(
            A = (8.500e+22, 'cm^3/(mol*s)'),
        n = -2.56,
        Ea = (6492.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.590e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (666.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.520e+23, 'cm^3/(mol*s)'),
        n = -2.71,
        Ea = (8376.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 1)
        Arrhenius(
            A = (6.530e+11, 'cm^3/(mol*s)'),
        n = 0.64,
        Ea = (914.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 2)
        Arrhenius(
            A = (2.050e+23, 'cm^3/(mol*s)'),
        n = -2.46,
        Ea = (9901.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.540e+12, 'cm^3/(mol*s)'),
        n = 0.34,
        Ea = (1388.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# SJ Klippenstein, unpublished calculations (2014).
# DH = -68.6

entry(
    index = 263,
    label = "C2H5 + O <=> C2H4 + OH",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished calculations (2014).
# DH = -11.4
entry(
    index = 264,
    label = "C2H5 + O <=> CH3 + CH2O",
    kinetics = Arrhenius(
        A = (4.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# IR Slagle, D Sarzynski, D Gutman, JA Miller, CF Melius, J. Chem. Soc. Farday Trans. 2 84:491 (1988); overall rate
# JA Miller, P Glarborg - estimated branching
# $$ Baulch (2005).
# DH = -67.0
entry(
    index = 265,
    label = "C2H5 + O <=> CH3CHO + H",
    kinetics = Arrhenius(
        A = (5.300e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# IR Slagle, D Sarzynski, D Gutman, JA Miller, CF Melius, J. Chem. Soc. Farday Trans. 2 84:491 (1988); overall rate
# JA Miller, P Glarborg - estimated branching
# $$ Baulch (2005).
# DH = -79.9
entry(
    index = 266,
    label = "CH3CH2OH <=> C2H5 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.820e+56, 's^-1'),
        n = -13.49,
        Ea = (107238.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.650e+63, 's^-1'),
        n = -14.99,
        Ea = (109623.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.460e+65, 's^-1'),
        n = -14.89,
        Ea = (112345.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.790e+61, 's^-1'),
        n = -13.4,
        Ea = (113080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.170e+51, 's^-1'),
        n = -10.34,
        Ea = (109941.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# IR Slagle, D Sarzynski, D Gutman, JA Miller, CF Melius, J. Chem. Soc. Farday Trans. 2 84:491 (1988); overall rate
# JA Miller, P Glarborg - estimated branching
# $$ Baulch (2005).
# DH = -75.8

entry(
    index = 267,
    label = "C2H5 + OH <=> C2H4 + H2O",
    kinetics = Arrhenius(
        A = (5.580e+10, 'cm^3/(mol*s)'),
        n = 0.735,
        Ea = (-931.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# DH = 92.4
entry(
    index = 268,
    label = "C2H5 + OH <=> C2H4 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.290e+19, 'cm^3/(mol*s)'),
        n = -1.96,
        Ea = (273.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.220e+19, 'cm^3/(mol*s)'),
        n = -1.953,
        Ea = (239.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.110e+19, 'cm^3/(mol*s)'),
        n = -2.101,
        Ea = (625.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.940e+22, 'cm^3/(mol*s)'),
        n = -2.989,
        Ea = (3863.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.790e+24, 'cm^3/(mol*s)'),
        n = -3.329,
        Ea = (7749.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.700e+18, 'cm^3/(mol*s)'),
        n = -1.58,
        Ea = (7999.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True
)

# SJ Klippenstein - unpublished calculations (2014); abstraction component
# DH = -83.1

entry(
    index = 269,
    label = "C2H5 + OH <=> CH3 + CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.200e+17, 'cm^3/(mol*s)'),
        n = -1.299,
        Ea = (2505.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.100e+18, 'cm^3/(mol*s)'),
        n = -1.321,
        Ea = (2569.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.740e+18, 'cm^3/(mol*s)'),
        n = -1.518,
        Ea = (3185.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.530e+21, 'cm^3/(mol*s)'),
        n = -2.351,
        Ea = (6023.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.880e+25, 'cm^3/(mol*s)'),
        n = -3.249,
        Ea = (10576.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.500e+22, 'cm^3/(mol*s)'),
        n = -2.443,
        Ea = (12647.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DJ = -83.1

entry(
    index = 270,
    label = "C2H5 + HO2 <=> CH3CH2O + OH",
    kinetics = Arrhenius(
        A = (2.680e+13, 'cm^3/(mol*s)'),
        n = -0.845,
        Ea = (-23.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -7.1
entry(
    index = 271,
    label = "C2H6 + O2 <=> C2H5 + HO2",
    kinetics = Arrhenius(
        A = (7.290e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (49158.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# E Kamarchik, AW Jasper - unpublished (2013).
# DH = -26.0
entry(
    index = 272,
    label = "C2H5 + HCO <=> C2H6 + CO",
    kinetics = Arrhenius(
        A = (4.300e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 51.5
entry(
    index = 273,
    label = "C2H5 + HCO <=> C2H4 + CH2O",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JE Bagott, HM Frey, PD Lightfoot, R Walsh, JPC 91:3386 (1987).
# DH = -84.8
entry(
    index = 274,
    label = "C2H5 + CH3 <=> C2H4 + CH4",
    kinetics = Arrhenius(
        A = (1.950e+13, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate.
# DH = -52.0
entry(
    index = 275,
    label = "C3H8 <=> CH3 + C2H5",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.55e+24, 's^-1'), n=-2.034, Ea=(90388.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.77e+77, 'cm^3/(mol*s)'), n=-16.67, Ea=(100100.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.81,
        T3 = (3091.0, 'K'),
        T1 = (128.0, 'K'),
        T2 = (8829.0, 'K'),
        efficiencies = { 'O': 5.0, '[H][H]': 2.0, '[C-]#[O+]': 2.0, 'O=C=O': 3.0 }
    ),
)

entry(
    index = 276,
    label = "C2H5 + C2H5 <=> C2H4 + C2H6",
    kinetics = Arrhenius(
        A = (1.400e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 115:3366 (2011).
# DH = 87.1
entry(
    index = 277,
    label = "CH3CHO <=> CH2CHOH",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.1, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.310e+45, 's^-1'),
        n = -10.04,
        Ea = (78785.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (2.930e+45, 's^-1'),
        n = -9.86,
        Ea = (78884.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.110e+46, 's^-1'),
        n = -9.76,
        Ea = (81964.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.780e+45, 's^-1'),
        n = -9.35,
        Ea = (84645.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

#  W Tsang, RF Hampson JPCRD 15:1087 (1986).
#  DH = -64.8
# C2H5+CH3OO=C2H5O+CH3O	NO ARRHENIUS PARAMETERS
#  ## Missing Reaction
#  *****************************************************************************
#     CH3CHO subset                                                            *
#     CH2CHOH subset                                                           *
#     c-CH2CH2O subset
#  *****************************************************************************
#  Fuel Radicals: CH3CO, CH2CHO, CHCHOH
#  New Radicals Formed: CH3CHOH
#  New Fuels: OCHCHO
#  *** Fuel Decomposition
#  Note: Decomposition to CH3 + HCO, is included in CH4 submechanism
#  CH3CHO=CH4+CO
#  $$ Missing Reaction
#  DH = ??

entry(
    index = 278,
    label = "CH3CHO <=> CH2CO + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.1, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.980e+44, 's^-1'),
        n = -10.07,
        Ea = (87428.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (7.380e+44, 's^-1'),
        n = -10.05,
        Ea = (88422.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.540e+44, 's^-1'),
        n = -9.77,
        Ea = (90905.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.220e+45, 's^-1'),
        n = -9.55,
        Ea = (94879.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# SJ Klippenstein - unpublished.
# DH = 9.7

entry(
    index = 279,
    label = "CH3CHO <=> CH4 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.1, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.120e+45, 's^-1'),
        n = -9.85,
        Ea = (89018.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (1.440e+45, 's^-1'),
        n = -9.65,
        Ea = (87925.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.870e+45, 's^-1'),
        n = -9.43,
        Ea = (89415.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.640e+45, 's^-1'),
        n = -9.1,
        Ea = (92793.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# R Sivaramkrishnan, JV Michael, SJ Klippenstein, JPCA 114:755 (2010).
# 0.05 atm Roaming
# DH = 26.1

entry(
    index = 280,
    label = "CH2CHOH <=> CH2CHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.160e+65, 's^-1'),
        n = -17.67,
        Ea = (93699.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.710e+66, 's^-1'),
        n = -16.74,
        Ea = (98013.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.920e+54, 's^-1'),
        n = -11.75,
        Ea = (99871.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# R Sivaramkrishnan, JV Michael, SJ Klippenstein, JPCA 114:755 (2010).
# 0.05 atm Roaming
# DH = -6.1

entry(
    index = 281,
    label = "CH2CHOH <=> C2H2 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.850e+60, 's^-1'),
        n = -16.89,
        Ea = (90603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.240e+63, 's^-1'),
        n = -16.19,
        Ea = (96099.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.400e+50, 's^-1'),
        n = -11.09,
        Ea = (97892.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JX Shao, CM Gong, XY Li, J Li, TCA 128:314 (2011).
# DH = 84.6

entry(
    index = 282,
    label = "CH2CHOH <=> CH2C + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.570e+61, 's^-1'),
        n = -16.7,
        Ea = (90057.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.260e+63, 's^-1'),
        n = -16.05,
        Ea = (95573.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.070e+50, 's^-1'),
        n = -10.95,
        Ea = (97089.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JX Shao, CM Gong, XY Li, J Li, TCA 128:314 (2011).
# DH = 24.8

entry(
    index = 283,
    label = "CH3CHOH <=> H + CH3CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.05, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.210e+32, 's^-1'),
        n = -6.915,
        Ea = (36561.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.480e+34, 's^-1'),
        n = -7.133,
        Ea = (38747.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (1.640e+36, 's^-1'),
        n = -7.493,
        Ea = (40201.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.800e+34, 's^-1'),
        n = -6.722,
        Ea = (41727.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.230e+31, 's^-1'),
        n = -5.523,
        Ea = (41727.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.650e+18, 's^-1'),
        n = -1.662,
        Ea = (36263.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JX Shao, CM Gong, XY Li, J Li, TCA 128:314 (2011).
# DH = 68.6
# c-CH2CH2O=CH3+HCO
# ## Missing Reaction
# c-CH2CH2O=CH3CHO
# ## Missing Reaction
# *** Fuel + Radical

entry(
    index = 284,
    label = "CH3CHO + H <=> CH3CO + H2",
    kinetics = Arrhenius(
        A = (2.810e+10, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (2663.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110, 6960 (2006).
# DH = 24.9
entry(
    index = 285,
    label = "CH3CHO + H <=> CH2CHO + H2",
    kinetics = Arrhenius(
        A = (3.640e+05, 'cm^3/(mol*s)'),
        n = 2.59,
        Ea = (5523.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramkrishnan, JV Michael, SJ Klippenstein, JPCA 114:755 (2010).
# DH = -15.7
entry(
    index = 286,
    label = "CH3CHO + O <=> CH3CO + OH",
    kinetics = Arrhenius(
        A = (4.100e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1528.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramkrishnan, JV Michael, SJ Klippenstein, JPCA 114:755 (2010).
# DH = -9.1
entry(
    index = 287,
    label = "CH3CHO + O <=> CH2CHO + OH",
    kinetics = Arrhenius(
        A = (8.550e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (6239.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -14.1
entry(
    index = 288,
    label = "CH3CHO + OH <=> CH3CO + H2O",
    kinetics = Arrhenius(
        A = (2.610e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-733.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -7.5
entry(
    index = 289,
    label = "CH3CHO + OH <=> CH2CHO + H2O",
    kinetics = Arrhenius(
        A = (5.040e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4789.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# PH Taylor, T Yamada, P Marshall, IJCK 38:489 (2006).
# DH = -30.2
entry(
    index = 290,
    label = "CH3CH(O)CH3 <=> CH3CHO + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.760e+31, 's^-1'),
        n = -7.2,
        Ea = (16400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.180e+35, 's^-1'),
        n = -7.97,
        Ea = (18000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.100e+35, 's^-1'),
        n = -7.88,
        Ea = (18900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.090e+34, 's^-1'),
        n = -6.93,
        Ea = (19200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.420e+27, 's^-1'),
        n = -4.63,
        Ea = (18400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# PH Taylor, T Yamada, P Marshall, IJCK 38:489 (2006).
# DH = -23.6
# CH3CHO+OH=CH3+OCHOH
# ## Missing Reaction

entry(
    index = 291,
    label = "CH3CHO + CH3 <=> CH3CO + CH4",
    kinetics = Arrhenius(
        A = (2.000e-06, 'cm^3/(mol*s)'),
        n = 5.6,
        Ea = (2464.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 4.9
entry(
    index = 292,
    label = "H + CH2CHOH <=> CH3CHOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.05, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.670e+40, 'cm^3/(mol*s)'),
        n = -9.339,
        Ea = (8697.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.410e+34, 'cm^3/(mol*s)'),
        n = -7.166,
        Ea = (7916.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (1.660e+34, 'cm^3/(mol*s)'),
        n = -6.868,
        Ea = (8175.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.110e+31, 'cm^3/(mol*s)'),
        n = -5.802,
        Ea = (8928.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.990e+21, 'cm^3/(mol*s)'),
        n = -2.434,
        Ea = (5365.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (9.010e+14, 'cm^3/(mol*s)'),
        n = -0.376,
        Ea = (3577.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# ## GUPTE ET AL.,PROC COMBUST INST 31 (2007) 167:174
# DL Baulch, CJ Cobos, RA Cox, P Frank, G Hayman, Th Just, JA Kerr, T Murrells, MJ Pilling, J Troe, RW Walker, J Warnatz JPCRD 23:847 (1994).
# DH = -15.8
# CH3CHO+CH3OO=CH3CO+CH3OOH
# ## Missing Reaction
# CH3CHO+CH3CO3=CH3CO+CH3CO3H
# ## Missing Reaction

entry(
    index = 293,
    label = "CH2CHOH + H <=> CH2CHO + H2",
    kinetics = Arrhenius(
        A = (7.190e+01, 'cm^3/(mol*s)'),
        n = 3.36,
        Ea = (5266.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan  - based on
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -34.6
entry(
    index = 294,
    label = "H + CH2CHOH <=> CH3CHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.05, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.640e+12, 'cm^3/(mol*s)'),
        n = 0.506,
        Ea = (3394.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.860e+13, 'cm^3/(mol*s)'),
        n = 0.078,
        Ea = (4715.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (3.850e+14, 'cm^3/(mol*s)'),
        n = -0.145,
        Ea = (5464.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.180e+17, 'cm^3/(mol*s)'),
        n = -0.957,
        Ea = (8743.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.640e+20, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (12916.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.080e+18, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (15264.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# R Sivaramakrishnan - unpublished calculation.
# CCSD(T)/CBS//QCISD Variflex TST RRHO
# DH = -18.7

entry(
    index = 295,
    label = "H + CH2CHOH <=> CH3 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.05, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.150e+10, 'cm^3/(mol*s)'),
        n = 0.587,
        Ea = (3475.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.820e+12, 'cm^3/(mol*s)'),
        n = 0.161,
        Ea = (4783.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (1.170e+13, 'cm^3/(mol*s)'),
        n = -0.06,
        Ea = (5518.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.230e+16, 'cm^3/(mol*s)'),
        n = -0.87,
        Ea = (8745.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.210e+19, 'cm^3/(mol*s)'),
        n = -1.789,
        Ea = (13581.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.180e+17, 'cm^3/(mol*s)'),
        n = -1.0,
        Ea = (15302.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# R Sivaramakrishnan  - based on
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -9.7

entry(
    index = 296,
    label = "OH + C2H4 <=> CH2CHOH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.040e+04, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (4121.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.070e+04, 'cm^3/(mol*s)'),
        n = 2.6,
        Ea = (4129.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.520e+04, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (4238.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.190e+05, 'cm^3/(mol*s)'),
        n = 2.19,
        Ea = (5256.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.940e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (7829.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.550e+10, 'cm^3/(mol*s)'),
        n = 0.75,
        Ea = (11491.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# R Sivaramakrishnan  - based on
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -13.7

entry(
    index = 297,
    label = "CH2CHOH + H <=> CH2CO + H + H2",
    kinetics = Arrhenius(
        A = (2.310e+08, 'cm^3/(mol*s)'),
        n = 2.01,
        Ea = (14585.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
#  JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
#  DH = 0.9
# c-CH2CH2O+H=c-CH2CHO+H
#  ## Missing Reaction
#  c-CH2CH2O+OH=c-CH2CHO+H2O
#  ## Missing Reaction
#  c-CH2CH2O+HO2=c-CH2CHO+H2O2
#  ## Missing Reaction
#  c-CH2CH2O+CH3=c-CH2CHO+CH4
#  ## Missing Reaction
#  c-CH2CH2O+CH3O=c-CH2CHO+CH3OH
#  ## Missing Reaction
#  c-CH2CH2O+CH3OO=c-CH2CHO+CH3OOH
#  ## Missing Reaction
#  c-CH2CH2O+CH3CH2OO=c-CH2CHO+CH3CH2OOH
#  ## Missing Reaction
#  *** Fuel Radical + Radical
entry(
    index = 298,
    label = "CH2CHOH + O <=> CH2CHO + OH",
    kinetics = Arrhenius(
        A = (1.460e-03, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, JV Michael, LB Harding, SJ Klippenstein, JPCA 119:7724 (2015).
# DH = 16.5
entry(
    index = 299,
    label = "CH2CHOH + OH <=> CH2CHO + H2O",
    kinetics = Arrhenius(
        A = (2.900e-02, 'cm^3/(mol*s)'),
        n = 4.28,
        Ea = (-3561.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimate
# DH = -17.1
entry(
    index = 300,
    label = "CH3CHO + HO2 <=> CH2CHO + H2O2",
    kinetics = Arrhenius(
        A = (1.100e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (23248.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimate
# DH = -33.2
entry(
    index = 301,
    label = "CH3CH2CHOH <=> CH2CHOH + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.010e+39, 's^-1'),
        n = -8.34,
        Ea = (38200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.670e+41, 's^-1'),
        n = -8.8,
        Ea = (41900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.960e+40, 's^-1'),
        n = -8.21,
        Ea = (43700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.540e+34, 's^-1'),
        n = -6.18,
        Ea = (42500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# M Altarawneh AH Al-Muhtaseb BZ Dlugogorski EM Kennedy JC Mackie J Comput Chem 32: 17251733, 2011

entry(
    index = 302,
    label = "CH3CH(OH)CH2 <=> CH2CHOH + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.810e+15, 's^-1'),
        n = -2.39,
        Ea = (23300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.720e+26, 's^-1'),
        n = -4.99,
        Ea = (30000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.270e+33, 's^-1'),
        n = -6.63,
        Ea = (35800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.830e+36, 's^-1'),
        n = -7.14,
        Ea = (40100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.720e+32, 's^-1'),
        n = -5.66,
        Ea = (40400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 21.8

entry(
    index = 303,
    label = "CH2CHOH + CH3 <=> CH2CHO + CH4",
    kinetics = Arrhenius(
        A = (2.040e+00, 'cm^3/(mol*s)'),
        n = 3.57,
        Ea = (7721.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 18.8
entry(
    index = 304,
    label = "CHCHOH + O2 <=> OCHCHO + OH",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimate
# DH = -18.8
# CH2CHOH+CH3OO=CH2CHO+CH3OOH
# ## Missing Reaction
entry(
    index = 305,
    label = "CHCHOH + H <=> CH2CHO + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate.
# DH = -73.4
entry(
    index = 306,
    label = "CHCHOH + O <=> OCHCHO + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate.
# DH = -27.3
entry(
    index = 307,
    label = "CH2CHO <=> H + CH2CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.390e+25, 's^-1'),
        n = -4.8,
        Ea = (43424.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.480e+27, 's^-1'),
        n = -5.23,
        Ea = (44304.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (2.370e+30, 's^-1'),
        n = -5.86,
        Ea = (46114.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.320e+34, 's^-1'),
        n = -6.57,
        Ea = (49454.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.460e+36, 's^-1'),
        n = -6.92,
        Ea = (52979.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.180e+36, 's^-1'),
        n = -6.48,
        Ea = (55171.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate.
# DH = -90.0
# *** Fuel Radical Decomposition

entry(
    index = 308,
    label = "CH3CHO + HO2 <=> CH3CO + H2O2",
    kinetics = Arrhenius(
        A = (1.490e-05, 'cm^3/(mol*s)'),
        n = 5.05,
        Ea = (4847.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA, 110:5772 (2006).
# DH = 35.2
# c-CH2CHO=CH3CO
# ## Missing Reaction
# c-CH2CHO=CH2CHO
# ## Missing Reaction
# *** Fuel Radical + Stable
entry(
    index = 309,
    label = "CH2CHOH + H <=> CHCHOH + H2",
    kinetics = Arrhenius(
        A = (7.180e+07, 'cm^3/(mol*s)'),
        n = 1.96,
        Ea = (15205.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - unpublished calculation.
# CCSD(T)/aug-cc-pvinfz//DFT
# DH = 1.5
entry(
    index = 310,
    label = "CH3CO + H <=> CH2CO + H2",
    kinetics = Arrhenius(
        A = (1.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - unpublished calculation.
# CCSD(T)/CBS//QCISD Variflex TST RRHO
# DH = 8.6
# *** Fuel Radical + Radical
entry(
    index = 311,
    label = "CH3CO + H <=> CH3 + HCO",
    kinetics = Arrhenius(
        A = (2.100e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# M Bartels, J Edelbuttal, K Hoyermann, PCI 23:131 (1991).
# K Ohmori, A Miyoshi, H Matsui, N Washida, JPC 94:3253 (1990).
# DH = -61.5
entry(
    index = 312,
    label = "CH3CO + O <=> CH3 + CO2",
    kinetics = Arrhenius(
        A = (1.500e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# M Bartels, J Edelbuttal, K Hoyermann, PCI 23:131 (1991).
# K Ohmori, A Miyoshi, H Matsui, N Washida, JPC 94:3253 (1990).
# DH = -42.0
# CH3CO+H(+M)=CH3CHO(+M)
# $$ Missing Reaction
# DH = ??
entry(
    index = 313,
    label = "CH3CO + O <=> CH2CO + OH",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CJ Cobos, RA Cox, P Frank, G Hayman, Th Just, JA Kerr, T Murrells, MJ Pilling, J Troe, RW Walker, J Warnatz JPCRD 23:847 (1994).
# $$ Baulch 2005
# DH = -116.2
entry(
    index = 314,
    label = "CH3CO + OH <=> CH2CO + H2O",
    kinetics = Arrhenius(
        A = (1.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CJ Cobos, RA Cox, P Frank, G Hayman, Th Just, JA Kerr, T Murrells, MJ Pilling, J Troe, RW Walker, J Warnatz JPCRD 23:847 (1994).
# $$ Baulch 2005
# DH = -59.9
entry(
    index = 315,
    label = "CH3CHO + O2 <=> CH3CO + HO2",
    kinetics = Arrhenius(
        A = (1.200e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37554.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -75.9
# CH3CO+OH=CH3+CO+OH
# $$ Missing Reaction
# DH = ??
entry(
    index = 316,
    label = "CH2CHO + O2 <=> CH2O + CO + OH",
    kinetics = Arrhenius(
        A = (2.200e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 39.6
# CH3CO+HO2=CH3+CO2+OH
# $$ Missing Reaction
# DH = ??
entry(
    index = 317,
    label = "CH2CHO + H <=> CH3 + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.490e+17, 'cm^3/(mol*s)'),
        n = -0.903,
        Ea = (3023.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.930e+17, 'cm^3/(mol*s)'),
        n = -0.935,
        Ea = (3120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.540e+18, 'cm^3/(mol*s)'),
        n = -1.243,
        Ea = (4062.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.930e+22, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (7693.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.790e+25, 'cm^3/(mol*s)'),
        n = -3.1,
        Ea = (12454.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.470e+20, 'cm^3/(mol*s)'),
        n = -1.693,
        Ea = (13429.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# ## J. LEE, AND J.W. BOZZELLI. J. PHYS. CHEM. A, 2003, 107 (19), 3778-3791
# DL Baulch, CJ Cobos, RA Cox, P Frank, G Hayman, Th Just, JA Kerr, T Murrells, MJ Pilling, J Troe, RW Walker, J Warnatz JPCRD 23:847 (1994).
# $$ Baulch (2005).
# DH = -48.9
# CH2CHO+O2=CH2CO+HO2
# ## Missing Reaction
# CH2CHO+O2=O2CH2HO
# ## Missing Reaction
# CH2CHO+O2=HO2CH2CO
# ## Missing Reaction
# O2CH2CHO=HO2CH2CO
# ## Missing Reaction
# O2CH2CHO=CH2CO+HO2
# ## Missing Reaction
# HO2CH2CO=CO+CH2O+OH
# ## Missing Reaction
# HO2CH2CO=CH2CO+HO2
# ## Missing Reaction
# CH3CO+O2=CH3CO3
# ## Missing Reaction
# CH3CO+O2=HO2+CH2CO
# $$ Missing Reaction
# CH3CO+CH3=CH2CO+CH4
# ## Missing Reaction
# $$ Missing Reaction; Hassinen E, Kalliorinne K, Koskikallio J. Kinetics of reactions between methyl and acetyl radicals in gas phase produced by flash photolysis of acetic anhydride. Int J Chem Kinet. 1990;22:741-5.

entry(
    index = 318,
    label = "CH2CHO + H <=> H + CH3CO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.600e+13, 'cm^3/(mol*s)'),
        n = 0.051,
        Ea = (4302.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (4.640e+13, 'cm^3/(mol*s)'),
        n = 0.021,
        Ea = (4392.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.370e+14, 'cm^3/(mol*s)'),
        n = -0.217,
        Ea = (5113.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.210e+17, 'cm^3/(mol*s)'),
        n = -1.158,
        Ea = (8193.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.580e+22, 'cm^3/(mol*s)'),
        n = -2.273,
        Ea = (13261.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.070e+19, 'cm^3/(mol*s)'),
        n = -1.51,
        Ea = (15534.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = - 11.6

entry(
    index = 319,
    label = "CH2CHO + O <=> CH2O + HCO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -6.6
# CH2CHO+H=CH2CH+H2
# $$ Missing Reaction
entry(
    index = 320,
    label = "C2H2 + HO2 <=> CH2CHO + O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.500e+06, 'cm^3/(mol*s)'),
        n = 1.19,
        Ea = (12880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.940e-04, 'cm^3/(mol*s)'),
        n = 4.16,
        Ea = (7736.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.160e+08, 'cm^3/(mol*s)'),
        n = 0.77,
        Ea = (13600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.140e-03, 'cm^3/(mol*s)'),
        n = 3.81,
        Ea = (8394.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.200e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (13050.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (5.440e-04, 'cm^3/(mol*s)'),
        n = 4.09,
        Ea = (8044.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.020e+07, 'cm^3/(mol*s)'),
        n = 0.98,
        Ea = (13310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.480e-04, 'cm^3/(mol*s)'),
        n = 4.19,
        Ea = (8203.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.980e+74, 'cm^3/(mol*s)'),
        n = -16.33,
        Ea = (109200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (6.570e+04, 'cm^3/(mol*s)'),
        n = 1.85,
        Ea = (12360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (7.500e+14, 'cm^3/(mol*s)'),
        n = -1.17,
        Ea = (18350.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.920e-01, 'cm^3/(mol*s)'),
        n = 3.38,
        Ea = (10590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (8.630e+18, 'cm^3/(mol*s)'),
        n = -2.27,
        Ea = (22230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.950e+00, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (11740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (5.780e+18, 'cm^3/(mol*s)'),
        n = -2.09,
        Ea = (24350.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.100e-01, 'cm^3/(mol*s)'),
        n = 3.52,
        Ea = (11980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller - estimate
# DH = -80.1
# CH2CHO+O=H+CH2+CO2
# $$ Missing Reaction
# DH = ??

entry(
    index = 321,
    label = "CH2CHO + OH <=> CH2CO + H2O",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = 6.5
entry(
    index = 322,
    label = "CH2CHO + OH <=> CH2OH + HCO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -82.6
entry(
    index = 323,
    label = "C2H4 + O2 <=> CH2CHO + OH",
    kinetics = Arrhenius(
        A = (7.100e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (60010.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -7.4
entry(
    index = 324,
    label = "C2H5 + HCO <=> CH3 + CH2CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.200e+17, 'cm^3/(mol*s)'),
        n = -1.299,
        Ea = (2505.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.100e+18, 'cm^3/(mol*s)'),
        n = -1.321,
        Ea = (2569.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.740e+18, 'cm^3/(mol*s)'),
        n = -1.518,
        Ea = (3185.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.530e+21, 'cm^3/(mol*s)'),
        n = -2.351,
        Ea = (6023.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.880e+25, 'cm^3/(mol*s)'),
        n = -3.249,
        Ea = (10576.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.500e+22, 'cm^3/(mol*s)'),
        n = -2.443,
        Ea = (12647.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# H Hua, B Ruscic,  B Wang  Chem. Phys. 311:335 (2005).
# DH = 0.3

entry(
    index = 325,
    label = "CH2CHO + CH2 <=> C2H4 + HCO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015); estimate.
# DH = 0.3
entry(
    index = 326,
    label = "CH2CHO + CH <=> C2H3 + HCO",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -74.9
entry(
    index = 327,
    label = "CH3CH2OH <=> C2H4 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.620e+57, 's^-1'),
        n = -13.29,
        Ea = (85262.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.650e+52, 's^-1'),
        n = -11.52,
        Ea = (84746.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.230e+43, 's^-1'),
        n = -8.9,
        Ea = (81507.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.590e+32, 's^-1'),
        n = -5.6,
        Ea = (76062.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.840e+20, 's^-1'),
        n = -2.06,
        Ea = (69466.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -65.7
# *****************************************************************************
#    CH3CH2OH subset                                                          *
# *****************************************************************************
# Fuel Radicals: CH3CHOH, CH2CH2OH,CH3CH2O
# New Radicals Formed: OHCH2CH2OO
# New Fuels: CH3CHCH2
# *** Fuel Decomposition
# Decomposition to CH3 + CH2OH included in CH3OH submechanism
# Decomposition to C2H5 + OH included in C2H6 submechanism

entry(
    index = 328,
    label = "CH3CH2OH <=> CH3CHO + H2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(724000000000.0, 's^-1'), n=0.095, Ea=(91007.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.46e+87, 'cm^3/(mol*s)'), n=-19.42, Ea=(115590.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.9,
        T3 = (900.0, 'K'),
        T1 = (1100.0, 'K'),
        T2 = (3500.0, 'K'),
        efficiencies = { 'O': 5.0 }
    ),
)

entry(
    index = 329,
    label = "CH3CH2OH + H <=> CH3CHOH + H2",
    kinetics = Arrhenius(
        A = (1.720e+09, 'cm^3/(mol*s)'),
        n = 1.376,
        Ea = (4533.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = 14.9
# *** Fuel + Radical
entry(
    index = 330,
    label = "CH3CH2OH + H <=> CH2CH2OH + H2",
    kinetics = Arrhenius(
        A = (8.780e+08, 'cm^3/(mol*s)'),
        n = 1.526,
        Ea = (9060.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# k tot Expt, BR Theory
# DH = -10.0
entry(
    index = 331,
    label = "CH3CH2OH + O <=> CH3CHOH + OH",
    kinetics = Arrhenius(
        A = (1.450e+05, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (876.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# k tot Expt, BR Theory
# DH = -2.6
entry(
    index = 332,
    label = "CH3CH2OH + O <=> CH2CH2OH + OH",
    kinetics = Arrhenius(
        A = (9.700e+02, 'cm^3/(mol*s)'),
        n = 3.23,
        Ea = (4658.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CW Wu, YP Lee, SC Xu, MC Lin, JPCA 111:6693 (2007).
# DH = -8.4
entry(
    index = 333,
    label = "CH3CH2OH + OH <=> CH3CHOH + H2O",
    kinetics = Arrhenius(
        A = (5.950e+08, 'cm^3/(mol*s)'),
        n = 1.273,
        Ea = (-499.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CW Wu, YP Lee, SC Xu, MC Lin, JPCA 111:6693 (2007).
# DH = -1.0
entry(
    index = 334,
    label = "CH3CH2OH + OH <=> CH2CH2OH + H2O",
    kinetics = Arrhenius(
        A = (9.020e+05, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (1435.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# DH = -24.5
entry(
    index = 335,
    label = "CH3CH2OH + OH <=> CH3CH2O + H2O",
    kinetics = Arrhenius(
        A = (5.710e+03, 'cm^3/(mol*s)'),
        n = 2.567,
        Ea = (-263.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# DH = -17.1
entry(
    index = 336,
    label = "CH3CH2OH + CH3 <=> CH3CHOH + CH4",
    kinetics = Arrhenius(
        A = (1.990e+01, 'cm^3/(mol*s)'),
        n = 3.37,
        Ea = (7634.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# DH = -13.8
entry(
    index = 337,
    label = "CH3CH2OH + CH3 <=> CH2CH2OH + CH4",
    kinetics = Arrhenius(
        A = (3.300e+02, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (12290.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ZF Xu, J Park, MC Lin, JCP 120:6593 (2004).
# DH = -10.1
entry(
    index = 338,
    label = "OH + C2H4 <=> CH2CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.760e+47, 'cm^3/(mol*s)'),
        n = -11.64,
        Ea = (11099.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.020e+37, 'cm^3/(mol*s)'),
        n = -9.76,
        Ea = (1995.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 1)
        Arrhenius(
            A = (4.960e+37, 'cm^3/(mol*s)'),
        n = -8.68,
        Ea = (5355.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 2)
        Arrhenius(
            A = (6.020e+37, 'cm^3/(mol*s)'),
        n = -9.65,
        Ea = (2363.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.560e+35, 'cm^3/(mol*s)'),
        n = -7.79,
        Ea = (5017.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (6.020e+37, 'cm^3/(mol*s)'),
        n = -8.14,
        Ea = (8043.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (7.290e+31, 'cm^3/(mol*s)'),
        n = -6.91,
        Ea = (2855.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (6.020e+37, 'cm^3/(mol*s)'),
        n = -7.77,
        Ea = (10736.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (3.020e+26, 'cm^3/(mol*s)'),
        n = -4.87,
        Ea = (2297.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.020e+37, 'cm^3/(mol*s)'),
        n = -7.44,
        Ea = (14269.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.790e+19, 'cm^3/(mol*s)'),
        n = -2.41,
        Ea = (1011.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# ZF Xu, J Park, MC Lin, JCP 120:6593 (2004).
# DH = -2.7
# *** Fuel Radical Decomposition

entry(
    index = 339,
    label = "CH3CH2O <=> CH3CHO + H",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.160e+35, 'cm^3/(mol*s)'),
        n = -5.89,
        Ea = (25274.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = None,
    ),
    
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -26.3
entry(
    index = 340,
    label = "CH3CH2OH + H <=> CH3CH2O + H2",
    kinetics = Arrhenius(
        A = (1.560e+07, 'cm^3/(mol*s)'),
        n = 1.856,
        Ea = (10266.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = 14.3
# *** Fuel Radical + Stable
entry(
    index = 341,
    label = "CH3CH2OH + HO2 <=> CH3CHOH + H2O2",
    kinetics = Arrhenius(
        A = (5.930e-02, 'cm^3/(mol*s)'),
        n = 4.05,
        Ea = (10432.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# R Sivaramakrishnan, MC Su, JV Michael, SJ Klippenstein, LB Harding, B Ruscic, JPCA 114:9425 (2010).
# k tot Expt, BR Theory
# DH = 0.6
entry(
    index = 342,
    label = "CH3CH2OH + HO2 <=> CH3CHOH + H2O2",
    kinetics = Arrhenius(
        A = (2.110e+09, 'cm^3/(mol*s)'),
        n = 1.0,
        Ea = (20651.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 343,
    label = "CH3CH2OH + HO2 <=> CH2CH2OH + H2O2",
    kinetics = Arrhenius(
        A = (1.230e+04, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (15750.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan unpublished
# CCSD(T)/cc-pvinfz TST
# DH = 7.2
entry(
    index = 344,
    label = "CH3CH2OH + HO2 <=> CH3CH2O + H2O2",
    kinetics = Arrhenius(
        A = (2.500e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (24000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = 14.6
entry(
    index = 345,
    label = "CH3CH2OH + CH3 <=> CH3CH2O + CH4",
    kinetics = Arrhenius(
        A = (2.040e+00, 'cm^3/(mol*s)'),
        n = 3.57,
        Ea = (7721.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = 17.8
entry(
    index = 346,
    label = "CH3CH2O + CO <=> C2H5 + CO2",
    kinetics = Arrhenius(
        A = (4.680e+02, 'cm^3/(mol*s)'),
        n = 3.16,
        Ea = (5380.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ZF Xu, J Park, MC Lin, JCP 120:6593 (2004).
# DH = 0.5
# CH3CH2OH+CH3OO=CH3CH2O+CH3OOH
# ## Missing Reaction
# CH3CH2OH+CH3OO=CH3CHOH+CH3OOH
# ## Missing Reaction
# CH3CH2OH+C2H5=CH2CH2OH+C2H6
# ## Missing Reaction
# CH3CH2OH+C2H5=CH3CHOH+C2H6
# ## Missing Reaction
entry(
    index = 347,
    label = "CH3CHOH + O2 <=> CH3CHO + HO2",
    kinetics = Arrhenius(
        A = (2.920e+11, 'cm^3/(mol*s)'),
        n = 0.385,
        Ea = (-1128.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = -35.7
# *** Fuel Radical + Radical
entry(
    index = 348,
    label = "CH3CHOH + H <=> CH3CHO + H2",
    kinetics = Arrhenius(
        A = (1.360e+09, 'cm^3/(mol*s)'),
        n = 1.29,
        Ea = (2824.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, RX Fernandes, Y Georgievskii, G Meloni, CA Taatjes, JA Miller, PCI 32:271 (2009).
# DH = -23.1
entry(
    index = 349,
    label = "CH3CHOH + H <=> CH2CHOH + H2",
    kinetics = Arrhenius(
        A = (3.140e+12, 'cm^3/(mol*s)'),
        n = 0.273,
        Ea = (-334.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ZF Xu, K Xu, MC Lin, JPCA 115:3509 (2011).
# DH = -78.4
entry(
    index = 350,
    label = "CH3CHOH + H <=> C2H4 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.230e+17, 'cm^3/(mol*s)'),
        n = -1.166,
        Ea = (284.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.190e+17, 'cm^3/(mol*s)'),
        n = -1.162,
        Ea = (266.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.850e+17, 'cm^3/(mol*s)'),
        n = -1.216,
        Ea = (386.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.590e+20, 'cm^3/(mol*s)'),
        n = -2.079,
        Ea = (3148.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.300e+23, 'cm^3/(mol*s)'),
        n = -2.996,
        Ea = (7954.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.650e+20, 'cm^3/(mol*s)'),
        n = -1.812,
        Ea = (9448.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJK - unpublished
# DH = -68.7

entry(
    index = 351,
    label = "CH3CHOH + H <=> CH3 + CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.380e+17, 'cm^3/(mol*s)'),
        n = -0.912,
        Ea = (3081.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.520e+17, 'cm^3/(mol*s)'),
        n = -0.923,
        Ea = (3116.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.470e+17, 'cm^3/(mol*s)'),
        n = -1.052,
        Ea = (3509.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.270e+20, 'cm^3/(mol*s)'),
        n = -1.795,
        Ea = (5893.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.980e+24, 'cm^3/(mol*s)'),
        n = -2.949,
        Ea = (10754.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.030e+23, 'cm^3/(mol*s)'),
        n = -2.527,
        Ea = (13636.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -84.1

entry(
    index = 352,
    label = "CH3CHOH + H <=> C2H5 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.040e+13, 'cm^3/(mol*s)'),
        n = 0.021,
        Ea = (4441.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (4.440e+13, 'cm^3/(mol*s)'),
        n = 0.01,
        Ea = (4476.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.060e+14, 'cm^3/(mol*s)'),
        n = -0.095,
        Ea = (4790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.650e+16, 'cm^3/(mol*s)'),
        n = -0.697,
        Ea = (6677.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.800e+20, 'cm^3/(mol*s)'),
        n = -1.943,
        Ea = (11331.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.270e+21, 'cm^3/(mol*s)'),
        n = -2.106,
        Ea = (15269.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -8.0

entry(
    index = 353,
    label = "CH3CHOH + O <=> CH3CHO + OH",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -1.0
entry(
    index = 354,
    label = "CH3CHOH + OH <=> CH3CHO + H2O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = -76.8
entry(
    index = 355,
    label = "CH3CHOH + HO2 <=> CH3CHO + H2O2",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -92.9
entry(
    index = 356,
    label = "CH3CHOH + HO2 <=> CH3CHO + OH + OH",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -61.2
entry(
    index = 357,
    label = "CH3CHOH + CH3 <=> CH3CHO + CH4",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = -12.3
entry(
    index = 358,
    label = "CH3 + CH3CHOH <=> CH3CHCH2 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.1, 0.25, 0.5, 0.75, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.850e+39, 'cm^3/(mol*s)'),
        n = -8.072,
        Ea = (13734.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (1.220e+40, 'cm^3/(mol*s)'),
        n = -8.217,
        Ea = (15035.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.330e+40, 'cm^3/(mol*s)'),
        n = -8.247,
        Ea = (16517.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.25 atm
        Arrhenius(
            A = (1.190e+40, 'cm^3/(mol*s)'),
        n = -8.123,
        Ea = (17412.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (4.800e+39, 'cm^3/(mol*s)'),
        n = -7.985,
        Ea = (17828.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.75 atm
        Arrhenius(
            A = (1.950e+39, 'cm^3/(mol*s)'),
        n = -7.856,
        Ea = (18067.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.620e+32, 'cm^3/(mol*s)'),
        n = -5.754,
        Ea = (18000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.130e+19, 'cm^3/(mol*s)'),
        n = -1.828,
        Ea = (14114.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -78.5

entry(
    index = 359,
    label = "CH2CH2OH + H <=> C2H5 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.600e+13, 'cm^3/(mol*s)'),
        n = 0.051,
        Ea = (4302.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (4.640e+13, 'cm^3/(mol*s)'),
        n = 0.021,
        Ea = (4392.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.370e+14, 'cm^3/(mol*s)'),
        n = -0.217,
        Ea = (5113.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.210e+17, 'cm^3/(mol*s)'),
        n = -1.158,
        Ea = (8193.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.580e+22, 'cm^3/(mol*s)'),
        n = -2.273,
        Ea = (13261.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.070e+19, 'cm^3/(mol*s)'),
        n = -1.51,
        Ea = (15534.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -74.4

entry(
    index = 360,
    label = "CH2CH2OH + O2 <=> OHCH2CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.500e+44, 'cm^3/(mol*s)'),
        n = -11.15,
        Ea = (5523.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm
        Arrhenius(
            A = (4.870e+42, 'cm^3/(mol*s)'),
        n = -10.34,
        Ea = (5913.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.420e+38, 'cm^3/(mol*s)'),
        n = -8.77,
        Ea = (5859.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.570e+32, 'cm^3/(mol*s)'),
        n = -6.58,
        Ea = (5046.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.220e+26, 'cm^3/(mol*s)'),
        n = -4.46,
        Ea = (3940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -8.3

entry(
    index = 361,
    label = "CH2CH2OH + O2 <=> CH2CHOH + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.300e+53, 'cm^3/(mol*s)'),
        n = -11.88,
        Ea = (35927.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 1)
        Arrhenius(
            A = (2.250e+10, 'cm^3/(mol*s)'),
        n = -0.15,
        Ea = (-791.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 2)
        Arrhenius(
            A = (4.960e+12, 'cm^3/(mol*s)'),
        n = -0.79,
        Ea = (877.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.800e+61, 'cm^3/(mol*s)'),
        n = -14.17,
        Ea = (43492.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (3.590e+13, 'cm^3/(mol*s)'),
        n = -0.88,
        Ea = (3074.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (6.020e+03, 'cm^3/(mol*s)'),
        n = -10.0,
        Ea = (199.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (4.380e+20, 'cm^3/(mol*s)'),
        n = -2.85,
        Ea = (8516.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (6.020e+03, 'cm^3/(mol*s)'),
        n = -10.0,
        Ea = (199.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.900e+30, 'cm^3/(mol*s)'),
        n = -5.51,
        Ea = (16616.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.020e+03, 'cm^3/(mol*s)'),
        n = -10.0,
        Ea = (199.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# J Zador, RX Fernandes, Y Georgievskii, G Meloni, CA Taatjes, JA Miller, PCI 32:271 (2009).
# DH = ??

entry(
    index = 362,
    label = "CH2CH2OH + O2 <=> CH2O + CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.570e+22, 'cm^3/(mol*s)'),
        n = -3.95,
        Ea = (1210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm
        Arrhenius(
            A = (1.420e+24, 'cm^3/(mol*s)'),
        n = -4.31,
        Ea = (2664.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.350e+24, 'cm^3/(mol*s)'),
        n = -4.36,
        Ea = (4396.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.970e+25, 'cm^3/(mol*s)'),
        n = -4.5,
        Ea = (6763.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.190e+29, 'cm^3/(mol*s)'),
        n = -5.44,
        Ea = (11323.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, RX Fernandes, Y Georgievskii, G Meloni, CA Taatjes, JA Miller, PCI 32:271 (2009).
# DH = -20.8

entry(
    index = 363,
    label = "CH2CH2OH + H <=> CH2CHOH + H2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, RX Fernandes, Y Georgievskii, G Meloni, CA Taatjes, JA Miller, PCI 32:271 (2009).
# DH = -38.5
entry(
    index = 364,
    label = "CH2CH2OH + H <=> C2H4 + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.670e+17, 'cm^3/(mol*s)'),
        n = -1.184,
        Ea = (334.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.560e+17, 'cm^3/(mol*s)'),
        n = -1.176,
        Ea = (299.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.660e+18, 'cm^3/(mol*s)'),
        n = -1.461,
        Ea = (1107.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.650e+22, 'cm^3/(mol*s)'),
        n = -2.599,
        Ea = (5235.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.500e+23, 'cm^3/(mol*s)'),
        n = -2.883,
        Ea = (9307.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.640e+16, 'cm^3/(mol*s)'),
        n = -0.716,
        Ea = (8767.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate.
# DH = -76.1

entry(
    index = 365,
    label = "CH2CHOH + HO2 <=> CH2CHO + H2O2",
    kinetics = Arrhenius(
        A = (1.600e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (16293.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -67.0
entry(
    index = 366,
    label = "CH2CHOH + HO2 <=> CH3CHO + HO2",
    kinetics = Arrhenius(
        A = (1.500e+05, 'cm^3/(mol*s)'),
        n = 1.67,
        Ea = (6810.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# M Altarawneh, AH Al-Muhtaseb, BZ Dlugogorski, EM Kennedy, JC Mackie, JCC 32:1725 (2011).
# DH = ??
entry(
    index = 367,
    label = "CH3CH2O + O2 <=> CH3CHO + HO2",
    kinetics = Arrhenius(
        A = (3.610e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1093.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# G da Silva, JW Bozzelli, CPL 483:25 (2009).
# DH = ??
entry(
    index = 368,
    label = "CH3CH2O + H <=> CH3CHO + H2",
    kinetics = Arrhenius(
        A = (7.470e+09, 'cm^3/(mol*s)'),
        n = 1.15,
        Ea = (674.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Atkinson, DL Baulch, RA Cox, RF Hampson, JA Kerr, MJ Rossi, J Troe, JPCRD 26:521 (1997).
# DH = -33.7
entry(
    index = 369,
    label = "CH3CH2O + H <=> C2H4 + H2O",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ZF Xu, K Xu, MC Lin, JPCA 115:3509 (2011).
# DH = -89.0
entry(
    index = 370,
    label = "CH3CH2O + H <=> CH3 + CH2OH",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = -94.7
entry(
    index = 371,
    label = "CH3CH2O + OH <=> CH3CHO + H2O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = -18.7
entry(
    index = 372,
    label = "CH3CH2OH + O <=> CH3CH2O + OH",
    kinetics = Arrhenius(
        A = (1.460e-03, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (1727.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, IJCK 31:183 (1999).
# DH = -103.5
entry(
    index = 373,
    label = "CH3CH2OH + O2 <=> CH3CHOH + HO2",
    kinetics = Arrhenius(
        A = (2.410e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (44052.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CW Wu, YP Lee, SC Xu, MC Lin, JPCA 111:6693 (2007).
# DH = 2.3
entry(
    index = 374,
    label = "CH3CH2OH + O2 <=> CH2CH2OH + HO2",
    kinetics = Arrhenius(
        A = (3.610e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (47748.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 45.3
entry(
    index = 375,
    label = "OHCH2CH2OO <=> CH2CHOH + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.020e+09, 's^-1'),
        n = -1.01,
        Ea = (13160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm
        Arrhenius(
            A = (2.130e+09, 's^-1'),
        n = -0.81,
        Ea = (13598.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.380e+10, 's^-1'),
        n = -0.78,
        Ea = (14836.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.460e+11, 's^-1'),
        n = -1.01,
        Ea = (17045.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.820e+14, 's^-1'),
        n = -1.51,
        Ea = (20561.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 52.7
# *****************************************************************************
#    OHCH2CH2OOH subset                                                       *
# *****************************************************************************
# Fuel Radicals:  OHCH2CH2OO
# New Radicals Formed:
# New Fuels:

entry(
    index = 376,
    label = "OHCH2CH2OO <=> CH2O + CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.013, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.610e+13, 's^-1'),
        n = -1.9,
        Ea = (14338.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm
        Arrhenius(
            A = (2.150e+14, 's^-1'),
        n = -1.92,
        Ea = (14870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.970e+15, 's^-1'),
        n = -2.03,
        Ea = (15913.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.010e+16, 's^-1'),
        n = -2.26,
        Ea = (17552.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.780e+18, 's^-1'),
        n = -2.6,
        Ea = (19972.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, RX Fernandes, Y Georgievskii, G Meloni, CA Taatjes, JA Miller, PCI 32:271 (2009).
# DH = ??

entry(
    index = 377,
    label = "CH3CH2OO <=> CH2CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.150e+31, 's^-1'),
        n = -8.25,
        Ea = (29360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (3.500e+30, 's^-1'),
        n = -7.88,
        Ea = (29330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (1.520e+29, 's^-1'),
        n = -7.37,
        Ea = (29210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (3.470e+27, 's^-1'),
        n = -6.77,
        Ea = (29000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (3.570e+25, 's^-1'),
        n = -6.04,
        Ea = (28780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.600e+24, 's^-1'),
        n = -5.51,
        Ea = (28800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (1.440e+21, 's^-1'),
        n = -4.4,
        Ea = (28410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.850e+19, 's^-1'),
        n = -3.73,
        Ea = (28490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (1.270e+17, 's^-1'),
        n = -2.81,
        Ea = (28500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.270e+14, 's^-1'),
        n = -1.9,
        Ea = (28470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (4.670e+13, 's^-1'),
        n = -1.4,
        Ea = (28970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.210e+12, 's^-1'),
        n = -0.92,
        Ea = (29380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.870e+08, 's^-1'),
        n = 0.57,
        Ea = (28590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, RX Fernandes, Y Georgievskii, G Meloni, CA Taatjes, JA Miller, PCI 32:271 (2009).
# DH = ??
# *****************************************************************************
#    CH3CH2OOH subset                                                         *
# *****************************************************************************
# Fuel Radicals:  CH3CH2OO, CH2CH2OOH
# New Radicals Formed:
# New Fuels:
# Only partially treated
# *** Fuel Decomposition
# CH3CH2OOH=CH3CH2O+OH
# ## Missing Reaction
# CH3CH2OOH=C2H4+H2O
# ## Missing Reaction
# CH3CH2OOH=CH3+CH2OH
# ## Missing Reaction
# CH3CH2OOH=C2H5+OH
# ## Missing Reaction
# *** Fuel Radical Decomposition

entry(
    index = 378,
    label = "CH3CH2OO <=> C2H4 + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.910e+46, 's^-1'),
        n = -11.85,
        Ea = (36440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (4.210e+46, 's^-1'),
        n = -11.88,
        Ea = (36820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (3.630e+46, 's^-1'),
        n = -11.77,
        Ea = (37100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.700e+46, 's^-1'),
        n = -11.58,
        Ea = (37330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (4.360e+45, 's^-1'),
        n = -11.28,
        Ea = (37570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (8.120e+44, 's^-1'),
        n = -10.94,
        Ea = (37780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (4.610e+43, 's^-1'),
        n = -10.43,
        Ea = (37910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.690e+41, 's^-1'),
        n = -9.77,
        Ea = (37860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (8.650e+39, 's^-1'),
        n = -9.01,
        Ea = (37780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.240e+36, 's^-1'),
        n = -7.95,
        Ea = (37240.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (4.300e+33, 's^-1'),
        n = -6.84,
        Ea = (36660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.920e+30, 's^-1'),
        n = -5.71,
        Ea = (35910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.580e+26, 's^-1'),
        n = -4.37,
        Ea = (34840.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = 17.0

entry(
    index = 379,
    label = "CH3CH2OO <=> c-CH2CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.000e+49, 's^-1'),
        n = -13.32,
        Ea = (38820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (1.660e+50, 's^-1'),
        n = -13.52,
        Ea = (39510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (6.610e+50, 's^-1'),
        n = -13.62,
        Ea = (40180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (3.890e+48, 's^-1'),
        n = -12.85,
        Ea = (39830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (7.630e+48, 's^-1'),
        n = -12.82,
        Ea = (40620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (9.690e+46, 's^-1'),
        n = -12.11,
        Ea = (40640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (9.940e+46, 's^-1'),
        n = -11.94,
        Ea = (41670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.250e+45, 's^-1'),
        n = -11.2,
        Ea = (42020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (1.480e+44, 's^-1'),
        n = -10.71,
        Ea = (43040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.030e+42, 's^-1'),
        n = -9.86,
        Ea = (43640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (2.460e+39, 's^-1'),
        n = -8.87,
        Ea = (44290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.850e+36, 's^-1'),
        n = -7.75,
        Ea = (44660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (2.450e+31, 's^-1'),
        n = -6.1,
        Ea = (44560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = 19.4

entry(
    index = 380,
    label = "CH2CH2OOH <=> C2H4 + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.090e+18, 's^-1'),
        n = -4.08,
        Ea = (11730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (9.250e+18, 's^-1'),
        n = -4.31,
        Ea = (12390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (1.020e+21, 's^-1'),
        n = -4.76,
        Ea = (13430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (5.100e+21, 's^-1'),
        n = -4.75,
        Ea = (13900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (7.700e+25, 's^-1'),
        n = -5.82,
        Ea = (15440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.440e+27, 's^-1'),
        n = -5.99,
        Ea = (16150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (3.630e+30, 's^-1'),
        n = -6.81,
        Ea = (17690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.160e+31, 's^-1'),
        n = -6.88,
        Ea = (18540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (1.470e+32, 's^-1'),
        n = -6.85,
        Ea = (19480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.160e+31, 's^-1'),
        n = -6.55,
        Ea = (20100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (8.820e+29, 's^-1'),
        n = -5.75,
        Ea = (20260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.520e+27, 's^-1'),
        n = -4.8,
        Ea = (20070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (7.520e+23, 's^-1'),
        n = -3.57,
        Ea = (19460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = 0.9

entry(
    index = 381,
    label = "CH2CH2OOH <=> c-CH2CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.200e+24, 's^-1'),
        n = -5.76,
        Ea = (12410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (7.310e+26, 's^-1'),
        n = -6.39,
        Ea = (13340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (1.260e+29, 's^-1'),
        n = -6.91,
        Ea = (14240.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.680e+28, 's^-1'),
        n = -6.45,
        Ea = (14230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (2.190e+30, 's^-1'),
        n = -6.94,
        Ea = (15220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.400e+30, 's^-1'),
        n = -6.7,
        Ea = (15540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (9.950e+31, 's^-1'),
        n = -7.1,
        Ea = (16610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.330e+31, 's^-1'),
        n = -6.87,
        Ea = (17080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (2.010e+31, 's^-1'),
        n = -6.53,
        Ea = (17550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.190e+30, 's^-1'),
        n = -6.0,
        Ea = (17750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (4.000e+27, 's^-1'),
        n = -5.08,
        Ea = (17550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.840e+24, 's^-1'),
        n = -4.12,
        Ea = (17130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (3.180e+21, 's^-1'),
        n = -2.97,
        Ea = (16400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = 2.4

entry(
    index = 382,
    label = "C2H3 + H <=> C2H4",
    kinetics = PDepArrhenius(
        pressures = ([0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.150e+25, 'cm^3/(mol*s)'),
        n = -5.453,
        Ea = (15568.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (1.360e+27, 'cm^3/(mol*s)'),
        n = -5.778,
        Ea = (11335.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.910e+29, 'cm^3/(mol*s)'),
        n = -6.328,
        Ea = (8440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (1.510e+33, 'cm^3/(mol*s)'),
        n = -7.037,
        Ea = (6990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.790e+35, 'cm^3/(mol*s)'),
        n = -7.466,
        Ea = (6833.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (1.010e+37, 'cm^3/(mol*s)'),
        n = -7.605,
        Ea = (7273.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.600e+37, 'cm^3/(mol*s)'),
        n = -7.441,
        Ea = (7775.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (1.830e+36, 'cm^3/(mol*s)'),
        n = -6.961,
        Ea = (8066.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.210e+34, 'cm^3/(mol*s)'),
        n = -6.25,
        Ea = (7882.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (2.030e+31, 'cm^3/(mol*s)'),
        n = -5.235,
        Ea = (7124.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = 5.9
# CH2CH2OOH=CH3CHO+OH
# ## Missing Reaction
# Fuel Radical + Stable
# CH3CH2OO+C2H6=CH3CH2OOH+C2H5
# ## Missing Reaction
# CH3CH2OO+HO2=CH3CH2OOH+O2
# ## Missing Reaction
# CH3CH2OO+H2=CH3CH2OOH+H
# ## Missing Reaction
# CH3CH2OO+CH2O=CH3CH2OOH+HCO
# ## Missing Reaction
# CH3CH2OO+CH4=CH3CH2OOH+CH3
# ## Missing Reaction
# CH3CH2OO+CH3OH=CH3CH2OOH+CH2OH
# ## Missing Reaction
# *****************************************************************************
#    C2H4 subset                                                              *
# *****************************************************************************
# Fuel Radicals: C2H3
# New Radicals Formed: CH2CHOO, CH2CHCH2, CH2CHCHO, CHCHO
# New Fuels: CH2CCH2
# *** Fuel Decomposition

entry(
    index = 383,
    label = "C2H4 <=> CH2C + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.490e+45, 's^-1'),
        n = -9.908,
        Ea = (106920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (3.230e+45, 's^-1'),
        n = -9.67,
        Ea = (107470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (9.680e+44, 's^-1'),
        n = -9.384,
        Ea = (107910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (1.220e+44, 's^-1'),
        n = -8.982,
        Ea = (108290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.280e+42, 's^-1'),
        n = -8.488,
        Ea = (108420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (8.300e+40, 's^-1'),
        n = -7.822,
        Ea = (108300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.900e+38, 's^-1'),
        n = -7.051,
        Ea = (107780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (3.240e+35, 's^-1'),
        n = -6.07,
        Ea = (106800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.620e+32, 's^-1'),
        n = -5.051,
        Ea = (105510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (2.110e+28, 's^-1'),
        n = -3.873,
        Ea = (103790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein - unpublished
# DH = -109.2

entry(
    index = 384,
    label = "C2H4 + O <=> CH3 + HCO",
    kinetics = Arrhenius(
        A = (5.880e+17, 'cm^3/(mol*s)'),
        n = -1.717,
        Ea = (2893.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished
# DH = 84.0
# *** Fuel + Radical
entry(
    index = 385,
    label = "C2H4 + O <=> CH3CO + H",
    kinetics = Arrhenius(
        A = (8.660e+12, 'cm^3/(mol*s)'),
        n = -0.484,
        Ea = (1957.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# X Li, AW Jasper, J Zador, JA Miller, SJ Klippenstein, PCI 36:219 (2017).
# DH = -27.9
entry(
    index = 386,
    label = "C2H4 + O <=> CH2CHO + H",
    kinetics = Arrhenius(
        A = (9.150e+09, 'cm^3/(mol*s)'),
        n = 0.948,
        Ea = (1724.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# X Li, AW Jasper, J Zador, JA Miller, SJ Klippenstein, PCI 36:219 (2017).
# DH = -22.9
entry(
    index = 387,
    label = "C2H4 + O <=> CH2 + CH2O",
    kinetics = Arrhenius(
        A = (5.770e+06, 'cm^3/(mol*s)'),
        n = 1.991,
        Ea = (2859.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# X Li, AW Jasper, J Zador, JA Miller, SJ Klippenstein, PCI 36:219 (2017).
# DH = -16.3
entry(
    index = 388,
    label = "C2H4 + O <=> CH2CO + H2",
    kinetics = Arrhenius(
        A = (1.120e+17, 'cm^3/(mol*s)'),
        n = -1.831,
        Ea = (3179.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# X Li, AW Jasper, J Zador, JA Miller, SJ Klippenstein, PCI 36:219 (2017).
# DH = -5.3
entry(
    index = 389,
    label = "OH + C2H4 <=> H2O + C2H3",
    kinetics = Arrhenius(
        A = (1.310e-01, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# X Li, AW Jasper, J Zador, JA Miller, SJ Klippenstein, PCI 36:219 (2017).
# DH = -84.3
entry(
    index = 390,
    label = "OH + C2H4 <=> CH3 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.350e+00, 'cm^3/(mol*s)'),
        n = 2.92,
        Ea = (-1733.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.190e+01, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (-1172.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (5.550e+02, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (-181.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.780e+05, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (2061.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.370e+09, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (6007.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.760e+13, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (11455.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -8.6

entry(
    index = 391,
    label = "OH + C2H4 <=> CH3CHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.370e-07, 'cm^3/(mol*s)'),
        n = 5.3,
        Ea = (-2051.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (8.730e-05, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (-618.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (4.030e-01, 'cm^3/(mol*s)'),
        n = 3.54,
        Ea = (1882.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.380e-02, 'cm^3/(mol*s)'),
        n = 3.91,
        Ea = (1723.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.250e+08, 'cm^3/(mol*s)'),
        n = 1.01,
        Ea = (10507.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.800e+09, 'cm^3/(mol*s)'),
        n = 0.81,
        Ea = (13867.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -12.8

entry(
    index = 392,
    label = "C2H4 + HO2 <=> c-CH2CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.030e+04, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (12050.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0001 atm
        Arrhenius(
            A = (1.070e+04, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (12060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0003 atm
        Arrhenius(
            A = (1.090e+04, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (12070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.150e+04, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (12080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (1.340e+04, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (12120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.010e+04, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (12230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (5.970e+04, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (12530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.150e+05, 'cm^3/(mol*s)'),
        n = 1.96,
        Ea = (13090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (1.320e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (14120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.330e+08, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (15470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (1.080e+11, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (17220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.120e+12, 'cm^3/(mol*s)'),
        n = 0.11,
        Ea = (18750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (2.220e+12, 'cm^3/(mol*s)'),
        n = 0.16,
        Ea = (19980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
# DH = -8.8

entry(
    index = 393,
    label = "CH3CHCHO <=> C2H4 + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.290e+53, 's^-1'),
        n = -13.16,
        Ea = (53130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (3.110e+35, 's^-1'),
        n = -8.14,
        Ea = (42500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (3.440e+53, 's^-1'),
        n = -12.82,
        Ea = (54820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.210e+36, 's^-1'),
        n = -8.06,
        Ea = (44050.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (1.180e+53, 's^-1'),
        n = -12.37,
        Ea = (56880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (2.690e+32, 's^-1'),
        n = -6.63,
        Ea = (44760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (6.350e+49, 's^-1'),
        n = -11.06,
        Ea = (58330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (2.180e+29, 's^-1'),
        n = -5.57,
        Ea = (45310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (1.250e+47, 's^-1'),
        n = -9.92,
        Ea = (61260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (5.080e+21, 's^-1'),
        n = -3.11,
        Ea = (44540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.080e+46, 's^-1'),
        n = -9.23,
        Ea = (67030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (8.620e+10, 's^-1'),
        n = 0.34,
        Ea = (42910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# SJ Klippenstein, PCI 36:77 (2017).
# DH = -18.5

entry(
    index = 394,
    label = "CH2CH2CHO <=> C2H4 + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.590e+89, 's^-1'),
        n = -25.32,
        Ea = (48450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (9.330e+36, 's^-1'),
        n = -8.67,
        Ea = (28850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.090e+76, 's^-1'),
        n = -20.65,
        Ea = (45250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (3.100e+34, 's^-1'),
        n = -7.58,
        Ea = (28900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (4.020e+58, 's^-1'),
        n = -14.65,
        Ea = (40580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (1.450e+30, 's^-1'),
        n = -5.98,
        Ea = (28290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (3.880e+50, 's^-1'),
        n = -11.77,
        Ea = (39680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (2.290e+25, 's^-1'),
        n = -4.29,
        Ea = (27450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (4.160e+39, 's^-1'),
        n = -8.09,
        Ea = (37310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (7.830e+23, 's^-1'),
        n = -3.76,
        Ea = (27220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (2.450e+30, 's^-1'),
        n = -5.13,
        Ea = (35070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (5.820e+16, 's^-1'),
        n = -1.34,
        Ea = (25670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 27.5

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 16.2

entry(
    index = 396,
    label = "CH2OCHCH2 <=> C2H4 + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.230e+26, 's^-1'),
        n = -5.84,
        Ea = (19357.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.320e+29, 's^-1'),
        n = -6.21,
        Ea = (21294.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.470e+32, 's^-1'),
        n = -6.96,
        Ea = (24197.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.440e+36, 's^-1'),
        n = -7.76,
        Ea = (28008.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.720e+37, 's^-1'),
        n = -8.02,
        Ea = (32395.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.430e+31, 's^-1'),
        n = -5.81,
        Ea = (34296.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (3.730e+14, 's^-1'),
        n = -0.726,
        Ea = (32008.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 23.5

entry(
    index = 397,
    label = "CH2CHCH2O <=> C2H4 + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.620e+16, 's^-1'),
        n = -2.84,
        Ea = (13197.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.260e+20, 's^-1'),
        n = -3.53,
        Ea = (15469.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.130e+21, 's^-1'),
        n = -3.64,
        Ea = (16584.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.070e+24, 's^-1'),
        n = -4.16,
        Ea = (18985.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.420e+25, 's^-1'),
        n = -4.4,
        Ea = (22383.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.860e+21, 's^-1'),
        n = -2.73,
        Ea = (23659.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (4.750e+08, 's^-1'),
        n = 1.14,
        Ea = (20922.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 0.0

entry(
    index = 398,
    label = "CH3 + C2H4 <=> CH3CH2CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.670e+48, 'cm^3/(mol*s)'),
        n = -12.541,
        Ea = (18206.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 1)
        Arrhenius(
            A = (1.120e+43, 'cm^3/(mol*s)'),
        n = -11.304,
        Ea = (13080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 2)
        Arrhenius(
            A = (1.060e+49, 'cm^3/(mol*s)'),
        n = -12.035,
        Ea = (20001.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 1)
        Arrhenius(
            A = (7.290e+39, 'cm^3/(mol*s)'),
        n = -9.88,
        Ea = (13164.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 2)
        Arrhenius(
            A = (7.670e+47, 'cm^3/(mol*s)'),
        n = -11.169,
        Ea = (22366.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.600e+33, 'cm^3/(mol*s)'),
        n = -7.462,
        Ea = (12416.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.810e+45, 'cm^3/(mol*s)'),
        n = -10.03,
        Ea = (23769.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (3.850e+27, 'cm^3/(mol*s)'),
        n = -5.385,
        Ea = (11455.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.040e+40, 'cm^3/(mol*s)'),
        n = -8.254,
        Ea = (24214.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.660e+21, 'cm^3/(mol*s)'),
        n = -3.175,
        Ea = (10241.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -2.7

entry(
    index = 399,
    label = "CH2(S) + C2H4 <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.820e+57, 'cm^3/(mol*s)'),
        n = -14.34,
        Ea = (17091.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.150e+45, 'cm^3/(mol*s)'),
        n = -11.13,
        Ea = (6145.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.840e+59, 'cm^3/(mol*s)'),
        n = -14.36,
        Ea = (18427.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.830e+45, 'cm^3/(mol*s)'),
        n = -10.68,
        Ea = (6639.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.130e+58, 'cm^3/(mol*s)'),
        n = -13.55,
        Ea = (20355.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.300e+40, 'cm^3/(mol*s)'),
        n = -8.77,
        Ea = (5864.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (8.480e+52, 'cm^3/(mol*s)'),
        n = -11.63,
        Ea = (20677.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.270e+32, 'cm^3/(mol*s)'),
        n = -6.14,
        Ea = (4318.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.080e+47, 'cm^3/(mol*s)'),
        n = -9.85,
        Ea = (22055.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.280e+24, 'cm^3/(mol*s)'),
        n = -3.49,
        Ea = (2530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = -22.0

entry(
    index = 400,
    label = "CH2(S) + C2H4 <=> c-CH2CH2CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.450e+51, 'cm^3/(mol*s)'),
        n = -13.12,
        Ea = (14153.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (6.160e+40, 'cm^3/(mol*s)'),
        n = -10.5,
        Ea = (5428.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.380e+54, 'cm^3/(mol*s)'),
        n = -13.55,
        Ea = (16473.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.930e+41, 'cm^3/(mol*s)'),
        n = -10.3,
        Ea = (6189.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.350e+54, 'cm^3/(mol*s)'),
        n = -12.97,
        Ea = (18862.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.810e+37, 'cm^3/(mol*s)'),
        n = -8.55,
        Ea = (5521.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.730e+47, 'cm^3/(mol*s)'),
        n = -10.78,
        Ea = (14232.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.260e+37, 'cm^3/(mol*s)'),
        n = -8.32,
        Ea = (4770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.710e+50, 'cm^3/(mol*s)'),
        n = -11.22,
        Ea = (16720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.680e+35, 'cm^3/(mol*s)'),
        n = -7.37,
        Ea = (4689.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -108.7

entry(
    index = 401,
    label = "CH2(S) + C2H4 <=> CH2CHCH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.210e+19, 'cm^3/(mol*s)'),
        n = -2.07,
        Ea = (1145.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.080e+07, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (-3175.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (2.270e+21, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (2648.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.370e+05, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (-3799.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.440e+35, 'cm^3/(mol*s)'),
        n = -6.55,
        Ea = (13894.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.900e+14, 'cm^3/(mol*s)'),
        n = -0.42,
        Ea = (1238.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.180e+28, 'cm^3/(mol*s)'),
        n = -4.09,
        Ea = (14013.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.450e+10, 'cm^3/(mol*s)'),
        n = 0.67,
        Ea = (751.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.510e+26, 'cm^3/(mol*s)'),
        n = -3.58,
        Ea = (18927.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.810e+02, 'cm^3/(mol*s)'),
        n = 2.97,
        Ea = (-746.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -99.9

entry(
    index = 402,
    label = "CH2(S) + C2H4 <=> CH3 + C2H3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.770e+19, 'cm^3/(mol*s)'),
        n = -1.95,
        Ea = (6787.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.300e+12, 'cm^3/(mol*s)'),
        n = 0.19,
        Ea = (-110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.680e+19, 'cm^3/(mol*s)'),
        n = -1.8,
        Ea = (4310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.260e+11, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (48.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.160e+24, 'cm^3/(mol*s)'),
        n = -3.19,
        Ea = (9759.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.920e+09, 'cm^3/(mol*s)'),
        n = 1.02,
        Ea = (600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.890e+24, 'cm^3/(mol*s)'),
        n = -3.08,
        Ea = (13894.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.470e+08, 'cm^3/(mol*s)'),
        n = 1.33,
        Ea = (1228.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (7.360e+29, 'cm^3/(mol*s)'),
        n = -4.28,
        Ea = (23849.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (8.110e+10, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (5507.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -22.4

entry(
    index = 403,
    label = "CH2CH2CH2OH <=> C2H4 + CH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.960e+22, 's^-1'),
        n = -4.59,
        Ea = (30200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.630e+32, 's^-1'),
        n = -6.8,
        Ea = (37100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.290e+38, 's^-1'),
        n = -8.33,
        Ea = (43300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.080e+42, 's^-1'),
        n = -9.08,
        Ea = (48600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.610e+37, 's^-1'),
        n = -7.15,
        Ea = (48200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -9.2

entry(
    index = 404,
    label = "CH2C + C2H4 <=> CH2CHCHCH2",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 19.3
entry(
    index = 405,
    label = "H + C2H2 <=> C2H3",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(17100000000.0, 'cm^3/(mol*s)'), n=1.266, Ea=(2709.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(6.35e+31, 'cm^6/(mol^2*s)'), n=-4.664, Ea=(3780.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.78784,
        T3 = (-10210.0, 'K'),
        T1 = (1e-30, 'K'),
        efficiencies = { 'N#N': 1.2, '[C-]#[O+]': 1.5, '[H][H]': 2.0, 'O=C=O': 3.0, 'O': 10.0 }
    ),
)

entry(
    index = 406,
    label = "C2H4 + H <=> C2H3 + H2",
    kinetics = Arrhenius(
        A = (2.350e+02, 'cm^3/(mol*s)'),
        n = 3.62,
        Ea = (11266.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein, PCCP 6:1192 (2004).
# DH = -34.3
# *** Fuel Radical + Stable
entry(
    index = 407,
    label = "C2H3 + H2O2 <=> C2H4 + HO2",
    kinetics = Arrhenius(
        A = (1.210e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-596.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 5.9
entry(
    index = 408,
    label = "C2H4 + CH3 <=> CH4 + C2H3",
    kinetics = Arrhenius(
        A = (9.760e+02, 'cm^3/(mol*s)'),
        n = 2.947,
        Ea = (15148.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -23.1
entry(
    index = 409,
    label = "C2H4 + CH3 <=> CH4 + C2H3",
    kinetics = Arrhenius(
        A = (8.130e-05, 'cm^3/(mol*s)'),
        n = 4.417,
        Ea = (8836.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 410,
    label = "C2H3 + CH2O <=> C2H4 + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.110e+07, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (1807.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (2.470e+07, 'cm^3/(mol*s)'),
        n = 0.993,
        Ea = (1995.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.470e+08, 'cm^3/(mol*s)'),
        n = 0.704,
        Ea = (2596.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.420e+10, 'cm^3/(mol*s)'),
        n = 0.209,
        Ea = (3934.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.450e+13, 'cm^3/(mol*s)'),
        n = -0.726,
        Ea = (6944.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.310e+14, 'cm^3/(mol*s)'),
        n = -0.866,
        Ea = (10966.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (1.650e+01, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (9400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = 5.8

entry(
    index = 411,
    label = "C2H3 + CH2O <=> CH2CHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.600e+04, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (1510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (5.130e+04, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (1675.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.990e+05, 'cm^3/(mol*s)'),
        n = 1.91,
        Ea = (2218.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.750e+07, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (3428.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.350e+09, 'cm^3/(mol*s)'),
        n = 0.933,
        Ea = (5173.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.240e+11, 'cm^3/(mol*s)'),
        n = 0.357,
        Ea = (8001.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (6.010e+05, 'cm^3/(mol*s)'),
        n = 2.09,
        Ea = (7896.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -22.5

entry(
    index = 412,
    label = "CH2CH2CHO <=> C2H3 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.890e-69, 's^-1'),
        n = 21.5,
        Ea = (2638.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (5.340e-33, 's^-1'),
        n = 11.1,
        Ea = (16749.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.110e+26, 's^-1'),
        n = -6.01,
        Ea = (44117.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.040e+35, 's^-1'),
        n = -8.31,
        Ea = (46920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.520e+40, 's^-1'),
        n = -9.19,
        Ea = (50509.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.850e+35, 's^-1'),
        n = -7.18,
        Ea = (52038.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (1.930e+19, 's^-1'),
        n = -1.94,
        Ea = (48440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -8.3

entry(
    index = 413,
    label = "CH2OCHCH2 <=> C2H3 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.300e+09, 's^-1'),
        n = -0.638,
        Ea = (19748.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (3.360e+21, 's^-1'),
        n = -3.9,
        Ea = (23945.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.910e+29, 's^-1'),
        n = -5.9,
        Ea = (27250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.830e+34, 's^-1'),
        n = -6.94,
        Ea = (30690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.720e+33, 's^-1'),
        n = -6.5,
        Ea = (33002.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.680e+27, 's^-1'),
        n = -4.26,
        Ea = (33306.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (8.810e+14, 's^-1'),
        n = -0.326,
        Ea = (31553.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = 38.7

entry(
    index = 414,
    label = "CH2CHCH2O <=> C2H3 + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.260e+06, 's^-1'),
        n = 0.182,
        Ea = (17815.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (6.970e+16, 's^-1'),
        n = -2.5,
        Ea = (20879.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.640e+23, 's^-1'),
        n = -4.23,
        Ea = (23565.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.070e+26, 's^-1'),
        n = -4.56,
        Ea = (24623.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.500e+29, 's^-1'),
        n = -5.37,
        Ea = (26645.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.630e+31, 's^-1'),
        n = -5.59,
        Ea = (28915.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (8.520e+25, 's^-1'),
        n = -3.61,
        Ea = (27863.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = 22.5

entry(
    index = 415,
    label = "C2H3 + O2 <=> CH2CHOO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.550e+24, 'cm^3/(mol*s)'),
        n = -5.45,
        Ea = (9662.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.780e-09, 'cm^3/(mol*s)'),
        n = 4.15,
        Ea = (-4707.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.480e+56, 'cm^3/(mol*s)'),
        n = -15.01,
        Ea = (19160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.360e+22, 'cm^3/(mol*s)'),
        n = -4.52,
        Ea = (2839.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.250e+64, 'cm^3/(mol*s)'),
        n = -16.97,
        Ea = (21290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (2.000e+26, 'cm^3/(mol*s)'),
        n = -5.43,
        Ea = (2725.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.340e+61, 'cm^3/(mol*s)'),
        n = -15.79,
        Ea = (20150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (6.130e+28, 'cm^3/(mol*s)'),
        n = -5.89,
        Ea = (3154.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.340e+53, 'cm^3/(mol*s)'),
        n = -13.11,
        Ea = (17300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (2.140e+29, 'cm^3/(mol*s)'),
        n = -5.8,
        Ea = (3520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (4.160e+48, 'cm^3/(mol*s)'),
        n = -11.21,
        Ea = (16000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (3.480e+28, 'cm^3/(mol*s)'),
        n = -5.37,
        Ea = (3636.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.330e+43, 'cm^3/(mol*s)'),
        n = -9.38,
        Ea = (14810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (3.320e+27, 'cm^3/(mol*s)'),
        n = -4.95,
        Ea = (3610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (3.410e+39, 'cm^3/(mol*s)'),
        n = -8.04,
        Ea = (14360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.030e+27, 'cm^3/(mol*s)'),
        n = -4.72,
        Ea = (3680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = 19.8
# *** Fuel Radical + Radical

entry(
    index = 416,
    label = "C2H3 + O2 <=> CO2 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.370e+35, 'cm^3/(mol*s)'),
        n = -7.76,
        Ea = (12630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (6.270e+13, 'cm^3/(mol*s)'),
        n = -1.16,
        Ea = (406.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.730e+35, 'cm^3/(mol*s)'),
        n = -7.72,
        Ea = (12520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.240e+13, 'cm^3/(mol*s)'),
        n = -1.16,
        Ea = (401.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.470e+34, 'cm^3/(mol*s)'),
        n = -7.55,
        Ea = (12140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (6.120e+13, 'cm^3/(mol*s)'),
        n = -1.16,
        Ea = (397.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (7.250e+31, 'cm^3/(mol*s)'),
        n = -6.7,
        Ea = (10440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (5.320e+13, 'cm^3/(mol*s)'),
        n = -1.14,
        Ea = (447.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.630e+35, 'cm^3/(mol*s)'),
        n = -7.75,
        Ea = (12830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.450e+14, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (988.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (2.090e+35, 'cm^3/(mol*s)'),
        n = -7.53,
        Ea = (14050.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (5.020e+13, 'cm^3/(mol*s)'),
        n = -1.11,
        Ea = (1409.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.840e+18, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (5408.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.400e+70, 'cm^3/(mol*s)'),
        n = -20.11,
        Ea = (15430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.210e+32, 'cm^3/(mol*s)'),
        n = -6.32,
        Ea = (16190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (9.210e+08, 'cm^3/(mol*s)'),
        n = 0.25,
        Ea = (855.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -43.5

entry(
    index = 417,
    label = "C2H3 + O2 <=> CO + CH3O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.190e+18, 'cm^3/(mol*s)'),
        n = -2.66,
        Ea = (3201.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.290e+09, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (-1717.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (4.060e+14, 'cm^3/(mol*s)'),
        n = -1.32,
        Ea = (886.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (5.990e+11, 'cm^3/(mol*s)'),
        n = -2.93,
        Ea = (-9564.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.340e+14, 'cm^3/(mol*s)'),
        n = -1.33,
        Ea = (900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (2.910e+11, 'cm^3/(mol*s)'),
        n = -2.93,
        Ea = (-10120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (1.030e+11, 'cm^3/(mol*s)'),
        n = -0.33,
        Ea = (-748.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (5.770e+21, 'cm^3/(mol*s)'),
        n = -3.54,
        Ea = (4772.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.890e+12, 'cm^3/(mol*s)'),
        n = -3.0,
        Ea = (-8995.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (4.990e+15, 'cm^3/(mol*s)'),
        n = -1.62,
        Ea = (1849.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.930e+24, 'cm^3/(mol*s)'),
        n = -5.63,
        Ea = (2.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (9.330e+16, 'cm^3/(mol*s)'),
        n = -1.96,
        Ea = (3324.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.100e+18, 'cm^3/(mol*s)'),
        n = -2.22,
        Ea = (5178.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.020e+72, 'cm^3/(mol*s)'),
        n = -20.69,
        Ea = (15860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (5.790e+32, 'cm^3/(mol*s)'),
        n = -6.45,
        Ea = (16810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.100e+09, 'cm^3/(mol*s)'),
        n = 0.31,
        Ea = (1024.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -130.0

entry(
    index = 418,
    label = "C2H3 + O2 <=> CH2O + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.770e+36, 'cm^3/(mol*s)'),
        n = -7.6,
        Ea = (12640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (5.040e+15, 'cm^3/(mol*s)'),
        n = -1.28,
        Ea = (515.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (2.700e+36, 'cm^3/(mol*s)'),
        n = -7.6,
        Ea = (12610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (5.100e+15, 'cm^3/(mol*s)'),
        n = -1.28,
        Ea = (513.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.170e+36, 'cm^3/(mol*s)'),
        n = -7.57,
        Ea = (12490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (5.340e+15, 'cm^3/(mol*s)'),
        n = -1.29,
        Ea = (521.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.030e+35, 'cm^3/(mol*s)'),
        n = -7.32,
        Ea = (11820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (6.750e+15, 'cm^3/(mol*s)'),
        n = -1.31,
        Ea = (646.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.590e+36, 'cm^3/(mol*s)'),
        n = -7.47,
        Ea = (12460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.050e+16, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (1066.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (5.760e+35, 'cm^3/(mol*s)'),
        n = -7.2,
        Ea = (13430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.840e+15, 'cm^3/(mol*s)'),
        n = -1.18,
        Ea = (1429.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.540e+20, 'cm^3/(mol*s)'),
        n = -2.57,
        Ea = (5578.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.140e+69, 'cm^3/(mol*s)'),
        n = -19.23,
        Ea = (14760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (3.030e+33, 'cm^3/(mol*s)'),
        n = -6.28,
        Ea = (16000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.680e+10, 'cm^3/(mol*s)'),
        n = 0.19,
        Ea = (831.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -92.0

entry(
    index = 419,
    label = "C2H3 + O2 <=> CH2O + H + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.470e+36, 'cm^3/(mol*s)'),
        n = -7.6,
        Ea = (12640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.180e+16, 'cm^3/(mol*s)'),
        n = -1.28,
        Ea = (515.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (6.290e+36, 'cm^3/(mol*s)'),
        n = -7.6,
        Ea = (12610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.190e+16, 'cm^3/(mol*s)'),
        n = -1.28,
        Ea = (513.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.050e+36, 'cm^3/(mol*s)'),
        n = -7.57,
        Ea = (12490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.250e+16, 'cm^3/(mol*s)'),
        n = -1.29,
        Ea = (521.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (7.070e+35, 'cm^3/(mol*s)'),
        n = -7.32,
        Ea = (11820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.580e+16, 'cm^3/(mol*s)'),
        n = -1.31,
        Ea = (646.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.720e+36, 'cm^3/(mol*s)'),
        n = -7.47,
        Ea = (12460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (2.440e+16, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (1066.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.340e+36, 'cm^3/(mol*s)'),
        n = -7.2,
        Ea = (13430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (6.640e+15, 'cm^3/(mol*s)'),
        n = -1.18,
        Ea = (1429.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (8.260e+20, 'cm^3/(mol*s)'),
        n = -2.57,
        Ea = (5578.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (2.660e+69, 'cm^3/(mol*s)'),
        n = -19.23,
        Ea = (14760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (7.070e+33, 'cm^3/(mol*s)'),
        n = -6.28,
        Ea = (16000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.090e+11, 'cm^3/(mol*s)'),
        n = 0.19,
        Ea = (831.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -87.3

entry(
    index = 420,
    label = "C2H3 + O2 <=> CH2CO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.660e+02, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (6061.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.820e-01, 'cm^3/(mol*s)'),
        n = 3.12,
        Ea = (1331.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (8.910e+02, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (6078.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.070e-01, 'cm^3/(mol*s)'),
        n = 3.11,
        Ea = (1383.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (9.430e+02, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (6112.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (2.710e-01, 'cm^3/(mol*s)'),
        n = 3.08,
        Ea = (1496.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (1.060e+03, 'cm^3/(mol*s)'),
        n = 2.39,
        Ea = (6180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (5.260e-01, 'cm^3/(mol*s)'),
        n = 3.01,
        Ea = (1777.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.090e+03, 'cm^3/(mol*s)'),
        n = 2.38,
        Ea = (6179.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.370e+00, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (2225.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.390e+03, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (6074.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.190e-01, 'cm^3/(mol*s)'),
        n = 2.93,
        Ea = (2052.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.490e+06, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (8480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.190e-04, 'cm^3/(mol*s)'),
        n = 4.21,
        Ea = (2043.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.660e+10, 'cm^3/(mol*s)'),
        n = 0.36,
        Ea = (12010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.300e-03, 'cm^3/(mol*s)'),
        n = 3.97,
        Ea = (3414.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -72.7

entry(
    index = 421,
    label = "C2H3 + O2 <=> OCHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.790e+14, 'cm^3/(mol*s)'),
        n = -1.03,
        Ea = (912.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.800e-04, 'cm^3/(mol*s)'),
        n = 4.04,
        Ea = (-7019.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (5.030e+14, 'cm^3/(mol*s)'),
        n = -1.04,
        Ea = (922.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.450e-04, 'cm^3/(mol*s)'),
        n = 4.01,
        Ea = (-6978.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (6.430e+14, 'cm^3/(mol*s)'),
        n = -1.07,
        Ea = (983.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (9.730e-04, 'cm^3/(mol*s)'),
        n = 3.89,
        Ea = (-6768.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.730e+15, 'cm^3/(mol*s)'),
        n = -1.29,
        Ea = (1441.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.980e-01, 'cm^3/(mol*s)'),
        n = 3.15,
        Ea = (-5496.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.440e+18, 'cm^3/(mol*s)'),
        n = -2.13,
        Ea = (3234.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.340e+05, 'cm^3/(mol*s)'),
        n = 1.67,
        Ea = (-2931.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.300e+15, 'cm^3/(mol*s)'),
        n = -1.09,
        Ea = (2393.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.500e+15, 'cm^3/(mol*s)'),
        n = -3.08,
        Ea = (-4836.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.570e+33, 'cm^3/(mol*s)'),
        n = -6.5,
        Ea = (14910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (3.840e+10, 'cm^3/(mol*s)'),
        n = 0.22,
        Ea = (941.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (3.280e+31, 'cm^3/(mol*s)'),
        n = -5.76,
        Ea = (16250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.750e+08, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (858.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -73.7

entry(
    index = 422,
    label = "C2H3 + O2 <=> C2H2 + HO2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.080e+07, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (3322.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.760e+01, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (-796.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (7.750e+06, 'cm^3/(mol*s)'),
        n = 1.33,
        Ea = (3216.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (5.160e+01, 'cm^3/(mol*s)'),
        n = 2.73,
        Ea = (-768.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.210e+07, 'cm^3/(mol*s)'),
        n = 1.27,
        Ea = (3311.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (5.550e+01, 'cm^3/(mol*s)'),
        n = 2.73,
        Ea = (-658.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (2.150e+07, 'cm^3/(mol*s)'),
        n = 1.19,
        Ea = (3367.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.600e+01, 'cm^3/(mol*s)'),
        n = 2.76,
        Ea = (-493.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.130e+08, 'cm^3/(mol*s)'),
        n = 1.0,
        Ea = (3695.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (3.750e+00, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (-601.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.310e+11, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (5872.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (5.480e+00, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (86.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.190e+09, 'cm^3/(mol*s)'),
        n = 0.82,
        Ea = (5617.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (4.470e+08, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (955.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.060e+17, 'cm^3/(mol*s)'),
        n = -1.45,
        Ea = (12230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.020e+01, 'cm^3/(mol*s)'),
        n = 2.94,
        Ea = (1847.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -69.8

entry(
    index = 423,
    label = "C2H3 + O2 <=> CH2CHO + O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.160e+20, 'cm^3/(mol*s)'),
        n = -2.67,
        Ea = (6742.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.240e+10, 'cm^3/(mol*s)'),
        n = 0.62,
        Ea = (-278.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (7.020e+20, 'cm^3/(mol*s)'),
        n = -2.67,
        Ea = (6713.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.290e+10, 'cm^3/(mol*s)'),
        n = 0.62,
        Ea = (-248.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (8.970e+20, 'cm^3/(mol*s)'),
        n = -2.7,
        Ea = (6724.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.510e+10, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (-162.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (6.450e+20, 'cm^3/(mol*s)'),
        n = -2.65,
        Ea = (6489.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.840e+10, 'cm^3/(mol*s)'),
        n = 0.58,
        Ea = (38.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (4.090e+20, 'cm^3/(mol*s)'),
        n = -2.53,
        Ea = (6406.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (8.860e+09, 'cm^3/(mol*s)'),
        n = 0.67,
        Ea = (248.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.600e+23, 'cm^3/(mol*s)'),
        n = -3.22,
        Ea = (8697.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (6.670e+09, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (778.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.850e+25, 'cm^3/(mol*s)'),
        n = -3.77,
        Ea = (11530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.430e+09, 'cm^3/(mol*s)'),
        n = 0.92,
        Ea = (1219.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (9.280e+25, 'cm^3/(mol*s)'),
        n = -3.8,
        Ea = (13910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (7.140e+07, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (1401.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -13.7

entry(
    index = 424,
    label = "C2H3 + O2 <=> CHCHO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.910e+11, 'cm^3/(mol*s)'),
        n = -0.11,
        Ea = (2131.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (9.910e+11, 'cm^3/(mol*s)'),
        n = -0.66,
        Ea = (-1.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.130e+09, 'cm^3/(mol*s)'),
        n = 0.55,
        Ea = (46.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.940e+14, 'cm^3/(mol*s)'),
        n = -1.16,
        Ea = (4542.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (8.460e+08, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (1.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (2.790e+13, 'cm^3/(mol*s)'),
        n = -0.72,
        Ea = (3479.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (2.750e+14, 'cm^3/(mol*s)'),
        n = -1.83,
        Ea = (5.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.990e+11, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1995.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.580e+20, 'cm^3/(mol*s)'),
        n = -2.84,
        Ea = (7530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (2.350e+10, 'cm^3/(mol*s)'),
        n = 0.23,
        Ea = (1573.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (9.180e+14, 'cm^3/(mol*s)'),
        n = -2.26,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.700e+14, 'cm^3/(mol*s)'),
        n = -0.82,
        Ea = (4450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.110e+25, 'cm^3/(mol*s)'),
        n = -4.21,
        Ea = (13050.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.420e+11, 'cm^3/(mol*s)'),
        n = 0.05,
        Ea = (3774.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.650e+30, 'cm^3/(mol*s)'),
        n = -5.35,
        Ea = (18430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (3.170e+11, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (5338.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -7.2

entry(
    index = 425,
    label = "C2H3 + H <=> C2H2 + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.490e+15, 'cm^3/(mol*s)'),
        n = -0.311,
        Ea = (245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (1.500e+15, 'cm^3/(mol*s)'),
        n = -0.312,
        Ea = (245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.500e+15, 'cm^3/(mol*s)'),
        n = -0.312,
        Ea = (245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (1.510e+15, 'cm^3/(mol*s)'),
        n = -0.313,
        Ea = (248.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.490e+15, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (266.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (1.340e+15, 'cm^3/(mol*s)'),
        n = -0.291,
        Ea = (382.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.270e+15, 'cm^3/(mol*s)'),
        n = -0.426,
        Ea = (950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (8.790e+15, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (1677.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.400e+15, 'cm^3/(mol*s)'),
        n = -0.424,
        Ea = (2185.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (1.720e+13, 'cm^3/(mol*s)'),
        n = 0.287,
        Ea = (1158.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -0.3

entry(
    index = 426,
    label = "C2H3 + O <=> CH2CO + H",
    kinetics = Arrhenius(
        A = (1.030e+12, 'cm^3/(mol*s)'),
        n = 0.2,
        Ea = (-848.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished; 2013
# abstraction and addition
# DH = -69.0
entry(
    index = 427,
    label = "C2H4 + O <=> C2H3 + OH",
    kinetics = Arrhenius(
        A = (2.890e+03, 'cm^3/(mol*s)'),
        n = 3.201,
        Ea = (8507.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# LB Harding, SJ Klippenstein, Y Georgievskii, PCI 30:985 (2005).
# DH = -90.2
entry(
    index = 428,
    label = "C2H3 + OH <=> C2H2 + H2O",
    kinetics = Arrhenius(
        A = (3.010e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# X Li, AW Jasper, J Zador, JA Miller, SJ Klippenstein, PCI 36:219 (2017).
# DH = 7.5
entry(
    index = 429,
    label = "C2H3 + OH <=> CH2CHO + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -83.5
entry(
    index = 430,
    label = "C2H4 + O2 <=> C2H3 + HO2",
    kinetics = Arrhenius(
        A = (4.220e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (57629.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JAM estimate
# DH = -23.7
# C2H3+OH=CH3+HCO
# $$ Missing Reaction
# DH = ??
# C2H3+OH=CH3CO+H
# $$ Missing Reaction
# DH = ??
entry(
    index = 431,
    label = "C2H3 + HO2 <=> C2H2 + H2O2",
    kinetics = Arrhenius(
        A = (3.010e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# $$ Hua H, Ruscic B, Wang B. Theoretical calculations on the reaction of ethylene with oxygen. Chem Phys. 2005;311:335-41.
# DH = 61.2
entry(
    index = 432,
    label = "C2H3 + CH3 <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.930e+61, 'cm^3/(mol*s)'),
        n = -14.91,
        Ea = (19559.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (3.780e+46, 'cm^3/(mol*s)'),
        n = -11.15,
        Ea = (7332.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (7.490e+58, 'cm^3/(mol*s)'),
        n = -13.81,
        Ea = (20442.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.860e+40, 'cm^3/(mol*s)'),
        n = -8.97,
        Ea = (6234.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (9.740e+55, 'cm^3/(mol*s)'),
        n = -12.62,
        Ea = (21930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (7.240e+33, 'cm^3/(mol*s)'),
        n = -6.71,
        Ea = (4848.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.700e+50, 'cm^3/(mol*s)'),
        n = -10.88,
        Ea = (22198.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.280e+27, 'cm^3/(mol*s)'),
        n = -4.53,
        Ea = (3329.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.070e+48, 'cm^3/(mol*s)'),
        n = -9.9,
        Ea = (24315.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (5.400e+23, 'cm^3/(mol*s)'),
        n = -3.31,
        Ea = (2522.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -51.8

entry(
    index = 433,
    label = "C2H3 + CH3 <=> CH2CHCH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.120e+29, 'cm^3/(mol*s)'),
        n = -4.95,
        Ea = (7996.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (5.730e+15, 'cm^3/(mol*s)'),
        n = -0.77,
        Ea = (1196.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (4.860e+30, 'cm^3/(mol*s)'),
        n = -5.03,
        Ea = (11287.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.060e+13, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1429.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.300e+29, 'cm^3/(mol*s)'),
        n = -4.57,
        Ea = (14443.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.480e+10, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (1422.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.320e+30, 'cm^3/(mol*s)'),
        n = -4.54,
        Ea = (19255.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.100e+06, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (1057.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (5.160e+28, 'cm^3/(mol*s)'),
        n = -4.03,
        Ea = (23821.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.370e-01, 'cm^3/(mol*s)'),
        n = 3.91,
        Ea = (-354.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -99.5

entry(
    index = 434,
    label = "c-CH2CH2CH2 <=> C2H3 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.320e+64, 's^-1'),
        n = -15.14,
        Ea = (111300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.510e+49, 's^-1'),
        n = -11.04,
        Ea = (99748.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (8.300e+64, 's^-1'),
        n = -14.72,
        Ea = (113700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.050e+45, 's^-1'),
        n = -9.46,
        Ea = (99275.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.000e+70, 's^-1'),
        n = -15.72,
        Ea = (121940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.390e+50, 's^-1'),
        n = -10.63,
        Ea = (104220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.660e+67, 's^-1'),
        n = -14.59,
        Ea = (124380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.760e+47, 's^-1'),
        n = -9.43,
        Ea = (104930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (7.870e+62, 's^-1'),
        n = -13.05,
        Ea = (126800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.880e+39, 's^-1'),
        n = -6.94,
        Ea = (103980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -13.2

entry(
    index = 435,
    label = "C2H3 + CH3 <=> C2H2 + CH4",
    kinetics = Arrhenius(
        A = (9.040e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-1520.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = 90.7
entry(
    index = 436,
    label = "C2H3 + CH2 <=> CH2CCH2 + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SI Stoliarov, VD Knyazev, IR Slagle, JPCA 104:9687 (2000).
# DH = -69.1
entry(
    index = 437,
    label = "C2H3 + CH <=> CH2 + C2H2",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -66.6
entry(
    index = 438,
    label = "C2H3 + HCO <=> C2H4 + CO",
    kinetics = Arrhenius(
        A = (9.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -65.6
entry(
    index = 439,
    label = "C2H5 + C2H3 <=> C2H4 + C2H4",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, RF Hampson JPCRD 15:1087 (1986).
# DH = -94.5
entry(
    index = 440,
    label = "C2H3 + C2H3 <=> CH2CHCHCH2",
    kinetics = Arrhenius(
        A = (1.500e+42, 'cm^3/(mol*s)'),
        n = -8.84,
        Ea = (12483.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## TSANG AND HAMPSON, J. PHYS. CHEM. REF. DATA, 15:1087 (1986)
# JA Miller - estimate
# DH = -74.5
entry(
    index = 441,
    label = "C2H3 + C2H3 <=> C2H4 + C2H2",
    kinetics = Arrhenius(
        A = (8.430e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -114.0
entry(
    index = 442,
    label = "C2H3 + C2H3 <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (9.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -74.9
entry(
    index = 443,
    label = "C2H3 + C2H3 <=> CH2CCH + CH3",
    kinetics = Arrhenius(
        A = (1.800e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CJ Pope - estimate
# DH = -14.0
entry(
    index = 444,
    label = "C2H3 + C2H2 <=> CH2CHCHCH",
    kinetics = Arrhenius(
        A = (1.010e+51, 'cm^3/(mol*s)'),
        n = -12.778,
        Ea = (15608.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CJ Pope - estimate
# DH = -23.4
entry(
    index = 445,
    label = "C2H3 + C2H2 <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (1.540e+16, 'cm^3/(mol*s)'),
        n = -1.069,
        Ea = (9566.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = -37.7
entry(
    index = 446,
    label = "C2H3 + C2H2 <=> c-CH2CHCHCH",
    kinetics = Arrhenius(
        A = (1.490e+50, 'cm^3/(mol*s)'),
        n = -12.79,
        Ea = (15618.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = -4.2
entry(
    index = 447,
    label = "C2H3 + C2H <=> CH2CCCH + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = -44.7
entry(
    index = 448,
    label = "CH2CO + H <=> CH3 + CO",
    kinetics = Arrhenius(
        A = (7.770e+08, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (2780.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -36.3
# *****************************************************************************
#    CH2CO subset                                                             *
#    CHCOH subset                                                             *
#    CHCHO subset                                                             *
#    CCO subset                                                               *
# *****************************************************************************
# Fuel Radicals: HCCO
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition
# included in CH2 submechanism
# *** Fuel + Radical
entry(
    index = 449,
    label = "CH2CO + O <=> CH2O + CO",
    kinetics = Arrhenius(
        A = (3.610e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1351.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 109:6045 (2005).
# DH = -32.2
entry(
    index = 450,
    label = "CH2CO + O <=> CO2 + CH2",
    kinetics = Arrhenius(
        A = (1.080e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1351.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -100.7
entry(
    index = 451,
    label = "CH2CO + OH <=> HCCO + H2O",
    kinetics = Arrhenius(
        A = (1.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (3000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -48.8
# CH2CO+O=HCO+HCO
# $$ Missing Reaction
# DH = ?
entry(
    index = 452,
    label = "CH2CO + OH <=> CH2OH + CO",
    kinetics = Arrhenius(
        A = (1.010e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-1013.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -13.0
entry(
    index = 453,
    label = "CH2CO + OH <=> CH3 + CO2",
    kinetics = Arrhenius(
        A = (6.750e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-1013.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -27.9
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -56.3

entry(
    index = 455,
    label = "CH3C(O)CH2 <=> CH2CO + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.320e+75, 's^-1'),
        n = -19.8,
        Ea = (62920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (4.240e+39, 's^-1'),
        n = -8.92,
        Ea = (46300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (4.310e+69, 's^-1'),
        n = -17.52,
        Ea = (62170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.810e+36, 's^-1'),
        n = -7.63,
        Ea = (45980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (7.050e+62, 's^-1'),
        n = -15.1,
        Ea = (61380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (7.520e+31, 's^-1'),
        n = -6.09,
        Ea = (45200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (7.490e+54, 's^-1'),
        n = -12.38,
        Ea = (60130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.800e+28, 's^-1'),
        n = -4.84,
        Ea = (44490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (6.980e+47, 's^-1'),
        n = -10.01,
        Ea = (59250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.980e+25, 's^-1'),
        n = -3.81,
        Ea = (43940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.220e+41, 's^-1'),
        n = -7.8,
        Ea = (58220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (2.980e+22, 's^-1'),
        n = -2.83,
        Ea = (43390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# k_inf             4.28E+06       1.800      30840
# J Zador, JA Miller, PCI 35:181 (2013).
# DH = 0.7

entry(
    index = 456,
    label = "CH2(S) + CH2CO <=> C2H4 + CO",
    kinetics = Arrhenius(
        A = (1.600e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 29.2
# CH2CO+CH3=C2H5+CO
# ## Missing Reaction
entry(
    index = 457,
    label = "OH + C2H2 <=> CHCOH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.770e+05, 'cm^3/(mol*s)'),
        n = 2.28,
        Ea = (12419.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.470e+05, 'cm^3/(mol*s)'),
        n = 2.16,
        Ea = (12547.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.780e+06, 'cm^3/(mol*s)'),
        n = 2.04,
        Ea = (12669.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.410e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (12713.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.210e+06, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (12810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.350e+06, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (13603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# W Hack, M Koch, R Wagener, HGg Wagner, BBPC 93:165 (1989).
# DH = -104.5

entry(
    index = 458,
    label = "CHCOH + H <=> HCCO + H2",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 109:6045 (2005).
# DH = 10.6
entry(
    index = 459,
    label = "CHCOH + O <=> HCCO + OH",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1900.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -32.0
entry(
    index = 460,
    label = "CHCOH + OH <=> HCCO + H2O",
    kinetics = Arrhenius(
        A = (1.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -30.4
entry(
    index = 461,
    label = "C2H2 + HO2 <=> CHCHO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.490e+09, 'cm^3/(mol*s)'),
        n = 0.91,
        Ea = (18500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.410e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (14690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (5.930e+09, 'cm^3/(mol*s)'),
        n = 0.9,
        Ea = (18550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.480e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (14700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (6.800e+09, 'cm^3/(mol*s)'),
        n = 0.88,
        Ea = (18640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (2.630e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (14730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (1.560e+10, 'cm^3/(mol*s)'),
        n = 0.77,
        Ea = (19040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.500e+07, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (14790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.480e+09, 'cm^3/(mol*s)'),
        n = 0.99,
        Ea = (18810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.470e+08, 'cm^3/(mol*s)'),
        n = 1.32,
        Ea = (15090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (5.390e+10, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (20740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.610e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (15420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.700e+08, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (15960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.670e+07, 'cm^3/(mol*s)'),
        n = 1.59,
        Ea = (15910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.450e+11, 'cm^3/(mol*s)'),
        n = 0.48,
        Ea = (17730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (7.210e+06, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (16020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller - estimate
# DH = -46.5

entry(
    index = 462,
    label = "CH2CO + H <=> HCCO + H2",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (10000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = 13.3
# *** Fuel Radical Decomposition
# *** Fuel Radical + Stable
entry(
    index = 463,
    label = "CH2CO + O <=> HCCO + OH",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (10000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 1.5
# *** Fuel Radical + Radical
entry(
    index = 464,
    label = "HCCO + O2 <=> CO2 + CO + H",
    kinetics = Arrhenius(
        A = (4.780e+12, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 3.1
entry(
    index = 465,
    label = "HCCO + O2 <=> CO + CO + OH",
    kinetics = Arrhenius(
        A = (1.910e+11, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1023.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, PCI 29:1209 (2003).
# DH = -111.7
entry(
    index = 466,
    label = "HCCO + O2 <=> O + CO + HCO",
    kinetics = Arrhenius(
        A = (2.180e+02, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (3541.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, PCI 29:1209 (2003).
# DH = -87.6
entry(
    index = 467,
    label = "HCCO + H <=> CH2 + CO",
    kinetics = Arrhenius(
        A = (1.060e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, PCI 29:1209 (2003).
# DH = -37.5
entry(
    index = 468,
    label = "HCCO + O <=> H + CO + CO",
    kinetics = Arrhenius(
        A = (9.640e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -27.7
entry(
    index = 469,
    label = "HCCO + O <=> CH + CO2",
    kinetics = Arrhenius(
        A = (2.950e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1113.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -104.1
entry(
    index = 470,
    label = "HCCO + OH <=> CCO + H2O",
    kinetics = Arrhenius(
        A = (1.440e+04, 'cm^3/(mol*s)'),
        n = 2.65,
        Ea = (1472.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -53.6
# SZ Xiong, Q Yao, ZR Li, XY Li, CF 161:885 (2014).
# DH = -18.3

entry(
    index = 474,
    label = "HCCO + OH <=> CHOH(T) + CO",
    kinetics = Arrhenius(
        A = (2.870e+12, 'cm^3/(mol*s)'),
        n = 0.37,
        Ea = (24.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SZ Xiong, Q Yao, ZR Li, XY Li, CF 161:885 (2014).
# DH = -51.6
entry(
    index = 475,
    label = "HCCO + OH <=> OCCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.630e+08, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (845.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.630e+08, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (845.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.640e+08, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (849.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.960e+08, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (917.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.190e+08, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (1531.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SZ Xiong, Q Yao, ZR Li, XY Li, CF 161:885 (2014).
# DH = ??

entry(
    index = 476,
    label = "HCCO + CH3 <=> C2H4 + CO",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SZ Xiong, Q Yao, ZR Li, XY Li, CF 161:885 (2014).
# DH = -14.7
entry(
    index = 477,
    label = "CH2 + HCCO <=> C2H3 + CO",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -90.9
entry(
    index = 478,
    label = "CH + HCCO <=> C2H2 + CO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -91.0
entry(
    index = 479,
    label = "HCCO + HCCO <=> C2H2 + CO + CO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -156.7
entry(
    index = 480,
    label = "CCO <=> C + CO",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (2.000e+15, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (44200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = None,
    ),
    
)

# JA Miller, RE Mitchell, MD Smookte, RJ Kee, PCI 19:181 (1982).
# JA Miller - estimate
# DH = -84.4
# *** CCO Reactions
entry(
    index = 481,
    label = "CCO + O2 <=> CO + CO + O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# G Fridriechs, HGg Wagner, ZPC 203:1 (1998).
# DH = ??
entry(
    index = 482,
    label = "CCO + O2 <=> CO + CO2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# KH Becker, R Konig, R Meuser, P Wiesen, KD Bayes, JPPA 64:1 (1992).
# DG Williamson, KD Bayes, JACS 89:3390 (1967).
# DH = -85.4
entry(
    index = 483,
    label = "CCO + H <=> CH + CO",
    kinetics = Arrhenius(
        A = (1.300e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# KH Becker, R Konig, R Meuser, P Wiesen, KD Bayes, JPPA 64:1 (1992).
# DG Williamson, KD Bayes, JACS 89:3390 (1967).
# DH = ??
entry(
    index = 484,
    label = "CCO + O <=> CO + CO",
    kinetics = Arrhenius(
        A = (5.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Bauer, KH Becker, R Meuser, BBPC 89:340 (1985).
# DH = -27.2
entry(
    index = 485,
    label = "CCO + OH <=> CO + CO + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Bauer, KH Becker, R Meuser, BBPC 89:340 (1985).
# DH = -203.6
entry(
    index = 486,
    label = "CH2CHOO <=> CO2 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.090e+33, 's^-1'),
        n = -7.95,
        Ea = (31290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.200e+122, 's^-1'),
        n = -39.75,
        Ea = (43640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.210e+118, 's^-1'),
        n = -33.13,
        Ea = (73790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.960e+29, 's^-1'),
        n = -6.29,
        Ea = (30920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (8.560e+32, 's^-1'),
        n = -7.21,
        Ea = (33550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (5.100e-66, 's^-1'),
        n = 21.37,
        Ea = (-11110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.270e+33, 's^-1'),
        n = -7.22,
        Ea = (34990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.760e-47, 's^-1'),
        n = 15.85,
        Ea = (-5283.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.490e-79, 's^-1'),
        n = 25.01,
        Ea = (-21020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (3.820e+32, 's^-1'),
        n = -6.8,
        Ea = (35690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (8.160e+32, 's^-1'),
        n = -6.76,
        Ea = (37270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.620e+00, 's^-1'),
        n = 2.1,
        Ea = (17170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (7.010e+37, 's^-1'),
        n = -8.06,
        Ea = (42200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (3.490e+14, 's^-1'),
        n = -1.58,
        Ea = (26470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.280e+01, 's^-1'),
        n = 2.57,
        Ea = (20351.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -101.9
# *****************************************************************************
#    CH2CHOOH subset                                                          *
# *****************************************************************************
# Fuel Radicals: CH2CHOO
# New Radicals Formed:
# New Fuels:
# *** Fuel Radical Decomposition
# C2H3 + O2 = CH2CHOO included in C2H4 submechanism
# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -86.5

entry(
    index = 488,
    label = "CH2CHOO <=> CH2O + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.660e+174, 's^-1'),
        n = -55.52,
        Ea = (60320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.270e+35, 's^-1'),
        n = -7.97,
        Ea = (31280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (9.030e+66, 's^-1'),
        n = -17.25,
        Ea = (48120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.080e+26, 's^-1'),
        n = -4.96,
        Ea = (28780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.820e+43, 's^-1'),
        n = -9.87,
        Ea = (37960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.450e+20, 's^-1'),
        n = -3.08,
        Ea = (26630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (8.640e+33, 's^-1'),
        n = -6.88,
        Ea = (34370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.060e+130, 's^-1'),
        n = -39.38,
        Ea = (54700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.290e+171, 's^-1'),
        n = -43.53,
        Ea = (191900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (2.350e+34, 's^-1'),
        n = -6.87,
        Ea = (35700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.030e+32, 's^-1'),
        n = -6.06,
        Ea = (35500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.180e+175, 's^-1'),
        n = -53.78,
        Ea = (68500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.850e+34, 's^-1'),
        n = -6.57,
        Ea = (38510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.070e+185, 's^-1'),
        n = -54.22,
        Ea = (88990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (5.700e+29, 's^-1'),
        n = -5.19,
        Ea = (36800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.680e+02, 's^-1'),
        n = 1.81,
        Ea = (18100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -48.5

entry(
    index = 489,
    label = "CH2CHOO <=> CH2O + H + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.880e+174, 's^-1'),
        n = -55.52,
        Ea = (60320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (5.290e+35, 's^-1'),
        n = -7.97,
        Ea = (31280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (2.110e+67, 's^-1'),
        n = -17.25,
        Ea = (48120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (4.850e+26, 's^-1'),
        n = -4.96,
        Ea = (28780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.260e+43, 's^-1'),
        n = -9.87,
        Ea = (37960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (3.370e+20, 's^-1'),
        n = -3.08,
        Ea = (26630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (2.020e+34, 's^-1'),
        n = -6.88,
        Ea = (34370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.460e+130, 's^-1'),
        n = -39.38,
        Ea = (54700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.700e+172, 's^-1'),
        n = -43.53,
        Ea = (191900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (5.490e+34, 's^-1'),
        n = -6.87,
        Ea = (35700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (2.400e+32, 's^-1'),
        n = -6.06,
        Ea = (35500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (5.090e+175, 's^-1'),
        n = -53.78,
        Ea = (68500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (4.320e+34, 's^-1'),
        n = -6.57,
        Ea = (38510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (2.490e+185, 's^-1'),
        n = -54.22,
        Ea = (88990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.330e+30, 's^-1'),
        n = -5.19,
        Ea = (36800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.090e+03, 's^-1'),
        n = 1.81,
        Ea = (18100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -43.9

entry(
    index = 490,
    label = "CH2CHOO <=> CH2CO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.150e+47, 's^-1'),
        n = -12.28,
        Ea = (75330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.310e+02, 's^-1'),
        n = -0.73,
        Ea = (25710.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (8.430e+09, 's^-1'),
        n = -2.06,
        Ea = (33720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.830e-23, 's^-1'),
        n = 7.84,
        Ea = (20190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (6.060e+04, 's^-1'),
        n = 0.17,
        Ea = (34220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (3.820e+63, 's^-1'),
        n = -20.44,
        Ea = (43420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (1.510e+19, 's^-1'),
        n = -3.61,
        Ea = (43060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.180e+27, 's^-1'),
        n = -7.76,
        Ea = (37230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.130e+33, 's^-1'),
        n = -7.39,
        Ea = (51610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (2.320e-05, 's^-1'),
        n = 3.47,
        Ea = (31560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (4.440e+36, 's^-1'),
        n = -7.99,
        Ea = (54680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.060e-01, 's^-1'),
        n = 2.64,
        Ea = (34160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.190e+37, 's^-1'),
        n = -7.8,
        Ea = (56460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (5.620e+02, 's^-1'),
        n = 1.7,
        Ea = (36450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (9.080e+35, 's^-1'),
        n = -7.21,
        Ea = (57550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.110e+07, 's^-1'),
        n = 0.52,
        Ea = (38670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -29.2

entry(
    index = 491,
    label = "CH2CHOO <=> OCHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.410e+80, 's^-1'),
        n = -22.2,
        Ea = (51750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.190e+28, 's^-1'),
        n = -6.01,
        Ea = (28740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.310e+65, 's^-1'),
        n = -17.01,
        Ea = (48090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.400e+25, 's^-1'),
        n = -4.8,
        Ea = (28940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.980e+51, 's^-1'),
        n = -12.62,
        Ea = (43000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (2.910e+20, 's^-1'),
        n = -3.29,
        Ea = (27550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (1.480e+44, 's^-1'),
        n = -10.12,
        Ea = (40790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.580e+19, 's^-1'),
        n = -2.82,
        Ea = (27620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.260e+59, 's^-1'),
        n = -14.33,
        Ea = (51390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.930e+22, 's^-1'),
        n = -3.54,
        Ea = (29980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (4.930e+26, 's^-1'),
        n = -4.67,
        Ea = (34320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (7.510e+29, 's^-1'),
        n = -5.75,
        Ea = (34490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.060e+33, 's^-1'),
        n = -6.38,
        Ea = (39520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (7.140e+61, 's^-1'),
        n = -16.16,
        Ea = (43280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.300e+32, 's^-1'),
        n = -5.92,
        Ea = (40660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.140e+19, 's^-1'),
        n = -2.56,
        Ea = (29670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -30.2

entry(
    index = 492,
    label = "CH2CHOO <=> CH2CHO + O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.700e+180, 's^-1'),
        n = -48.19,
        Ea = (169300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.470e+30, 's^-1'),
        n = -6.64,
        Ea = (41110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.900e+38, 's^-1'),
        n = -8.69,
        Ea = (42770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (9.650e-12, 's^-1'),
        n = 5.96,
        Ea = (22890.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.570e+47, 's^-1'),
        n = -11.21,
        Ea = (47050.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (3.950e+22, 's^-1'),
        n = -3.71,
        Ea = (36270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (7.620e+81, 's^-1'),
        n = -21.28,
        Ea = (65080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.390e+33, 's^-1'),
        n = -6.62,
        Ea = (41280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.860e+68, 's^-1'),
        n = -16.83,
        Ea = (60680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (6.370e+31, 's^-1'),
        n = -5.96,
        Ea = (41260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (2.020e+55, 's^-1'),
        n = -12.69,
        Ea = (55840.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.130e+29, 's^-1'),
        n = -5.1,
        Ea = (40710.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.110e+53, 's^-1'),
        n = -11.79,
        Ea = (56690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (4.660e+27, 's^-1'),
        n = -4.5,
        Ea = (40530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (4.300e+48, 's^-1'),
        n = -10.31,
        Ea = (56090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (5.990e+25, 's^-1'),
        n = -3.85,
        Ea = (40120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -26.4

entry(
    index = 493,
    label = "CH2CHOO <=> CHCHO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.640e+49, 's^-1'),
        n = -12.13,
        Ea = (67420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.170e+56, 's^-1'),
        n = -14.81,
        Ea = (60700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.440e+36, 's^-1'),
        n = -9.92,
        Ea = (41220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.320e+40, 's^-1'),
        n = -9.39,
        Ea = (50420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.180e+40, 's^-1'),
        n = -10.53,
        Ea = (43670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.610e+43, 's^-1'),
        n = -9.99,
        Ea = (50290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.790e+46, 's^-1'),
        n = -10.72,
        Ea = (51900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.330e+124, 's^-1'),
        n = -36.77,
        Ea = (70100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.600e+49, 's^-1'),
        n = -11.24,
        Ea = (54150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.880e+103, 's^-1'),
        n = -29.49,
        Ea = (65410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (2.380e+51, 's^-1'),
        n = -11.64,
        Ea = (56980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (5.960e+86, 's^-1'),
        n = -23.81,
        Ea = (62170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.000e+54, 's^-1'),
        n = -12.22,
        Ea = (61840.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.510e+57, 's^-1'),
        n = -13.94,
        Ea = (55390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (9.540e+195, 's^-1'),
        n = -52.27,
        Ea = (163500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.790e+34, 's^-1'),
        n = -6.4,
        Ea = (50000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = 36.3

entry(
    index = 494,
    label = "C2H + H <=> C2H2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=-1.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(3.75e+33, 'cm^6/(mol^2*s)'), n=-4.8, Ea=(1900.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.646,
        T3 = (132.0, 'K'),
        T1 = (1320.0, 'K'),
        T2 = (5570.0, 'K'),
        efficiencies = { '[H][H]': 2.0, '[C-]#[O+]': 1.5, 'O=C=O': 2.0, 'O': 6.0, '[Ar]': 0.7, 'N#N': 1.0, 'C': 2.0, 'CC': 3.0 }
    ),
)

entry(
    index = 495,
    label = "CH2C <=> C2H2",
    kinetics = Arrhenius(
        A = (1.000e+07, 's^-1'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# GRIMech 1.2; M. Frenklach, H. Wang, C.-L. Yu, M. Goldenberg, C.T. Bowman et al.; #http://www.me.berkeley.edu/gri_mech/ 1995.
# $$ High P limit from LB Harding, Y Georgievskii, SJ Klippenstein, JPCA 109:4646 (2005).
# DH = -131.6
#entry(
#    index = 496,
#    label = "C2H2 + O2 <=> H + H + CO + CO",
#    kinetics = Arrhenius(
#        A = (7.400e+09, 'cm^3/(mol*s)'),
#        n = 0.866,
#        Ea = (52875.0, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    
#)
# ## 99 LAS/ WA
# $$ Baulch (2005).
# JA Miller - estimate
# DH = -43.8
# *** Fuel + Radical
entry(
    index = 497,
    label = "C2H2 + O <=> CH2 + CO",
    kinetics = Arrhenius(
        A = (4.080e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1900.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished
# DH = -5.6
entry(
    index = 498,
    label = "C2H2 + O <=> HCCO + H",
    kinetics = Arrhenius(
        A = (1.630e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1900.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - unpublished
# K Mahmud, A Fontijn, JPC 91:1918 (1987).
# TL Nguyen, L Vereecken, J Peeters, JPCA 110:6696 (2006).
# DH = -47.4
entry(
    index = 499,
    label = "OH + C2H2 <=> CHCHOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.870e+64, 'cm^3/(mol*s)'),
        n = -18.57,
        Ea = (10009.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.640e+33, 'cm^3/(mol*s)'),
        n = -7.36,
        Ea = (6392.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (4.690e+59, 'cm^3/(mol*s)'),
        n = -16.87,
        Ea = (9087.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 1)
        Arrhenius(
            A = (4.380e+32, 'cm^3/(mol*s)'),
        n = -7.02,
        Ea = (5933.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 2)
        Arrhenius(
            A = (1.240e+28, 'cm^3/(mol*s)'),
        n = -5.56,
        Ea = (3724.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.380e+42, 'cm^3/(mol*s)'),
        n = -9.96,
        Ea = (11737.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.900e+44, 'cm^3/(mol*s)'),
        n = -11.38,
        Ea = (6299.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.490e+31, 'cm^3/(mol*s)'),
        n = -6.2,
        Ea = (6635.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.490e+24, 'cm^3/(mol*s)'),
        n = -4.06,
        Ea = (3261.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.510e+31, 'cm^3/(mol*s)'),
        n = -5.92,
        Ea = (8761.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.200e+20, 'cm^3/(mol*s)'),
        n = -2.8,
        Ea = (2831.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.600e+29, 'cm^3/(mol*s)'),
        n = -4.91,
        Ea = (9734.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller - unpublished
# K Mahmud, A Fontijn, JPC 91:1918 (1987).
# TL Nguyen, L Vereecken, J Peeters, JPCA 110:6696 (2006).
# DH = -19.8

entry(
    index = 500,
    label = "OH + C2H2 <=> CH3 + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.760e+05, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (-330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.370e+06, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (227.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (7.650e+07, 'cm^3/(mol*s)'),
        n = 1.05,
        Ea = (1115.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.280e+09, 'cm^3/(mol*s)'),
        n = 0.73,
        Ea = (2579.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.310e+08, 'cm^3/(mol*s)'),
        n = 0.92,
        Ea = (3736.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.250e+05, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (4697.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 109:6045 (2005).
# DH = -30.7

entry(
    index = 501,
    label = "OH + C2H2 <=> CH2CO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.580e+03, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (-844.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.520e+04, 'cm^3/(mol*s)'),
        n = 2.28,
        Ea = (-292.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (3.020e+05, 'cm^3/(mol*s)'),
        n = 1.92,
        Ea = (598.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.530e+06, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (2106.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.100e+06, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (3400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.460e+04, 'cm^3/(mol*s)'),
        n = 2.45,
        Ea = (4477.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 109:6045 (2005).
# DH = -55.0

entry(
    index = 502,
    label = "C2H2 + HO2 <=> CH2CHOO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.990e+06, 'cm^3/(mol*s)'),
        n = -1.02,
        Ea = (9152.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.880e+26, 'cm^3/(mol*s)'),
        n = -8.34,
        Ea = (9249.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (6.020e+17, 'cm^3/(mol*s)'),
        n = -3.82,
        Ea = (10790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (5.260e+129, 'cm^3/(mol*s)'),
        n = -41.74,
        Ea = (35930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.470e+48, 'cm^3/(mol*s)'),
        n = -12.82,
        Ea = (25220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.960e+18, 'cm^3/(mol*s)'),
        n = -3.67,
        Ea = (10480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (4.060e+50, 'cm^3/(mol*s)'),
        n = -13.07,
        Ea = (27220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.930e+21, 'cm^3/(mol*s)'),
        n = -4.37,
        Ea = (12220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (9.080e+46, 'cm^3/(mol*s)'),
        n = -11.57,
        Ea = (26880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (1.920e+22, 'cm^3/(mol*s)'),
        n = -4.28,
        Ea = (13080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (4.600e+43, 'cm^3/(mol*s)'),
        n = -10.24,
        Ea = (26930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.110e+21, 'cm^3/(mol*s)'),
        n = -3.78,
        Ea = (13380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (5.610e+38, 'cm^3/(mol*s)'),
        n = -8.49,
        Ea = (26210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.390e+20, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (13410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (2.530e+35, 'cm^3/(mol*s)'),
        n = -7.26,
        Ea = (26390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.420e+19, 'cm^3/(mol*s)'),
        n = -2.91,
        Ea = (13420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 109:6045 (2005).
# DH = -22.8

entry(
    index = 503,
    label = "C2H2 + HO2 <=> CO2 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.150e-07, 'cm^3/(mol*s)'),
        n = 4.31,
        Ea = (4614.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.010e+08, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (11790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.100e-07, 'cm^3/(mol*s)'),
        n = 4.32,
        Ea = (4622.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.010e+08, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (11780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.750e+142, 'cm^3/(mol*s)'),
        n = -35.04,
        Ea = (188700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.550e+05, 'cm^3/(mol*s)'),
        n = 0.95,
        Ea = (10200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.960e+84, 'cm^3/(mol*s)'),
        n = -19.8,
        Ea = (119800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.380e+06, 'cm^3/(mol*s)'),
        n = 0.68,
        Ea = (10810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (5.020e+13, 'cm^3/(mol*s)'),
        n = -1.6,
        Ea = (14980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (9.290e-03, 'cm^3/(mol*s)'),
        n = 3.0,
        Ea = (7659.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (8.560e+28, 'cm^3/(mol*s)'),
        n = -6.15,
        Ea = (24030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.860e+04, 'cm^3/(mol*s)'),
        n = 1.26,
        Ea = (11230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.280e+27, 'cm^3/(mol*s)'),
        n = -5.42,
        Ea = (25380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (2.890e+02, 'cm^3/(mol*s)'),
        n = 1.79,
        Ea = (11240.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.710e+15, 'cm^3/(mol*s)'),
        n = -1.8,
        Ea = (20370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (3.900e-07, 'cm^3/(mol*s)'),
        n = 4.21,
        Ea = (7314.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -29.8

entry(
    index = 504,
    label = "C2H2 + HO2 <=> CO + CH3O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.540e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (49510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.890e+04, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (9903.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (2.780e+08, 'cm^3/(mol*s)'),
        n = 0.01,
        Ea = (11920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (9.670e-07, 'cm^3/(mol*s)'),
        n = 4.15,
        Ea = (5173.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (8.060e+07, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (11650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.840e-08, 'cm^3/(mol*s)'),
        n = 4.62,
        Ea = (4517.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (8.940e+69, 'cm^3/(mol*s)'),
        n = -15.85,
        Ea = (102500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (5.380e+05, 'cm^3/(mol*s)'),
        n = 0.86,
        Ea = (10700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (5.660e+12, 'cm^3/(mol*s)'),
        n = -1.25,
        Ea = (14570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (5.370e-04, 'cm^3/(mol*s)'),
        n = 3.42,
        Ea = (7218.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (3.300e+23, 'cm^3/(mol*s)'),
        n = -4.45,
        Ea = (21210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.860e+02, 'cm^3/(mol*s)'),
        n = 1.84,
        Ea = (10460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.430e+22, 'cm^3/(mol*s)'),
        n = -3.96,
        Ea = (22650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (8.110e+00, 'cm^3/(mol*s)'),
        n = 2.3,
        Ea = (10560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (1.170e+18, 'cm^3/(mol*s)'),
        n = -2.57,
        Ea = (22360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.860e-04, 'cm^3/(mol*s)'),
        n = 3.42,
        Ea = (9329.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -116.3

entry(
    index = 505,
    label = "C2H2 + HO2 <=> CH2O + HCO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.900e+13, 'cm^3/(mol*s)'),
        n = -1.17,
        Ea = (13750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (8.430e+00, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (7382.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (4.260e+00, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (7253.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.560e+13, 'cm^3/(mol*s)'),
        n = -1.05,
        Ea = (13520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.590e-06, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4525.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (6.900e+09, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (11720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (3.330e+102, 'cm^3/(mol*s)'),
        n = -24.18,
        Ea = (138600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (8.070e+07, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (10850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (5.220e+15, 'cm^3/(mol*s)'),
        n = -1.75,
        Ea = (15180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (3.540e+00, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (8025.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (7.320e+35, 'cm^3/(mol*s)'),
        n = -7.77,
        Ea = (26970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (9.840e+06, 'cm^3/(mol*s)'),
        n = 0.91,
        Ea = (11710.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.780e+28, 'cm^3/(mol*s)'),
        n = -5.3,
        Ea = (25130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (1.790e+04, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (11250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (2.470e+16, 'cm^3/(mol*s)'),
        n = -1.7,
        Ea = (20030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.320e-06, 'cm^3/(mol*s)'),
        n = 4.31,
        Ea = (6829.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -78.3

entry(
    index = 506,
    label = "C2H2 + HO2 <=> CH2O + H + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.100e+13, 'cm^3/(mol*s)'),
        n = -1.17,
        Ea = (13750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.970e+01, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (7382.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (9.940e+00, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (7253.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.630e+13, 'cm^3/(mol*s)'),
        n = -1.05,
        Ea = (13520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (6.050e-06, 'cm^3/(mol*s)'),
        n = 4.34,
        Ea = (4525.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.610e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (11720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (7.770e+102, 'cm^3/(mol*s)'),
        n = -24.18,
        Ea = (138600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.880e+08, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (10850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.220e+16, 'cm^3/(mol*s)'),
        n = -1.75,
        Ea = (15180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (8.260e+00, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (8025.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (1.710e+36, 'cm^3/(mol*s)'),
        n = -7.77,
        Ea = (26970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.300e+07, 'cm^3/(mol*s)'),
        n = 0.91,
        Ea = (11710.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (4.140e+28, 'cm^3/(mol*s)'),
        n = -5.3,
        Ea = (25130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (4.190e+04, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (11250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (5.770e+16, 'cm^3/(mol*s)'),
        n = -1.7,
        Ea = (20030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.010e-05, 'cm^3/(mol*s)'),
        n = 4.31,
        Ea = (6829.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -73.7

entry(
    index = 507,
    label = "C2H2 + HO2 <=> CH2CO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.250e-07, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (15530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.310e-14, 'cm^3/(mol*s)'),
        n = 6.58,
        Ea = (10270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (6.700e-07, 'cm^3/(mol*s)'),
        n = 4.74,
        Ea = (15550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.290e-14, 'cm^3/(mol*s)'),
        n = 6.59,
        Ea = (10330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.180e-07, 'cm^3/(mol*s)'),
        n = 4.81,
        Ea = (15410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (3.990e-14, 'cm^3/(mol*s)'),
        n = 6.36,
        Ea = (10270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (5.280e-07, 'cm^3/(mol*s)'),
        n = 4.78,
        Ea = (15460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.280e-15, 'cm^3/(mol*s)'),
        n = 6.7,
        Ea = (10090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.040e-06, 'cm^3/(mol*s)'),
        n = 4.69,
        Ea = (15640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (8.710e-21, 'cm^3/(mol*s)'),
        n = 8.3,
        Ea = (8107.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (4.680e-05, 'cm^3/(mol*s)'),
        n = 4.22,
        Ea = (16780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (8.360e-22, 'cm^3/(mol*s)'),
        n = 8.76,
        Ea = (8804.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (8.990e-01, 'cm^3/(mol*s)'),
        n = 2.97,
        Ea = (19730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (6.870e-14, 'cm^3/(mol*s)'),
        n = 6.67,
        Ea = (13130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (3.580e+03, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (23010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.630e-12, 'cm^3/(mol*s)'),
        n = 6.15,
        Ea = (14730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -44.6

entry(
    index = 508,
    label = "C2H2 + HO2 <=> OCHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 0.316, 1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.510e+07, 'cm^3/(mol*s)'),
        n = 0.48,
        Ea = (11720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.430e-06, 'cm^3/(mol*s)'),
        n = 4.43,
        Ea = (5578.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (7.430e+07, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (11690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.000e-06, 'cm^3/(mol*s)'),
        n = 4.45,
        Ea = (5564.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (7.910e+07, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (11700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 1)
        Arrhenius(
            A = (1.810e-06, 'cm^3/(mol*s)'),
        n = 4.46,
        Ea = (5654.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.316 atm (term 2)
        Arrhenius(
            A = (2.180e+09, 'cm^3/(mol*s)'),
        n = 0.06,
        Ea = (12470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.240e-05, 'cm^3/(mol*s)'),
        n = 4.17,
        Ea = (6416.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.000e+49, 'cm^3/(mol*s)'),
        n = -10.18,
        Ea = (77110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 1)
        Arrhenius(
            A = (7.650e+05, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (11340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.16 atm (term 2)
        Arrhenius(
            A = (4.060e+16, 'cm^3/(mol*s)'),
        n = -2.03,
        Ea = (17630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.010e-02, 'cm^3/(mol*s)'),
        n = 3.38,
        Ea = (8696.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (9.380e+16, 'cm^3/(mol*s)'),
        n = -2.03,
        Ea = (19590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 1)
        Arrhenius(
            A = (6.060e-03, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (9217.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 31.6 atm (term 2)
        Arrhenius(
            A = (5.910e+21, 'cm^3/(mol*s)'),
        n = -3.32,
        Ea = (25030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.760e-02, 'cm^3/(mol*s)'),
        n = 3.27,
        Ea = (10760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -60.0

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -56.2
# C2H2+HCO=C2H3+CO
# ## Missing Reaction

entry(
    index = 510,
    label = "CH2 + C2H2 <=> CH2CCH + H",
    kinetics = Arrhenius(
        A = (1.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (6600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, JP Senosiain, SJ Klippenstein, Y Georgievskii, JPCA 112:9429 (2008).
# DH = -23.9
entry(
    index = 511,
    label = "CH2(S) + C2H2 <=> CH2CCH + H",
    kinetics = Arrhenius(
        A = (3.970e+15, 'cm^3/(mol*s)'),
        n = -0.571,
        Ea = (-4.85, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# T Bohland, F Temps, HGg Wagner, PCI 21:841 (1986).
# DH = -11.8
entry(
    index = 512,
    label = "CH + C2H2 <=> CHCCH + H",
    kinetics = Arrhenius(
        A = (5.400e+14, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# D Polino, SJ Klippenstein, LB Harding, Y Georgievskii, JPCA 117:12677 (2013).
# DH = -20.9
entry(
    index = 513,
    label = "CH + C2H2 <=> c-CHCCH + H",
    kinetics = Arrhenius(
        A = (6.000e+13, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# H Thiesemann, J MacNamara, CA Taatjes, JPCA 101:1881 (1997).
# L Vereecken, J Peeters, JPCA, 103:5523 (1999).
# DH = -15.3
entry(
    index = 514,
    label = "HCCO + C2H2 <=> CH2CCH + CO",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (3000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# H Thiesemann, J MacNamara, CA Taatjes, JPCA 101:1881 (1997).
# L Vereecken, J Peeters, JPCA, 103:5523 (1999).
# DH = -26.0
entry(
    index = 515,
    label = "CH2C + C2H2 <=> CH2CHCCH",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(350000.0, 'cm^3/(mol*s)'), n=2.055, Ea=(-2400.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.4e+60, 'cm^6/(mol^2*s)'), n=-12.599, Ea=(7417.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.98,
        T3 = (56.0, 'K'),
        T1 = (580.0, 'K'),
        T2 = (4164.0, 'K'),
        efficiencies = { '[H][H]': 2.0, 'C': 2.0, 'O': 6.0, 'C#C': 3.0, '[C-]#[O+]': 1.5, 'C=C': 3.0, 'CC': 3.0, 'O=C=O': 2.0 }
    ),
    duplicate = True,
)

#entry(
#    index = 516,
#    label = "CH2C + O2 <=> H + H + CO + CO",
#    kinetics = Arrhenius(
#        A = (1.000e+13, 'cm^3/(mol*s)'),
#        n = 0.0,
#        Ea = (0.0, 'cal/mol'),
#        T0 = (1, 'K'),
#    ),
#    
#)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -82.2
entry(
    index = 517,
    label = "CH2C + H <=> C2H2 + H",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -49.4
entry(
    index = 518,
    label = "CH2C + OH <=> CH2CO + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -43.8
entry(
    index = 519,
    label = "C2H2 + H <=> C2H + H2",
    kinetics = Arrhenius(
        A = (1.010e+10, 'cm^3/(mol*s)'),
        n = 1.64,
        Ea = (30302.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -66.6
# *** Fuel Radical + Stable
entry(
    index = 520,
    label = "OH + C2H2 <=> C2H + H2O",
    kinetics = Arrhenius(
        A = (2.630e+06, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17060.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 28.3
entry(
    index = 521,
    label = "C2H + H2O2 <=> C2H2 + HO2",
    kinetics = Arrhenius(
        A = (9.970e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (577.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, JPCA 109:6045 (2005).
# DH = 13.8
entry(
    index = 522,
    label = "C2H + CH4 <=> C2H2 + CH3",
    kinetics = Arrhenius(
        A = (9.970e+09, 'cm^3/(mol*s)'),
        n = 1.1,
        Ea = (577.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# same as C2H + CH4 from
# B Ceursters, HMT Nguyen, J Peeters, MT Nguyen, CPL 329:412 (2000).
# BJ Opansky, SR Leone, JPC 100:4888 (1996).
# DH = -45.5
entry(
    index = 523,
    label = "C2H4 + C2H <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (1.200e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# B Ceursters, HMT Nguyen, J Peeters, MT Nguyen, CPL 329:412 (2000).
# BJ Opansky, SR Leone, JPC 100:4888 (1996).
# DH = -28.2
entry(
    index = 524,
    label = "C2H + C2H2 <=> CHCCCH + H",
    kinetics = Arrhenius(
        A = (2.470e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-391.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -26.6
entry(
    index = 525,
    label = "C2H + O2 <=> CO + CO + H",
    kinetics = Arrhenius(
        A = (2.520e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JOP Pedersen, BJ Opansky, SR Leone, JPC 97:6822 (1993).
# DH = -28.0
# CH3OH+C2H=C2H2+CH2OH
# $$ Missing Reaction
# DH = ??
# CH3OH+C2H=C2H2+CH3O
# $$ Missing Reaction
# DH = ??
# *** Fuel Radical + Radical
entry(
    index = 526,
    label = "C2H + O <=> CH + CO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JW Stephens, JL Hall, H Solka, WB Yan, RF Curl, GP Glass, JPC 91:5740 (1987).
# $$ Baulch (2005).
# DH = -137.2
entry(
    index = 527,
    label = "C2H + OH <=> HCCO + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# WG Browne, RP Porter, JD Verlin, AH Clarke, PCI 12:1035 (1969).
# $$ W Boullart, Boullart W, Devriendt K, Borms R, Peeters J. Identification of the sequence CH (2)+ C2H2 C3H2+ H (and C3H+ H2) followed by C3H2+ O C2H+ HCO (or H+ CO) as C2H source in C2H2/O/H atomic flames. J Phys Chem. 1996;100:998-1007.
# $$ Devriendt K, Peeters J. Direct identification of the C2H (X2+)+ O (3P) CH (A2)+ CO reaction as the source of the CH (A2 X2) chemiluminescence in C2H2/O/H atomic flames. J Phys Chem A. 1997;101:2546-51.
# DH = -79.0
entry(
    index = 528,
    label = "C2H + CH3 <=> CH2CCH + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -49.7
entry(
    index = 529,
    label = "C2H + CH2 <=> CHCCH(S) + H",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -34.1
entry(
    index = 530,
    label = "C2H + CH2 <=> CH2CC + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 531,
    label = "C2H3 + C2H <=> C2H2 + C2H2",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -44.0
entry(
    index = 532,
    label = "C2 + H2 <=> C2H + H",
    kinetics = Arrhenius(
        A = (4.000e+05, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, RE Mitchell, MD Smookte, RJ Kee, PCI 19:181 (1982).
# JA Miller - estimate
# DH = -97.3
# C2H+CH3OH=C2H2+CH2OH
# $$ Missing Reaction
# DH = ??
# C2H+CH3OH=C2H2+CH3O
# $$ Missing Reaction
# DH = ??
# *** C2 Reactions
entry(
    index = 533,
    label = "C2 + O2 <=> CO + CO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -9.4
entry(
    index = 534,
    label = "C2 + OH <=> CCO + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -249.9
# JA Miller - estimate
# DH = -62.8
# *****************************************************************************
#    OCHCHO subset                                                            *
# *****************************************************************************
# Fuel Radicals: OCCHO
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition

entry(
    index = 536,
    label = "OCCHO + O2 <=> CO + CO2 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.600e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.100e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.300e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2075.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        ],
    ),
)

# kinf                                		1.10E+14    0.133   10140
# G da Silva, PCCP 1: 6698 (2010).
# DH = ??
# *** Fuel + Radical

entry(
    index = 537,
    label = "OCHCHO + H <=> CH2O + HCO",
    kinetics = Arrhenius(
        A = (5.400e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4300.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# kinf                                		3.40E+04    1.929     344
# G da Silva, PCCP 1: 6698 (2010).
# DH = ??
entry(
    index = 538,
    label = "OCHCHO + OH <=> OCCHO + H2O",
    kinetics = Arrhenius(
        A = (4.000e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (-1630.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# M Colberg, G Friedrichs, JPCA 110:160 (2006).
# DH = -17.5
entry(
    index = 539,
    label = "OCCHO + H <=> HCO + HCO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# KJ Feierabend, L Zhu, RK Talukdar, JB Burkholder, JPCA 112:73, (2008).
# DH = ??
# Should products be OCH + CO + H2O ??
# *** Fuel Radical + Radical
entry(
    index = 540,
    label = "OCCHO + O <=> CO2 + HCO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -17.1
entry(
    index = 541,
    label = "OCCHO + OH <=> CO2 + CH2O",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -128.2
entry(
    index = 542,
    label = "CH3OCHO <=> CH3OH + CO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1150000000.0, 's^-1'), n=1.576, Ea=(62861.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+38, 'cm^3/(mol*s)'), n=-5.66, Ea=(61103.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.372,
        T3 = (935.2, 'K'),
        T1 = (935.1, 'K'),
        T2 = (159646.0, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 543,
    label = "CH3OCHO <=> CH2O + CH2O",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2990000.0, 's^-1'), n=2.044, Ea=(73389.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.75e+43, 'cm^3/(mol*s)'), n=-7.956, Ea=(81479.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.946,
        T3 = (2000.2, 'K'),
        T1 = (1989.5, 'K'),
        T2 = (376752.0, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 544,
    label = "CH3OCHO <=> CH4 + CO2",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.16, 's^-1'), n=4.05, Ea=(70188.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.56e+40, 'cm^3/(mol*s)'), n=-6.82, Ea=(79076.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.351,
        T3 = (2173.2, 'K'),
        T1 = (2180.9, 'K'),
        T2 = (146864.0, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 545,
    label = "CH2OCHO + H <=> CH3OCHO",
    kinetics = PDepArrhenius(
        pressures = ([0.1, 0.5, 1.0, 2.5, 5.0, 20.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.520e-17, 'cm^3/(mol*s)'),
        n = 7.534,
        Ea = (3116.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.856e+03, 'cm^3/(mol*s)'),
        n = 1.551,
        Ea = (3920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (1.902e+12, 'cm^3/(mol*s)'),
        n = -1.026,
        Ea = (4266.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.899e+23, 'cm^3/(mol*s)'),
        n = -4.432,
        Ea = (4723.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 2.5 atm
        Arrhenius(
            A = (2.910e+32, 'cm^3/(mol*s)'),
        n = -7.009,
        Ea = (5070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 5.0 atm
        Arrhenius(
            A = (2.630e+42, 'cm^3/(mol*s)'),
        n = -9.501,
        Ea = (8994.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 20.0 atm
        Arrhenius(
            A = (1.000e+46, 'cm^3/(mol*s)'),
        n = -10.05,
        Ea = (12223.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# DH = -27.4

entry(
    index = 546,
    label = "CH3OCHO <=> CH3OCO + H",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.66e+29, 's^-1'), n=-4.164, Ea=(105459.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.96e+60, 'cm^3/(mol*s)'), n=-12.416, Ea=(107924.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.093,
        T3 = (756.9, 'K'),
        T1 = (79987.5, 'K'),
        T2 = (4334.1, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 547,
    label = "CH3OCHO + H <=> CH2OCHO + H2",
    kinetics = Arrhenius(
        A = (7.110e+06, 'cm^3/(mol*s)'),
        n = 2.189,
        Ea = (8636.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# ## FISHER, E.M. ET AL., PROC. COMB. INST., VOL. 28, 2000.
# R Sivaramakrishnan estimated
# DH = 98.0
# *** Fuel + Radical
entry(
    index = 548,
    label = "CH3OCHO + H <=> CH3OCO + H2",
    kinetics = Arrhenius(
        A = (1.640e+07, 'cm^3/(mol*s)'),
        n = 1.984,
        Ea = (8111.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SL Peukert, R Sivaramakrishnan, MC Su, JV Michael, CF 159:2312 (2012).
# DH = -4.8
entry(
    index = 549,
    label = "CH3OCHO + O <=> CH2OCHO + OH",
    kinetics = Arrhenius(
        A = (1.480e+00, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (6730.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SL Peukert, R Sivaramakrishnan, MC Su, JV Michael, CF 159:2312 (2012).
# DH = -5.2
entry(
    index = 550,
    label = "CH3OCHO + O <=> CH3OCO + OH",
    kinetics = Arrhenius(
        A = (1.960e+03, 'cm^3/(mol*s)'),
        n = 3.22,
        Ea = (7070.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -3.2
entry(
    index = 551,
    label = "CH3OCHO + OH <=> CH2OCHO + H2O",
    kinetics = Arrhenius(
        A = (2.280e+03, 'cm^3/(mol*s)'),
        n = 2.931,
        Ea = (-172.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -3.7
entry(
    index = 552,
    label = "CH3OCHO + OH <=> CH3OCO + H2O",
    kinetics = Arrhenius(
        A = (5.950e+06, 'cm^3/(mol*s)'),
        n = 1.875,
        Ea = (863.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -19.3
entry(
    index = 553,
    label = "CH3OCHO + CH3 <=> CH2OCHO + CH4",
    kinetics = Arrhenius(
        A = (3.570e+00, 'cm^3/(mol*s)'),
        n = 3.597,
        Ea = (10498.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -19.8
entry(
    index = 554,
    label = "CH3OCHO + CH3 <=> CH3OCO + CH4",
    kinetics = Arrhenius(
        A = (9.380e+01, 'cm^3/(mol*s)'),
        n = 3.262,
        Ea = (8846.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -4.9
entry(
    index = 555,
    label = "CH3OCHO + CH3O <=> CH2OCHO + CH3OH",
    kinetics = Arrhenius(
        A = (4.590e+09, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (4824.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -5.4
entry(
    index = 556,
    label = "CH3OCHO + CH3O <=> CH3OCO + CH3OH",
    kinetics = Arrhenius(
        A = (5.270e+09, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2912.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -5.7
entry(
    index = 557,
    label = "CH3OCHO + CH3OO <=> CH2OCHO + CH3OOH",
    kinetics = Arrhenius(
        A = (7.800e+02, 'cm^3/(mol*s)'),
        n = 3.149,
        Ea = (16737.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -6.1
entry(
    index = 558,
    label = "CH3OCHO + CH3OO <=> CH3OCO + CH3OOH",
    kinetics = Arrhenius(
        A = (5.430e+04, 'cm^3/(mol*s)'),
        n = 2.471,
        Ea = (17080.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -4.0
entry(
    index = 559,
    label = "CH3OCHO + C2H5 <=> CH2OCHO + C2H6",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (10400.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -4.5
entry(
    index = 560,
    label = "CH3OCHO + C2H5 <=> CH3OCO + C2H6",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (10400.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -1.0
entry(
    index = 561,
    label = "CH3OCHO + C2H3 <=> CH2OCHO + C2H4",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (10400.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -1.5
entry(
    index = 562,
    label = "CH3OCHO + C2H3 <=> CH3OCO + C2H4",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (10400.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -10.7
entry(
    index = 563,
    label = "CH3OCO + CH3OCHO <=> CH3OCHO + CH2OCHO",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (10400.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = -11.2
entry(
    index = 564,
    label = "CH2OCHO <=> CH3OCO",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.58e-15, 's^-1'), n=8.497, Ea=(27345.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+26, 'cm^3/(mol*s)'), n=-3.529, Ea=(32711.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.29,
        T3 = (498.7, 'K'),
        T1 = (78603414.8, 'K'),
        T2 = (28615373326.5, 'K'),
        efficiencies = { '[Ar]': 0.7, '[He]': 2.2, '[H][H]': 2.3, '[C-]#[O+]': 1.0, 'C': 2.3, 'COC=O': 2.3, 'O': 6.0 }
    ),
)

entry(
    index = 565,
    label = "CH3OCHO + HO2 <=> CH2OCHO + H2O2",
    kinetics = Arrhenius(
        A = (7.800e+02, 'cm^3/(mol*s)'),
        n = 3.149,
        Ea = (16737.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJK - unpublished; fit by R Sivaramakrishnan, NJ Labbe.
# DH = -0.5
# *** Fuel Radical + Stable
entry(
    index = 566,
    label = "CH3OCHO + HO2 <=> CH3OCO + H2O2",
    kinetics = Arrhenius(
        A = (5.430e+04, 'cm^3/(mol*s)'),
        n = 2.471,
        Ea = (17080.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = 12.4
entry(
    index = 567,
    label = "CH3OCHO + HCO <=> CH2OCHO + CH2O",
    kinetics = Arrhenius(
        A = (1.030e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (18430.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = 11.9
entry(
    index = 568,
    label = "CH3OCHO + HCO <=> CH3OCO + CH2O",
    kinetics = Arrhenius(
        A = (5.400e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = 11.8
entry(
    index = 569,
    label = "H + CH2OCHO <=> CH4 + CO2",
    kinetics = Arrhenius(
        A = (3.840e+12, 'cm^3/(mol*s)'),
        n = -0.026,
        Ea = (581.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimated
# DH = 11.4
# *** Fuel Radical + Radical
entry(
    index = 570,
    label = "H + CH2OCHO <=> CH3OH + CO",
    kinetics = Arrhenius(
        A = (1.220e+18, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (1348.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -125.9
entry(
    index = 571,
    label = "H + CH2OCHO <=> CH2O + CH2O",
    kinetics = Arrhenius(
        A = (9.600e+11, 'cm^3/(mol*s)'),
        n = -0.045,
        Ea = (282.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -88.6
entry(
    index = 572,
    label = "H + CH2OCHO <=> CH3 + OCOH",
    kinetics = Arrhenius(
        A = (1.250e+14, 'cm^3/(mol*s)'),
        n = -0.59,
        Ea = (963.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -66.5
entry(
    index = 573,
    label = "H + CH2OCHO <=> CH3 + H + CO2",
    kinetics = Arrhenius(
        A = (1.940e+14, 'cm^3/(mol*s)'),
        n = -0.071,
        Ea = (920.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -23.5
entry(
    index = 574,
    label = "OH + CH2OCHO <=> H2O + CH2O + CO",
    kinetics = Arrhenius(
        A = (3.010e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -22.5
entry(
    index = 575,
    label = "CH3OCHO + O2 <=> CH2OCHO + HO2",
    kinetics = Arrhenius(
        A = (2.020e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (50875.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -82.9
entry(
    index = 576,
    label = "CH3OCHO + O2 <=> CH3OCO + HO2",
    kinetics = Arrhenius(
        A = (3.850e+12, 'cm^3/(mol*s)'),
        n = 0.113,
        Ea = (50760.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan - estimate
# DH = 50.5
entry(
    index = 577,
    label = "CH2OCHO + CH3 <=> C2H6 + CO2",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.5, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.920e+07, 'cm^3/(mol*s)'),
        n = 0.99,
        Ea = (2319.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (9.560e+07, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (2398.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (1.260e+08, 'cm^3/(mol*s)'),
        n = 0.93,
        Ea = (2506.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.330e+09, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (4172.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.160e+14, 'cm^3/(mol*s)'),
        n = -0.78,
        Ea = (9552.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (7.250e+11, 'cm^3/(mol*s)'),
        n = 0.07,
        Ea = (11866.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# R Sivaramakrishnan - estimate
# DH = 50.0

entry(
    index = 578,
    label = "CH2OCHO + CH3 <=> CH3CH2OH + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.5, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.570e+14, 'cm^3/(mol*s)'),
        n = -0.51,
        Ea = (1368.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (2.600e+14, 'cm^3/(mol*s)'),
        n = -0.51,
        Ea = (1374.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (2.750e+14, 'cm^3/(mol*s)'),
        n = -0.51,
        Ea = (1396.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.480e+16, 'cm^3/(mol*s)'),
        n = -0.99,
        Ea = (2985.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.680e+20, 'cm^3/(mol*s)'),
        n = -2.04,
        Ea = (8257.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (2.530e+14, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (8536.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -110.6

entry(
    index = 579,
    label = "CH3 + CH2OCHO <=> C2H4 + OCHOH",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.250e+30, 'cm^3/(mol*s)'),
        n = -5.18,
        Ea = (9758.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.590e+31, 'cm^3/(mol*s)'),
        n = -5.31,
        Ea = (10136.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.250e+36, 'cm^3/(mol*s)'),
        n = -6.65,
        Ea = (14868.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.790e+38, 'cm^3/(mol*s)'),
        n = -7.05,
        Ea = (20125.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.040e+27, 'cm^3/(mol*s)'),
        n = -3.89,
        Ea = (17212.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -79.3

entry(
    index = 580,
    label = "CH2OCHO + CH3 <=> CH3CHO + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.5, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.130e+08, 'cm^3/(mol*s)'),
        n = 0.68,
        Ea = (1216.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (2.440e+08, 'cm^3/(mol*s)'),
        n = 0.67,
        Ea = (1274.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (2.950e+08, 'cm^3/(mol*s)'),
        n = 0.64,
        Ea = (1350.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.780e+10, 'cm^3/(mol*s)'),
        n = 0.16,
        Ea = (3028.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.470e+14, 'cm^3/(mol*s)'),
        n = -1.03,
        Ea = (8446.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (7.630e+10, 'cm^3/(mol*s)'),
        n = 0.16,
        Ea = (10015.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -74.4

entry(
    index = 581,
    label = "HCO + CH2OCHO <=> CH2CO + OCHOH",
    kinetics = Arrhenius(
        A = (3.010e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -62.4
entry(
    index = 582,
    label = "CH3OCO + H <=> CH4 + CO2",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.5, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.450e+07, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (1554.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (8.540e+07, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (1666.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (1.170e+08, 'cm^3/(mol*s)'),
        n = 1.32,
        Ea = (1791.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.290e+10, 'cm^3/(mol*s)'),
        n = 0.77,
        Ea = (3746.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.390e+14, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (9188.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (5.330e+10, 'cm^3/(mol*s)'),
        n = 0.77,
        Ea = (10770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -73.6

entry(
    index = 583,
    label = "CH3OCO + H <=> CH3OH + CO",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.5, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.320e+15, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (989.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (1.340e+15, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (996.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (1.500e+15, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (1037.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.610e+17, 'cm^3/(mol*s)'),
        n = -0.89,
        Ea = (2956.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.060e+20, 'cm^3/(mol*s)'),
        n = -1.75,
        Ea = (8027.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (3.130e+13, 'cm^3/(mol*s)'),
        n = 0.34,
        Ea = (7436.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -125.4

entry(
    index = 584,
    label = "CH3OCO + H <=> CH2O + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.05, 0.5, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.520e+08, 'cm^3/(mol*s)'),
        n = 1.0,
        Ea = (563.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.05 atm
        Arrhenius(
            A = (4.250e+08, 'cm^3/(mol*s)'),
        n = 0.98,
        Ea = (641.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.5 atm
        Arrhenius(
            A = (5.400e+08, 'cm^3/(mol*s)'),
        n = 0.95,
        Ea = (740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.310e+10, 'cm^3/(mol*s)'),
        n = 0.39,
        Ea = (2724.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.110e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (8112.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (6.350e+09, 'cm^3/(mol*s)'),
        n = 0.85,
        Ea = (8876.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -88.2

entry(
    index = 585,
    label = "CH3OCO + H <=> CH3 + H + CO2",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.840e+15, 'cm^3/(mol*s)'),
        n = -0.44,
        Ea = (3809.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (5.040e+15, 'cm^3/(mol*s)'),
        n = -0.44,
        Ea = (3823.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.530e+15, 'cm^3/(mol*s)'),
        n = -0.51,
        Ea = (4032.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.360e+17, 'cm^3/(mol*s)'),
        n = -1.0,
        Ea = (5719.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.200e+22, 'cm^3/(mol*s)'),
        n = -2.22,
        Ea = (10892.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -66.0

entry(
    index = 586,
    label = "CH3OCO + CH3 <=> CH3OH + CH2CO",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.120e+38, 'cm^3/(mol*s)'),
        n = -7.23,
        Ea = (16278.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (5.640e+39, 'cm^3/(mol*s)'),
        n = -7.66,
        Ea = (18957.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.930e+39, 'cm^3/(mol*s)'),
        n = -7.52,
        Ea = (23491.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.510e+31, 'cm^3/(mol*s)'),
        n = -5.08,
        Ea = (22891.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.220e+15, 'cm^3/(mol*s)'),
        n = -0.45,
        Ea = (16410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -22.0

entry(
    index = 587,
    label = "CH3OCO + CH3 <=> CH3CHO + CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.930e+30, 'cm^3/(mol*s)'),
        n = -5.67,
        Ea = (14657.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.090e+33, 'cm^3/(mol*s)'),
        n = -6.28,
        Ea = (17641.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.000e+35, 'cm^3/(mol*s)'),
        n = -6.74,
        Ea = (23467.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.880e+29, 'cm^3/(mol*s)'),
        n = -4.9,
        Ea = (24412.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.790e+14, 'cm^3/(mol*s)'),
        n = -0.63,
        Ea = (18985.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -56.0

entry(
    index = 588,
    label = "CH3C(O)O + CH3 <=> CH3OCO + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.670e+25, 'cm^3/(mol*s)'),
        n = -3.5,
        Ea = (16091.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (3.600e+28, 'cm^3/(mol*s)'),
        n = -4.28,
        Ea = (18901.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.160e+35, 'cm^3/(mol*s)'),
        n = -6.07,
        Ea = (26694.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.800e+36, 'cm^3/(mol*s)'),
        n = -6.31,
        Ea = (32135.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.340e+27, 'cm^3/(mol*s)'),
        n = -3.72,
        Ea = (31145.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = -61.9

entry(
    index = 589,
    label = "CH3CHCHO <=> CH2CH2CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.230e+65, 's^-1'),
        n = -18.01,
        Ea = (51500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (9.430e+16, 's^-1'),
        n = -3.28,
        Ea = (31950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.430e+27, 's^-1'),
        n = -5.88,
        Ea = (38110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (5.640e+02, 's^-1'),
        n = -7.68,
        Ea = (-2367.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (3.530e+21, 's^-1'),
        n = -3.61,
        Ea = (37880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (3.420e-01, 's^-1'),
        n = -8.98,
        Ea = (-11240.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (1.440e+12, 's^-1'),
        n = -0.53,
        Ea = (35290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.440e+12, 's^-1'),
        n = -0.53,
        Ea = (35290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (1.360e+34, 's^-1'),
        n = -6.67,
        Ea = (47410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.680e+01, 's^-1'),
        n = 2.48,
        Ea = (29880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.110e+20, 's^-1'),
        n = -2.19,
        Ea = (42780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (6.700e-08, 's^-1'),
        n = 5.27,
        Ea = (27820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# NJ Labbe, R Sivaramakrishnan, SJ Klippenstein, PCI 35:447 (2015).
# DH = 7.4
# *****************************************************************************
#    CH3CH2CHO subset                                                         *
#    CH3CHCHOH subset                                                         *
# *****************************************************************************
# Fuel Radicals: CH3CHCHO,CH2CH2CHO,CH2CHCHOH
# New Radicals Formed:
# New Fuels:
# *** Fuel + Radical
# *** Fuel Radical Decompositiona

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 11.3

entry(
    index = 591,
    label = "CH3CHCHO <=> CH3CHCO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.140e+54, 's^-1'),
        n = -13.74,
        Ea = (61230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (9.500e+40, 's^-1'),
        n = -10.18,
        Ea = (52990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (9.850e+55, 's^-1'),
        n = -13.82,
        Ea = (63040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.000e+42, 's^-1'),
        n = -10.07,
        Ea = (53880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (1.150e+58, 's^-1'),
        n = -14.03,
        Ea = (65370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (7.920e+35, 's^-1'),
        n = -7.68,
        Ea = (53180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (3.420e+55, 's^-1'),
        n = -12.85,
        Ea = (66370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.100e+32, 's^-1'),
        n = -6.22,
        Ea = (52730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (1.870e+50, 's^-1'),
        n = -10.89,
        Ea = (66680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (3.680e+29, 's^-1'),
        n = -5.31,
        Ea = (52430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.310e+45, 's^-1'),
        n = -9.08,
        Ea = (67080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (4.870e+23, 's^-1'),
        n = -3.29,
        Ea = (51230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 4.1

entry(
    index = 592,
    label = "CH3CHCHO <=> CH2CHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.840e+57, 's^-1'),
        n = -14.12,
        Ea = (56780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (4.760e+41, 's^-1'),
        n = -9.85,
        Ea = (47390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (3.140e+55, 's^-1'),
        n = -13.24,
        Ea = (57460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (3.720e+39, 's^-1'),
        n = -8.95,
        Ea = (47300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (3.540e+55, 's^-1'),
        n = -12.93,
        Ea = (59340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (1.450e+32, 's^-1'),
        n = -6.32,
        Ea = (46030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (6.490e+51, 's^-1'),
        n = -11.47,
        Ea = (59960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (3.030e+28, 's^-1'),
        n = -5.01,
        Ea = (45400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (4.140e+47, 's^-1'),
        n = -9.93,
        Ea = (60640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (5.820e+24, 's^-1'),
        n = -3.71,
        Ea = (44740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (2.820e+42, 's^-1'),
        n = -8.17,
        Ea = (60720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (4.190e+19, 's^-1'),
        n = -1.96,
        Ea = (43630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 42.8
# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 41.8

entry(
    index = 594,
    label = "CH2CH2CHO <=> CH3CHCO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.120e+31, 's^-1'),
        n = -7.95,
        Ea = (41520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (5.780e+14, 's^-1'),
        n = -7.63,
        Ea = (20440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (4.940e+92, 's^-1'),
        n = -26.87,
        Ea = (64940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.170e+24, 's^-1'),
        n = -5.26,
        Ea = (39530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (3.960e+62, 's^-1'),
        n = -16.81,
        Ea = (55590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (5.440e+22, 's^-1'),
        n = -4.41,
        Ea = (39660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (6.680e+50, 's^-1'),
        n = -12.52,
        Ea = (53690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.290e+20, 's^-1'),
        n = -3.2,
        Ea = (40060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (7.900e+35, 's^-1'),
        n = -7.38,
        Ea = (51140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (4.000e+19, 's^-1'),
        n = -2.96,
        Ea = (41060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (2.300e+27, 's^-1'),
        n = -4.42,
        Ea = (51930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (4.790e+04, 's^-1'),
        n = 1.93,
        Ea = (38490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -7.3

entry(
    index = 595,
    label = "CH2CH2CHO <=> CH2CHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.730e+30, 's^-1'),
        n = -7.11,
        Ea = (35440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (4.430e+17, 's^-1'),
        n = -5.37,
        Ea = (24600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.710e+72, 's^-1'),
        n = -20.02,
        Ea = (52720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.960e+21, 's^-1'),
        n = -4.0,
        Ea = (33070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (2.480e+54, 's^-1'),
        n = -13.85,
        Ea = (48120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (2.180e+20, 's^-1'),
        n = -3.35,
        Ea = (34010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (3.310e+49, 's^-1'),
        n = -11.88,
        Ea = (48380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (2.080e+21, 's^-1'),
        n = -3.28,
        Ea = (36010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (2.400e+36, 's^-1'),
        n = -7.35,
        Ea = (45250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (2.380e+24, 's^-1'),
        n = -4.11,
        Ea = (37530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.470e+31, 's^-1'),
        n = -5.44,
        Ea = (45500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (7.730e+17, 's^-1'),
        n = -1.8,
        Ea = (36450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 31.0

entry(
    index = 596,
    label = "CH2CHCHOH <=> CH3CHCO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.530e+51, 's^-1'),
        n = -13.03,
        Ea = (55550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (5.470e+40, 's^-1'),
        n = -10.2,
        Ea = (49190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.580e+53, 's^-1'),
        n = -13.15,
        Ea = (57870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.010e+42, 's^-1'),
        n = -10.1,
        Ea = (50610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (5.490e+57, 's^-1'),
        n = -13.97,
        Ea = (62920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (3.170e+33, 's^-1'),
        n = -6.92,
        Ea = (50310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (2.500e+47, 's^-1'),
        n = -10.44,
        Ea = (62170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (8.340e+28, 's^-1'),
        n = -5.47,
        Ea = (50180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (8.400e+35, 's^-1'),
        n = -6.81,
        Ea = (60330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.490e+25, 's^-1'),
        n = -4.48,
        Ea = (49740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (3.650e+34, 's^-1'),
        n = -6.2,
        Ea = (65150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (4.280e+10, 's^-1'),
        n = 0.2,
        Ea = (47100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 30.5

entry(
    index = 597,
    label = "CH2CHCHOH <=> CH2CHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.380e+54, 's^-1'),
        n = -13.54,
        Ea = (51510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (1.480e+42, 's^-1'),
        n = -10.09,
        Ea = (44170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.020e+55, 's^-1'),
        n = -13.27,
        Ea = (54360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (5.120e+40, 's^-1'),
        n = -9.35,
        Ea = (45320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (3.400e+54, 's^-1'),
        n = -12.66,
        Ea = (57640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (4.570e+29, 's^-1'),
        n = -5.61,
        Ea = (44060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (4.460e+44, 's^-1'),
        n = -9.41,
        Ea = (56850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (3.490e+29, 's^-1'),
        n = -5.8,
        Ea = (44590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (4.680e+32, 's^-1'),
        n = -5.7,
        Ea = (54740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (3.850e+21, 's^-1'),
        n = -3.42,
        Ea = (43120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (4.580e+33, 's^-1'),
        n = -5.79,
        Ea = (60970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (7.260e+05, 's^-1'),
        n = 1.67,
        Ea = (40280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 38.2

entry(
    index = 598,
    label = "C3H8 + H <=> CH3CHCH3 + H2",
    kinetics = Arrhenius(
        A = (5.080e+06, 'cm^3/(mol*s)'),
        n = 2.22,
        Ea = (4957.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 35:181 (2015).
# *****************************************************************************
#    C3H8 subset                                                              *
# *****************************************************************************
# Fuel Radicals: CH3CHCH3,CH3CH2CH2
# New Radicals Formed: CH3CH(OO)CH3,CH3CH2CH2OO
# New Fuels:
# *** Fuel + Radical
entry(
    index = 599,
    label = "C3H8 + H <=> CH3CH2CH2 + H2",
    kinetics = Arrhenius(
        A = (9.630e+06, 'cm^3/(mol*s)'),
        n = 2.25,
        Ea = (7428.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, JV Michael, B Ruscic, IJCK 44:194 (2012).
# DH = -6.6
entry(
    index = 600,
    label = "C3H8 + O <=> CH3CHCH3 + OH",
    kinetics = Arrhenius(
        A = (5.480e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3139.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, JV Michael, B Ruscic, IJCK 44:194 (2012).
# DH = -3.5
entry(
    index = 601,
    label = "C3H8 + O <=> CH3CH2CH2 + OH",
    kinetics = Arrhenius(
        A = (3.730e+06, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5504.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# N Cohen, KR Westberg, IJCK 18:99 (1986).
# DH = -5.0
entry(
    index = 602,
    label = "C3H8 + OH <=> CH3CHCH3 + H2O",
    kinetics = Arrhenius(
        A = (1.980e+07, 'cm^3/(mol*s)'),
        n = 1.751,
        Ea = (-64.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# N Cohen, KR Westberg, IJCK 18:99 (1986).
# DH = -1.9
entry(
    index = 603,
    label = "C3H8 + OH <=> CH3CH2CH2 + H2O",
    kinetics = Arrhenius(
        A = (2.730e+07, 'cm^3/(mol*s)'),
        n = 1.813,
        Ea = (868.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, JV Michael, JPCA 113:5047 (2009).
# DH = -21.1
entry(
    index = 604,
    label = "C3H8 + CH3 <=> CH3CHCH3 + CH4",
    kinetics = Arrhenius(
        A = (1.510e+00, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (5480.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# R Sivaramakrishnan, JV Michael, JPCA 113:5047 (2009).
# DH = -18.0
entry(
    index = 605,
    label = "C3H8 + CH3 <=> CH3CH2CH2 + CH4",
    kinetics = Arrhenius(
        A = (9.040e-01, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (7153.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -6.7
entry(
    index = 606,
    label = "C3H8 + C2H5 <=> CH3CHCH3 + C2H6",
    kinetics = Arrhenius(
        A = (1.510e+00, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (7470.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -3.6
entry(
    index = 607,
    label = "C3H8 + C2H3 <=> CH3CHCH3 + C2H4",
    kinetics = Arrhenius(
        A = (1.000e+03, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (8830.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -2.8
entry(
    index = 608,
    label = "C3H8 + C2H3 <=> CH3CH2CH2 + C2H4",
    kinetics = Arrhenius(
        A = (6.000e+02, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (10500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -12.5
entry(
    index = 609,
    label = "CH3CHCH2 + H <=> CH3CHCH3",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.350e+44, 'cm^3/(mol*s)'),
        n = -10.678,
        Ea = (8196.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 1)
        Arrhenius(
            A = (3.400e+38, 'cm^3/(mol*s)'),
        n = -32.584,
        Ea = (136140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 2)
        Arrhenius(
            A = (2.110e+57, 'cm^3/(mol*s)'),
        n = -14.227,
        Ea = (15147.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 1)
        Arrhenius(
            A = (2.250e+29, 'cm^3/(mol*s)'),
        n = -5.843,
        Ea = (4242.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 2)
        Arrhenius(
            A = (3.260e+61, 'cm^3/(mol*s)'),
        n = -14.944,
        Ea = (20161.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.060e+30, 'cm^3/(mol*s)'),
        n = -5.632,
        Ea = (5613.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (5.300e+56, 'cm^3/(mol*s)'),
        n = -13.122,
        Ea = (20667.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (6.110e+26, 'cm^3/(mol*s)'),
        n = -4.442,
        Ea = (5182.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.110e+50, 'cm^3/(mol*s)'),
        n = -10.803,
        Ea = (20202.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.730e+23, 'cm^3/(mol*s)'),
        n = -3.261,
        Ea = (4598.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# W Tsang, JPCRD 17:887 (1988).
# DH = -9.4
# *** Fuel Radical Decomposition
# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = -34.8

entry(
    index = 611,
    label = "C3H8 + HO2 <=> CH3CHCH3 + H2O2",
    kinetics = Arrhenius(
        A = (6.320e+00, 'cm^3/(mol*s)'),
        n = 3.67,
        Ea = (13416.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = -34.8
# *** Fuel Radical + Stable
entry(
    index = 612,
    label = "C3H8 + HO2 <=> CH3CH2CH2 + H2O2",
    kinetics = Arrhenius(
        A = (2.700e-01, 'cm^3/(mol*s)'),
        n = 4.125,
        Ea = (15176.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# H Hashemi, JM Christensen, LB Harding, SJ Klippenstein, P Glarborg, PCI 37:461 (2019).
# DH = 10.6
entry(
    index = 613,
    label = "C3H8 + C2H5 <=> CH3CH2CH2 + C2H6",
    kinetics = Arrhenius(
        A = (9.030e-01, 'cm^3/(mol*s)'),
        n = 3.65,
        Ea = (9140.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# H Hashemi, JM Christensen, LB Harding, SJ Klippenstein, P Glarborg, PCI 37:461 (2019).
# DH = 13.7
entry(
    index = 614,
    label = "C3H8 + CH2CHCH2 <=> CH3CHCH2 + CH3CH2CH2",
    kinetics = Arrhenius(
        A = (2.350e+02, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (19842.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = 0.3
entry(
    index = 615,
    label = "C3H8 + CH2CHCH2 <=> CH3CHCH2 + CH3CHCH3",
    kinetics = Arrhenius(
        A = (7.830e+01, 'cm^3/(mol*s)'),
        n = 3.3,
        Ea = (18169.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = 13.5
entry(
    index = 616,
    label = "O2 + CH3CHCH3 <=> CH3CH(OO)CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.330e+05, 'cm^3/(mol*s)'),
        n = 1.33,
        Ea = (-6346.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.240e+11, 'cm^3/(mol*s)'),
        n = -0.105,
        Ea = (-3698.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.540e+18, 'cm^3/(mol*s)'),
        n = -2.02,
        Ea = (-499.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.740e+27, 'cm^3/(mol*s)'),
        n = -4.85,
        Ea = (3780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.670e+29, 'cm^3/(mol*s)'),
        n = -5.15,
        Ea = (5036.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# W Tsang, JPCRD 17:887 (1988).
# DH = 10.3
# *** Fuel Radical + Radical

entry(
    index = 617,
    label = "O2 + CH3CHCH3 <=> CH3CH(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.860e+10, 'cm^3/(mol*s)'),
        n = -1.56,
        Ea = (-708.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.760e+11, 'cm^3/(mol*s)'),
        n = -1.48,
        Ea = (470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.080e+12, 'cm^3/(mol*s)'),
        n = -1.45,
        Ea = (2169.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.130e+14, 'cm^3/(mol*s)'),
        n = -1.5,
        Ea = (5253.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.560e+10, 'cm^3/(mol*s)'),
        n = -0.116,
        Ea = (7056.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 618,
    label = "O2 + CH3CHCH3 <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.910e+09, 'cm^3/(mol*s)'),
        n = 0.428,
        Ea = (-1439.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.600e+14, 'cm^3/(mol*s)'),
        n = -0.845,
        Ea = (1424.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.050e+18, 'cm^3/(mol*s)'),
        n = -2.07,
        Ea = (4971.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.910e+17, 'cm^3/(mol*s)'),
        n = -1.66,
        Ea = (6964.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (9.840e+07, 'cm^3/(mol*s)'),
        n = 1.34,
        Ea = (5379.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 619,
    label = "O2 + CH3CHCH3 <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.430e+02, 'cm^3/(mol*s)'),
        n = 2.04,
        Ea = (-2163.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.030e+07, 'cm^3/(mol*s)'),
        n = 0.708,
        Ea = (692.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.000e+13, 'cm^3/(mol*s)'),
        n = -1.03,
        Ea = (5015.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.810e+18, 'cm^3/(mol*s)'),
        n = -2.31,
        Ea = (10119.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.350e+14, 'cm^3/(mol*s)'),
        n = -0.832,
        Ea = (12601.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = -13.2

entry(
    index = 620,
    label = "CH3CHCH3 + H <=> C2H5 + CH3",
    kinetics = Arrhenius(
        A = (1.660e+13, 'cm^3/(mol*s)'),
        n = 0.22,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = -33.9
entry(
    index = 621,
    label = "CH3CHCH3 + O <=> CH3CHO + CH3",
    kinetics = Arrhenius(
        A = (4.560e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# LB Harding, Y Georgievskii, SJ Klippenstein, JPCA 109:4646 (2005).
# DH = -9.6
entry(
    index = 622,
    label = "CH3CHCH3 + O <=> CH3C(O)CH3 + H",
    kinetics = Arrhenius(
        A = (4.100e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# K Hoyermann, M Olzmann, O Wlez, T Zeuch, PCI 33:283 (2011).
# DH = -85.4
entry(
    index = 623,
    label = "CH3CHCH3 + O <=> CH3CHCH2 + OH",
    kinetics = Arrhenius(
        A = (2.740e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# K Hoyermann, M Olzmann, O Wlez, T Zeuch, PCI 33:283 (2011).
# DH = -80.4
entry(
    index = 624,
    label = "CH3CHCH3 + OH <=> CH3CHCH2 + H2O",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# K Hoyermann, M Olzmann, O Wlez, T Zeuch, PCI 33:283 (2011).
# DH = -66.9
entry(
    index = 625,
    label = "CH3CHCH3 + OH <=> CH3CHOH + CH3",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -83.0
entry(
    index = 626,
    label = "CH3CHCH3 + HO2 <=> CH3CHCH2 + H2O2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -8.6
entry(
    index = 627,
    label = "C3H8 + O2 <=> CH3CHCH3 + HO2",
    kinetics = Arrhenius(
        A = (3.970e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (47700.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 48.7
entry(
    index = 628,
    label = "CH3CHCH3 + HO2 <=> CH3CHO + CH3 + OH",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = 48.7
entry(
    index = 629,
    label = "CH3CHCH3 + HO2 <=> OH + CH3CH(O)CH3",
    kinetics = Arrhenius(
        A = (1.650e+17, 'cm^3/(mol*s)'),
        n = -1.456,
        Ea = (216.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -20.9
entry(
    index = 630,
    label = "O2 + CH3CH2CH2 <=> CH3CH2CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.200e+08, 'cm^3/(mol*s)'),
        n = 0.405,
        Ea = (-4399.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.450e+14, 'cm^3/(mol*s)'),
        n = -0.984,
        Ea = (-1711.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.090e+13, 'cm^3/(mol*s)'),
        n = -0.499,
        Ea = (-938.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.150e+20, 'cm^3/(mol*s)'),
        n = -2.42,
        Ea = (2451.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.070e+16, 'cm^3/(mol*s)'),
        n = -1.3,
        Ea = (803.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# E Kamarchik, AW Jasper - unpublished (2013).
# DH = -25.7

entry(
    index = 631,
    label = "O2 + CH3CH2CH2 <=> CH3CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.970e+15, 'cm^3/(mol*s)'),
        n = -2.84,
        Ea = (3567.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.640e+12, 'cm^3/(mol*s)'),
        n = -1.58,
        Ea = (3362.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.780e+02, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-492.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.300e+14, 'cm^3/(mol*s)'),
        n = -1.73,
        Ea = (5164.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.630e+16, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (9036.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 632,
    label = "O2 + CH3CH2CH2 <=> CH2CH2CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.090e+146, 'cm^3/(mol*s)'),
        n = -45.9,
        Ea = (31282.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (6.190e+08, 'cm^3/(mol*s)'),
        n = 0.878,
        Ea = (11187.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.260e+47, 'cm^3/(mol*s)'),
        n = -12.4,
        Ea = (8203.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.120e+14, 'cm^3/(mol*s)'),
        n = -0.531,
        Ea = (13897.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.300e+23, 'cm^3/(mol*s)'),
        n = -4.03,
        Ea = (5089.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.070e+14, 'cm^3/(mol*s)'),
        n = -0.4,
        Ea = (15158.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.940e-18, 'cm^3/(mol*s)'),
        n = 8.88,
        Ea = (-6200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.020e+21, 'cm^3/(mol*s)'),
        n = -2.26,
        Ea = (18554.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.580e-15, 'cm^3/(mol*s)'),
        n = 7.8,
        Ea = (-3431.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.050e+15, 'cm^3/(mol*s)'),
        n = -0.486,
        Ea = (15877.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 633,
    label = "O2 + CH3CH2CH2 <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.050e+10, 'cm^3/(mol*s)'),
        n = 0.021,
        Ea = (502.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.470e+15, 'cm^3/(mol*s)'),
        n = -1.45,
        Ea = (4113.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.180e+19, 'cm^3/(mol*s)'),
        n = -2.35,
        Ea = (7299.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.630e+00, 'cm^3/(mol*s)'),
        n = 3.46,
        Ea = (2481.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.370e+02, 'cm^3/(mol*s)'),
        n = 2.71,
        Ea = (5496.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 634,
    label = "O2 + CH3CH2CH2 <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.980e+07, 'cm^3/(mol*s)'),
        n = 0.596,
        Ea = (-64.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.970e+13, 'cm^3/(mol*s)'),
        n = -0.939,
        Ea = (3664.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.730e+17, 'cm^3/(mol*s)'),
        n = -2.05,
        Ea = (7251.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.350e+02, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (4697.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.050e+08, 'cm^3/(mol*s)'),
        n = 0.919,
        Ea = (11048.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = -16.3

entry(
    index = 635,
    label = "CH3CH2CH2 + H <=> C2H5 + CH3",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = -37.1
entry(
    index = 636,
    label = "CH3CH2CH2 + O <=> CH3CH2CHO + H",
    kinetics = Arrhenius(
        A = (8.570e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -12.7
entry(
    index = 637,
    label = "CH3CH2CH2 + O <=> C2H5 + CH2O",
    kinetics = Arrhenius(
        A = (1.430e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -76.4
entry(
    index = 638,
    label = "CH3CH2CH2 + OH <=> CH3CHCH2 + H2O",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -81.2
entry(
    index = 639,
    label = "CH3CH2CH2 + OH <=> CH2OH + C2H5",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -86.1
entry(
    index = 640,
    label = "CH3CH2CH2 + OH <=> CH2CH2OH + CH3",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -8.4
entry(
    index = 641,
    label = "C3H8 + O2 <=> CH3CH2CH2 + HO2",
    kinetics = Arrhenius(
        A = (3.970e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (50900.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -4.3
entry(
    index = 642,
    label = "CH3CH2CH2 + HO2 <=> CH3CHCH2 + H2O2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = 51.8
entry(
    index = 643,
    label = "CH3CH2CH2 + HO2 <=> C2H5 + OH + CH2O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# E Kamarchik, AW Jasper - unpublished (2013).
# DH = -54.5
entry(
    index = 644,
    label = "CH3CH2CH2 + HO2 <=> OH + CH3CH2CH2O",
    kinetics = Arrhenius(
        A = (2.580e+16, 'cm^3/(mol*s)'),
        n = -1.178,
        Ea = (115.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 17:887 (1988).
# DH = -16.7
entry(
    index = 645,
    label = "CH3CH2CH2 + CH3 <=> C2H5 + C2H5",
    kinetics = Arrhenius(
        A = (1.840e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-769.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# E Kamarchik, AW Jasper - unpublished (2013).
# DH = -25.6
entry(
    index = 646,
    label = "CH3CH2CHOH <=> CH3CHCHOH + H",
    kinetics = Arrhenius(
        A = (1.260e+11, 's^-1'),
        n = 0.85,
        Ea = (37100.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# VD Knyazev, IR Slagle JPCA 105:6490 (2001).
# DH = -1.3
# *****************************************************************************
#    CH3CH2CH2OH subset                                                       *
#    CH3CH(OH)CH3 subset                                                      *
# *****************************************************************************
# Fuel Radicals: CH3CHCH3,CH3CH2CH2
# New Radicals Formed: CH3CH(OO)CH3,CH3CH2CH2OO
# New Fuels:
# *** Fuel Radical Decomposition
entry(
    index = 647,
    label = "CH3CH2CHOH <=> CH3CH2CHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.370e+31, 's^-1'),
        n = -6.82,
        Ea = (33800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.760e+38, 's^-1'),
        n = -8.33,
        Ea = (39500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.920e+41, 's^-1'),
        n = -9.05,
        Ea = (43800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.470e+41, 's^-1'),
        n = -8.64,
        Ea = (46300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.510e+35, 's^-1'),
        n = -6.61,
        Ea = (45400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 33.0

entry(
    index = 648,
    label = "CH3CHCH2OH <=> CH3CHCHOH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.170e-02, 's^-1'),
        n = 2.07,
        Ea = (16800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (7.840e+17, 's^-1'),
        n = -2.89,
        Ea = (28000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.330e+32, 's^-1'),
        n = -6.49,
        Ea = (38500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.520e+35, 's^-1'),
        n = -7.06,
        Ea = (43300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.380e+30, 's^-1'),
        n = -5.34,
        Ea = (43300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 24.2

entry(
    index = 649,
    label = "CH3CHCH2OH <=> CH2CHCH2OH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.440e-15, 's^-1'),
        n = 5.91,
        Ea = (14100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (3.950e+09, 's^-1'),
        n = -0.47,
        Ea = (25900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.360e+28, 's^-1'),
        n = -5.24,
        Ea = (38300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.570e+37, 's^-1'),
        n = -7.39,
        Ea = (46700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.780e+37, 's^-1'),
        n = -6.92,
        Ea = (50200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 29.1

entry(
    index = 650,
    label = "CH3CHCH2OH <=> CH3CHCH2 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.480e+28, 's^-1'),
        n = -5.71,
        Ea = (26300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (2.320e+32, 's^-1'),
        n = -6.53,
        Ea = (30200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.510e+33, 's^-1'),
        n = -6.46,
        Ea = (32400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.100e+30, 's^-1'),
        n = -5.28,
        Ea = (32600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.750e+23, 's^-1'),
        n = -3.22,
        Ea = (30600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True,
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 35.3

entry(
    index = 651,
    label = "CH2CH2CH2OH <=> CH2CHCH2OH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.370e+31, 's^-1'),
        n = -6.82,
        Ea = (33800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.760e+38, 's^-1'),
        n = -8.33,
        Ea = (39500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.920e+41, 's^-1'),
        n = -9.05,
        Ea = (43800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.470e+41, 's^-1'),
        n = -8.64,
        Ea = (46300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.510e+35, 's^-1'),
        n = -6.61,
        Ea = (45400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 26.7

entry(
    index = 652,
    label = "CH2CH2CH2OH <=> CH3CHCH2 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.390e+22, 's^-1'),
        n = -4.8,
        Ea = (28700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.810e+31, 's^-1'),
        n = -6.76,
        Ea = (35800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.160e+37, 's^-1'),
        n = -8.17,
        Ea = (41900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.300e+40, 's^-1'),
        n = -8.78,
        Ea = (46800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.570e+38, 's^-1'),
        n = -7.85,
        Ea = (48600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 33.3

entry(
    index = 653,
    label = "CH2CH2CH2OH <=> CH3CHCH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.000e-04, 's^-1'),
        n = 1.0,
        Ea = (10000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.010e+39, 's^-1'),
        n = -8.34,
        Ea = (38200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.670e+41, 's^-1'),
        n = -8.8,
        Ea = (41900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.960e+40, 's^-1'),
        n = -8.21,
        Ea = (43700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.540e+34, 's^-1'),
        n = -6.18,
        Ea = (42500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 24.7

entry(
    index = 654,
    label = "CH3CH2CH2O <=> CH3CH2CHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.000e-04, 's^-1'),
        n = 1.0,
        Ea = (10000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (3.140e+05, 's^-1'),
        n = 0.32,
        Ea = (13900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.720e+19, 's^-1'),
        n = -3.41,
        Ea = (18000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.440e+29, 's^-1'),
        n = -5.92,
        Ea = (22200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.930e+35, 's^-1'),
        n = -7.31,
        Ea = (26400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = -2.0

entry(
    index = 655,
    label = "CH3CH(OH)CH2 <=> CH3CHCH2 + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.000e+28, 's^-1'),
        n = -5.92,
        Ea = (26600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (3.170e+33, 's^-1'),
        n = -6.86,
        Ea = (30500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.290e+35, 's^-1'),
        n = -7.02,
        Ea = (33100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.990e+32, 's^-1'),
        n = -6.09,
        Ea = (33700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.490e+26, 's^-1'),
        n = -4.08,
        Ea = (32100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True,
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 13.7

entry(
    index = 656,
    label = "CH3C(OH)CH3 <=> CH3C(OH)CH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.480e+14, 's^-1'),
        n = -2.41,
        Ea = (25500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.910e+31, 's^-1'),
        n = -6.54,
        Ea = (37600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.480e+38, 's^-1'),
        n = -8.14,
        Ea = (44400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.660e+41, 's^-1'),
        n = -8.53,
        Ea = (49400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.810e+35, 's^-1'),
        n = -6.59,
        Ea = (49300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 9.0

entry(
    index = 657,
    label = "CH3C(OH)CH3 <=> CH3C(O)CH3 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.830e+32, 's^-1'),
        n = -6.98,
        Ea = (32800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (1.930e+38, 's^-1'),
        n = -8.12,
        Ea = (38000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.570e+40, 's^-1'),
        n = -8.34,
        Ea = (41300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.010e+37, 's^-1'),
        n = -7.25,
        Ea = (42200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.300e+29, 's^-1'),
        n = -4.72,
        Ea = (39700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 34.0

entry(
    index = 658,
    label = "CH3CH(O)CH3 <=> CH3C(O)CH3 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00526, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.260e+04, 's^-1'),
        n = 0.15,
        Ea = (8990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00526 atm
        Arrhenius(
            A = (2.910e+14, 's^-1'),
        n = -2.31,
        Ea = (13000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.130e+21, 's^-1'),
        n = -4.18,
        Ea = (16000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.640e+28, 's^-1'),
        n = -5.79,
        Ea = (19200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.370e+34, 's^-1'),
        n = -7.02,
        Ea = (22800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 22.5

entry(
    index = 659,
    label = "CH3CH2CH2OO <=> CH3CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.480e+20, 's^-1'),
        n = -5.14,
        Ea = (23710.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.240e+22, 's^-1'),
        n = -4.93,
        Ea = (26478.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.990e+20, 's^-1'),
        n = -3.92,
        Ea = (27634.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.580e+42, 's^-1'),
        n = -10.3,
        Ea = (37670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.790e+42, 's^-1'),
        n = -10.1,
        Ea = (39108.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 34:519 (2013).
# DH = 9.9
# *****************************************************************************
#    CH3CH2CH2OOH subset                                                      *
#    CH3CH(OOH)CH3 subset                                                     *
# *****************************************************************************
# *** Fuel Radical Decomposition

entry(
    index = 660,
    label = "CH3CH2CH2OO <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.300e+53, 's^-1'),
        n = -14.0,
        Ea = (39526.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (9.520e+57, 's^-1'),
        n = -15.0,
        Ea = (42684.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.900e+33, 's^-1'),
        n = -7.03,
        Ea = (36543.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.550e+16, 's^-1'),
        n = -1.22,
        Ea = (32480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.260e+32, 's^-1'),
        n = -6.22,
        Ea = (37948.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 661,
    label = "CH3CH2CH2OO <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.090e+47, 's^-1'),
        n = -12.6,
        Ea = (36677.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.450e+52, 's^-1'),
        n = -13.7,
        Ea = (40634.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.590e+33, 's^-1'),
        n = -7.28,
        Ea = (37564.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.280e+21, 's^-1'),
        n = -2.88,
        Ea = (37343.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.930e+33, 's^-1'),
        n = -6.68,
        Ea = (43797.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 663,
    label = "CH3CHCH2OOH <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.490e-15, 's^-1'),
        n = 9.24,
        Ea = (18961.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.900e-44, 's^-1'),
        n = 17.6,
        Ea = (1889.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.080e+31, 's^-1'),
        n = -4.56,
        Ea = (32123.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.160e-09, 's^-1'),
        n = 7.46,
        Ea = (14746.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.270e-15, 's^-1'),
        n = 8.78,
        Ea = (9266.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# Refit by SJK to remove large values at high T
# DH = ??

entry(
    index = 664,
    label = "CH3CHCH2OOH <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.760e+00, 's^-1'),
        n = 3.2,
        Ea = (8965.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.640e-05, 's^-1'),
        n = 4.82,
        Ea = (5690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.740e+17, 's^-1'),
        n = -1.42,
        Ea = (15417.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.170e+04, 's^-1'),
        n = 2.74,
        Ea = (10759.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.340e+14, 's^-1'),
        n = -0.746,
        Ea = (13074.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 665,
    label = "CH2CH2CH2OOH <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.550e-90, 's^-1'),
        n = 27.5,
        Ea = (-35057.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.210e+04, 's^-1'),
        n = -0.342,
        Ea = (4339.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.970e+26, 's^-1'),
        n = -5.97,
        Ea = (18743.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.600e+10, 's^-1'),
        n = -0.444,
        Ea = (17532.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.450e+17, 's^-1'),
        n = -2.82,
        Ea = (21579.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# DH = ??

entry(
    index = 666,
    label = "CH2CH2CH2OOH <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.000e-94, 's^-1'),
        n = 28.3,
        Ea = (-37006.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.720e+01, 's^-1'),
        n = 0.354,
        Ea = (3373.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.970e+25, 's^-1'),
        n = -5.92,
        Ea = (19145.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.600e+14, 's^-1'),
        n = -1.97,
        Ea = (21243.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.960e+25, 's^-1'),
        n = -5.29,
        Ea = (29003.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 667,
    label = "CH3CH(OO)CH3 <=> CH3CH(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.000e+33, 's^-1'),
        n = -8.94,
        Ea = (30442.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.480e+34, 's^-1'),
        n = -8.62,
        Ea = (32905.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.010e+33, 's^-1'),
        n = -7.75,
        Ea = (34890.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.620e+27, 's^-1'),
        n = -5.55,
        Ea = (35037.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.220e+18, 's^-1'),
        n = -2.35,
        Ea = (33245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 668,
    label = "CH3CH(OO)CH3 <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.610e+75, 's^-1'),
        n = -20.6,
        Ea = (46203.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.720e+66, 's^-1'),
        n = -17.3,
        Ea = (45459.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.030e+56, 's^-1'),
        n = -14.0,
        Ea = (44010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.290e+40, 's^-1'),
        n = -8.58,
        Ea = (39419.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.400e+25, 's^-1'),
        n = -4.02,
        Ea = (34914.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 669,
    label = "CH3CH(OO)CH3 <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.670e+87, 's^-1'),
        n = -25.3,
        Ea = (51030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.240e+72, 's^-1'),
        n = -19.8,
        Ea = (49111.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.350e+67, 's^-1'),
        n = -17.7,
        Ea = (50804.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.940e+53, 's^-1'),
        n = -13.0,
        Ea = (49382.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.600e+36, 's^-1'),
        n = -7.67,
        Ea = (46500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 670,
    label = "CH3CH(OOH)CH2 <=> HO2 + CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.860e-17, 's^-1'),
        n = 8.076,
        Ea = (7277.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.330e-10, 's^-1'),
        n = 6.192,
        Ea = (7283.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.830e+01, 's^-1'),
        n = 3.06,
        Ea = (10940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.480e+05, 's^-1'),
        n = 1.85,
        Ea = (12564.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.130e+16, 's^-1'),
        n = -1.086,
        Ea = (17721.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 671,
    label = "CH3CH(OOH)CH2 <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.310e-06, 's^-1'),
        n = 4.58,
        Ea = (2775.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.370e+00, 's^-1'),
        n = 2.89,
        Ea = (5130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.150e+09, 's^-1'),
        n = 0.521,
        Ea = (9007.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.400e+16, 's^-1'),
        n = -1.64,
        Ea = (12694.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.980e+18, 's^-1'),
        n = -2.0,
        Ea = (14251.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 672,
    label = "O2 + CH2CH2CH2OOH <=> OHOCH2CH2CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.950e+42, 'cm^3/(mol*s)'),
        n = -10.2,
        Ea = (5862.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.300e+42, 'cm^3/(mol*s)'),
        n = -9.88,
        Ea = (7527.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.470e+36, 'cm^3/(mol*s)'),
        n = -7.85,
        Ea = (6724.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.180e+27, 'cm^3/(mol*s)'),
        n = -4.75,
        Ea = (4026.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.460e+18, 'cm^3/(mol*s)'),
        n = -1.85,
        Ea = (1006.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
# *** Fuel Radical + Radical

entry(
    index = 673,
    label = "O2 + CH2CH2CH2OOH <=> OH + OH + OCHCH2CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.200e+30, 'cm^3/(mol*s)'),
        n = -6.23,
        Ea = (5242.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.420e+32, 'cm^3/(mol*s)'),
        n = -6.58,
        Ea = (8145.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.700e+27, 'cm^3/(mol*s)'),
        n = -5.03,
        Ea = (8654.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.580e+15, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (5986.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.320e+00, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (1625.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 674,
    label = "O2 + CH2CH2CH2OOH <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.460e+15, 'cm^3/(mol*s)'),
        n = -1.27,
        Ea = (3279.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.530e+20, 'cm^3/(mol*s)'),
        n = -2.73,
        Ea = (7333.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.770e+20, 'cm^3/(mol*s)'),
        n = -2.61,
        Ea = (9797.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.080e+11, 'cm^3/(mol*s)'),
        n = 0.179,
        Ea = (8570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.760e-04, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (4464.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 675,
    label = "O2 + CH2CH2CH2OOH <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.190e+11, 'cm^3/(mol*s)'),
        n = -0.662,
        Ea = (2532.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.740e+17, 'cm^3/(mol*s)'),
        n = -2.21,
        Ea = (6729.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.700e+17, 'cm^3/(mol*s)'),
        n = -2.19,
        Ea = (9352.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.360e+09, 'cm^3/(mol*s)'),
        n = 0.523,
        Ea = (8259.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.540e-06, 'cm^3/(mol*s)'),
        n = 4.94,
        Ea = (4159.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 676,
    label = "O2 + CH3CHCH2OOH <=> CH3CH(OO)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.530e+43, 'cm^3/(mol*s)'),
        n = -10.6,
        Ea = (5580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.730e+44, 'cm^3/(mol*s)'),
        n = -10.5,
        Ea = (7436.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.070e+40, 'cm^3/(mol*s)'),
        n = -9.11,
        Ea = (7633.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.230e+32, 'cm^3/(mol*s)'),
        n = -6.42,
        Ea = (5737.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.650e+22, 'cm^3/(mol*s)'),
        n = -3.28,
        Ea = (2695.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True,
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 677,
    label = "O2 + CH3CHCH2OOH <=> CH3CH(OOH)CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.230e+68, 'cm^3/(mol*s)'),
        n = -18.8,
        Ea = (15889.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (9.140e+63, 'cm^3/(mol*s)'),
        n = -17.2,
        Ea = (17206.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.480e+57, 'cm^3/(mol*s)'),
        n = -15.0,
        Ea = (17892.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.640e+39, 'cm^3/(mol*s)'),
        n = -9.26,
        Ea = (13927.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (9.850e+16, 'cm^3/(mol*s)'),
        n = -2.36,
        Ea = (7519.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True,
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 678,
    label = "O2 + CH3CHCH2OOH <=> CH2CH(OOH)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.700e+71, 'cm^3/(mol*s)'),
        n = -20.4,
        Ea = (19335.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.180e+56, 'cm^3/(mol*s)'),
        n = -15.4,
        Ea = (17248.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (9.120e+46, 'cm^3/(mol*s)'),
        n = -12.2,
        Ea = (18245.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.880e+34, 'cm^3/(mol*s)'),
        n = -8.11,
        Ea = (18262.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.260e+09, 'cm^3/(mol*s)'),
        n = -0.359,
        Ea = (12788.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 679,
    label = "O2 + CH3CHCH2OOH <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.900e+40, 'cm^3/(mol*s)'),
        n = -10.4,
        Ea = (9903.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.980e+43, 'cm^3/(mol*s)'),
        n = -11.1,
        Ea = (15060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.480e+44, 'cm^3/(mol*s)'),
        n = -11.0,
        Ea = (20566.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.770e+36, 'cm^3/(mol*s)'),
        n = -8.31,
        Ea = (23587.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (9.900e+09, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (19165.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 680,
    label = "O2 + CH3CHCH2OOH <=> OH + OH + CH3C(O)CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.810e+37, 'cm^3/(mol*s)'),
        n = -9.43,
        Ea = (8668.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.210e+39, 'cm^3/(mol*s)'),
        n = -9.86,
        Ea = (13087.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.550e+37, 'cm^3/(mol*s)'),
        n = -9.0,
        Ea = (16523.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.970e+26, 'cm^3/(mol*s)'),
        n = -5.41,
        Ea = (16538.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.150e+02, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (11159.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 681,
    label = "O2 + CH3CHCH2OOH <=> OH + OH + CH3CH(O)CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.790e+12, 'cm^3/(mol*s)'),
        n = -0.855,
        Ea = (528.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (8.750e+17, 'cm^3/(mol*s)'),
        n = -2.4,
        Ea = (4567.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.790e+20, 'cm^3/(mol*s)'),
        n = -2.96,
        Ea = (7844.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.720e+14, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (8212.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.360e+01, 'cm^3/(mol*s)'),
        n = 2.72,
        Ea = (5020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 682,
    label = "O2 + CH3CHCH2OOH <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.320e+10, 'cm^3/(mol*s)'),
        n = 0.002,
        Ea = (874.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.120e+16, 'cm^3/(mol*s)'),
        n = -1.68,
        Ea = (4872.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.510e+20, 'cm^3/(mol*s)'),
        n = -2.59,
        Ea = (8513.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.510e+16, 'cm^3/(mol*s)'),
        n = -1.27,
        Ea = (9391.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.350e+03, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (6477.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 683,
    label = "O2 + CH3CHCH2OOH <=> HO2 + CH3CHCHOOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.800e+08, 'cm^3/(mol*s)'),
        n = 0.606,
        Ea = (592.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.050e+14, 'cm^3/(mol*s)'),
        n = -1.12,
        Ea = (4599.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.610e+18, 'cm^3/(mol*s)'),
        n = -2.16,
        Ea = (8383.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.140e+14, 'cm^3/(mol*s)'),
        n = -0.988,
        Ea = (9472.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.500e+02, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (6674.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 684,
    label = "O2 + CH3CHCH2OOH <=> HO2 + CH3C(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.760e+26, 'cm^3/(mol*s)'),
        n = -5.92,
        Ea = (6496.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.260e+32, 'cm^3/(mol*s)'),
        n = -7.42,
        Ea = (11891.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.520e+34, 'cm^3/(mol*s)'),
        n = -7.71,
        Ea = (16629.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.330e+26, 'cm^3/(mol*s)'),
        n = -5.08,
        Ea = (17983.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.680e+04, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (13435.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 685,
    label = "O2 + CH3CHCH2OOH <=> O2 + CH3CH(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.680e+33, 'cm^3/(mol*s)'),
        n = -7.31,
        Ea = (8134.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.310e+38, 'cm^3/(mol*s)'),
        n = -8.76,
        Ea = (13399.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.960e+39, 'cm^3/(mol*s)'),
        n = -8.95,
        Ea = (17948.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.580e+31, 'cm^3/(mol*s)'),
        n = -6.24,
        Ea = (19092.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.020e+10, 'cm^3/(mol*s)'),
        n = 0.304,
        Ea = (14495.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 686,
    label = "O2 + CH3CH(OOH)CH2 <=> CH3CH(OO)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.340e+46, 'cm^3/(mol*s)'),
        n = -12.0,
        Ea = (9049.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.370e+42, 'cm^3/(mol*s)'),
        n = -10.6,
        Ea = (10094.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.820e+34, 'cm^3/(mol*s)'),
        n = -7.84,
        Ea = (9748.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.140e+26, 'cm^3/(mol*s)'),
        n = -5.4,
        Ea = (9407.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.550e+09, 'cm^3/(mol*s)'),
        n = -0.118,
        Ea = (4986.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True,
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 687,
    label = "O2 + CH3CH(OOH)CH2 <=> CH3CH(OOH)CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.150e+19, 'cm^3/(mol*s)'),
        n = -3.42,
        Ea = (-4037.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.500e+27, 'cm^3/(mol*s)'),
        n = -5.55,
        Ea = (518.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.100e+33, 'cm^3/(mol*s)'),
        n = -7.19,
        Ea = (4543.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.850e+33, 'cm^3/(mol*s)'),
        n = -6.97,
        Ea = (6018.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.870e+25, 'cm^3/(mol*s)'),
        n = -4.35,
        Ea = (4020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
    duplicate = True,
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 688,
    label = "O2 + CH3CH(OOH)CH2 <=> CH2CH(OOH)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.060e+29, 'cm^3/(mol*s)'),
        n = -7.2,
        Ea = (1939.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.310e+34, 'cm^3/(mol*s)'),
        n = -8.44,
        Ea = (6445.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.030e+37, 'cm^3/(mol*s)'),
        n = -8.9,
        Ea = (10770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.010e+31, 'cm^3/(mol*s)'),
        n = -6.67,
        Ea = (11888.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.460e+16, 'cm^3/(mol*s)'),
        n = -1.87,
        Ea = (8889.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 689,
    label = "O2 + CH3CH(OOH)CH2 <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.190e+13, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (92.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.980e+22, 'cm^3/(mol*s)'),
        n = -3.99,
        Ea = (5873.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.300e+32, 'cm^3/(mol*s)'),
        n = -6.72,
        Ea = (13056.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.600e+31, 'cm^3/(mol*s)'),
        n = -6.33,
        Ea = (17283.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.150e+15, 'cm^3/(mol*s)'),
        n = -1.23,
        Ea = (15031.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 690,
    label = "O2 + CH3CH(OOH)CH2 <=> OH + OH + CH3C(O)CH2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.280e+09, 'cm^3/(mol*s)'),
        n = -0.041,
        Ea = (-1693.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.260e+16, 'cm^3/(mol*s)'),
        n = -2.06,
        Ea = (2603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.700e+22, 'cm^3/(mol*s)'),
        n = -3.98,
        Ea = (7360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.350e+21, 'cm^3/(mol*s)'),
        n = -3.39,
        Ea = (9360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.130e+10, 'cm^3/(mol*s)'),
        n = 0.117,
        Ea = (7227.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 691,
    label = "O2 + CH3CH(OOH)CH2 <=> OH + OH + CH3CH(O)CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.110e+18, 'cm^3/(mol*s)'),
        n = -3.19,
        Ea = (5911.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.670e+13, 'cm^3/(mol*s)'),
        n = -1.44,
        Ea = (6967.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.700e+06, 'cm^3/(mol*s)'),
        n = 0.697,
        Ea = (7674.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.300e+03, 'cm^3/(mol*s)'),
        n = 1.68,
        Ea = (9631.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.910e-13, 'cm^3/(mol*s)'),
        n = 6.32,
        Ea = (6808.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 692,
    label = "O2 + CH3CH(OOH)CH2 <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.830e+15, 'cm^3/(mol*s)'),
        n = -1.76,
        Ea = (4657.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.680e+15, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (6599.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.810e+22, 'cm^3/(mol*s)'),
        n = -3.78,
        Ea = (11805.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.680e+20, 'cm^3/(mol*s)'),
        n = -3.2,
        Ea = (15352.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.230e+04, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (13075.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 693,
    label = "O2 + CH3CH(OOH)CH2 <=> HO2 + CH3CHCHOOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.060e+18, 'cm^3/(mol*s)'),
        n = -2.77,
        Ea = (6958.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.410e+12, 'cm^3/(mol*s)'),
        n = -0.913,
        Ea = (7831.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.370e+05, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (8424.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.810e+02, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (10617.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.040e-12, 'cm^3/(mol*s)'),
        n = 6.35,
        Ea = (8212.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 694,
    label = "O2 + CH3CH(OOH)CH2 <=> HO2 + CH3C(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.690e+05, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (-340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.920e+11, 'cm^3/(mol*s)'),
        n = -0.295,
        Ea = (3116.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.390e+18, 'cm^3/(mol*s)'),
        n = -2.5,
        Ea = (7896.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.260e+20, 'cm^3/(mol*s)'),
        n = -2.84,
        Ea = (10971.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.020e+11, 'cm^3/(mol*s)'),
        n = 0.048,
        Ea = (9737.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 695,
    label = "OHOCH2CH2CH2OO <=> OH + OCHCH2CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.080e+29, 's^-1'),
        n = -6.39,
        Ea = (23440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.490e+25, 's^-1'),
        n = -4.95,
        Ea = (22612.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.010e+19, 's^-1'),
        n = -2.88,
        Ea = (20804.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.460e+11, 's^-1'),
        n = -0.538,
        Ea = (18441.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.670e+05, 's^-1'),
        n = 1.48,
        Ea = (16238.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
# *****************************************************************************
#    OHOCH2CH2CH2OOH subset                                                   *
#    CH3CH(OOH)CH2OOH subset                                                  *
# *****************************************************************************

entry(
    index = 696,
    label = "OHOCH2CH2CH2OO <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.850e+46, 's^-1'),
        n = -11.4,
        Ea = (37872.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.560e+44, 's^-1'),
        n = -10.5,
        Ea = (38835.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.870e+37, 's^-1'),
        n = -8.08,
        Ea = (37522.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (6.420e+26, 's^-1'),
        n = -4.59,
        Ea = (34397.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.960e+16, 's^-1'),
        n = -1.27,
        Ea = (30917.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 697,
    label = "OHOCH2CH2CH2OO <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.470e+38, 's^-1'),
        n = -9.47,
        Ea = (33734.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.840e+35, 's^-1'),
        n = -8.3,
        Ea = (34435.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.960e+27, 's^-1'),
        n = -5.62,
        Ea = (32906.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.660e+16, 's^-1'),
        n = -1.93,
        Ea = (29584.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.720e+05, 's^-1'),
        n = 1.6,
        Ea = (25882.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 698,
    label = "CH3CH(OO)CH2OOH <=> CH3CH(OOH)CH2OO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.970e+32, 's^-1'),
        n = -7.73,
        Ea = (24949.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.450e+30, 's^-1'),
        n = -7.03,
        Ea = (25023.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.960e+26, 's^-1'),
        n = -5.68,
        Ea = (24306.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.250e+19, 's^-1'),
        n = -3.28,
        Ea = (22143.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.350e+10, 's^-1'),
        n = -0.557,
        Ea = (19335.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 699,
    label = "CH3CH(OO)CH2OOH <=> CH2CH(OOH)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.930e+57, 's^-1'),
        n = -15.8,
        Ea = (40644.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.010e+56, 's^-1'),
        n = -15.2,
        Ea = (42938.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.650e+51, 's^-1'),
        n = -13.3,
        Ea = (43899.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.530e+39, 's^-1'),
        n = -9.43,
        Ea = (42209.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.450e+08, 's^-1'),
        n = -0.201,
        Ea = (31860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 700,
    label = "CH3CH(OO)CH2OOH <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.960e+74, 's^-1'),
        n = -20.6,
        Ea = (49026.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.820e+75, 's^-1'),
        n = -20.6,
        Ea = (53262.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.590e+71, 's^-1'),
        n = -19.1,
        Ea = (56338.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.300e+58, 's^-1'),
        n = -14.9,
        Ea = (56128.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.870e+29, 's^-1'),
        n = -6.03,
        Ea = (49095.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 701,
    label = "CH3CH(OO)CH2OOH <=> OH + CH3C(O)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.100e+67, 's^-1'),
        n = -18.3,
        Ea = (45215.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.500e+62, 's^-1'),
        n = -16.8,
        Ea = (46575.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.210e+52, 's^-1'),
        n = -13.6,
        Ea = (45642.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.860e+36, 's^-1'),
        n = -8.6,
        Ea = (42194.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.290e+15, 's^-1'),
        n = -1.92,
        Ea = (35845.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 702,
    label = "CH3CH(OO)CH2OOH <=> OH + CH3CH(OOH)CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.530e+40, 's^-1'),
        n = -9.91,
        Ea = (32631.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.540e+37, 's^-1'),
        n = -8.72,
        Ea = (32909.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.120e+31, 's^-1'),
        n = -6.53,
        Ea = (31807.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.980e+21, 's^-1'),
        n = -3.34,
        Ea = (29138.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.950e+10, 's^-1'),
        n = 0.154,
        Ea = (25612.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 703,
    label = "CH3CH(OO)CH2OOH <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.020e+51, 's^-1'),
        n = -12.8,
        Ea = (39362.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.200e+50, 's^-1'),
        n = -12.2,
        Ea = (40662.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.150e+45, 's^-1'),
        n = -10.3,
        Ea = (40332.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.130e+35, 's^-1'),
        n = -7.15,
        Ea = (37939.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (7.710e+23, 's^-1'),
        n = -3.45,
        Ea = (34300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 704,
    label = "CH3CH(OO)CH2OOH <=> HO2 + CH3CHCHOOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.040e+50, 's^-1'),
        n = -12.7,
        Ea = (39536.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.230e+49, 's^-1'),
        n = -12.1,
        Ea = (41005.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.980e+44, 's^-1'),
        n = -10.3,
        Ea = (40814.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.650e+34, 's^-1'),
        n = -7.1,
        Ea = (38442.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.150e+22, 's^-1'),
        n = -3.26,
        Ea = (34691.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 705,
    label = "CH3CH(OO)CH2OOH <=> HO2 + CH3C(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.840e+68, 's^-1'),
        n = -18.8,
        Ea = (48357.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.430e+67, 's^-1'),
        n = -18.0,
        Ea = (50795.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.770e+59, 's^-1'),
        n = -15.4,
        Ea = (51184.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.870e+45, 's^-1'),
        n = -10.8,
        Ea = (48655.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.550e+23, 's^-1'),
        n = -3.97,
        Ea = (42478.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 706,
    label = "CH3CH(OOH)CH2OO <=> CH2CH(OOH)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.750e+42, 's^-1'),
        n = -10.5,
        Ea = (31159.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.760e+39, 's^-1'),
        n = -9.32,
        Ea = (31691.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.420e+33, 's^-1'),
        n = -7.12,
        Ea = (30696.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.660e+25, 's^-1'),
        n = -4.59,
        Ea = (28857.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.980e+16, 's^-1'),
        n = -1.63,
        Ea = (25974.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 707,
    label = "CH3CH(OOH)CH2OO <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.110e+75, 's^-1'),
        n = -20.3,
        Ea = (46622.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.410e+71, 's^-1'),
        n = -18.8,
        Ea = (48632.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.910e+60, 's^-1'),
        n = -15.0,
        Ea = (47775.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.440e+50, 's^-1'),
        n = -11.8,
        Ea = (47080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (8.890e+30, 's^-1'),
        n = -5.73,
        Ea = (41828.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 708,
    label = "CH3CH(OOH)CH2OO <=> OH + CH3C(O)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.030e+49, 's^-1'),
        n = -12.6,
        Ea = (34314.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (9.780e+40, 's^-1'),
        n = -9.67,
        Ea = (32757.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.470e+28, 's^-1'),
        n = -5.51,
        Ea = (29111.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.980e+18, 's^-1'),
        n = -2.52,
        Ea = (26400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.040e+09, 's^-1'),
        n = 0.515,
        Ea = (23246.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 709,
    label = "CH3CH(OOH)CH2OO <=> OH + CH3CH(OOH)CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.740e+40, 's^-1'),
        n = -9.94,
        Ea = (36653.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.980e+53, 's^-1'),
        n = -14.1,
        Ea = (42546.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.460e+53, 's^-1'),
        n = -13.7,
        Ea = (46324.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.080e+38, 's^-1'),
        n = -8.9,
        Ea = (43330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.400e+16, 's^-1'),
        n = -2.18,
        Ea = (37096.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 710,
    label = "CH3CH(OOH)CH2OO <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.870e+48, 's^-1'),
        n = -12.3,
        Ea = (39597.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.310e+85, 's^-1'),
        n = -23.5,
        Ea = (55900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.670e+59, 's^-1'),
        n = -15.1,
        Ea = (49926.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.300e+50, 's^-1'),
        n = -11.8,
        Ea = (49507.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.100e+29, 's^-1'),
        n = -5.33,
        Ea = (44044.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 711,
    label = "CH3CH(OOH)CH2OO <=> HO2 + CH3CHCHOOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.600e+41, 's^-1'),
        n = -10.3,
        Ea = (38545.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.080e+56, 's^-1'),
        n = -14.9,
        Ea = (45866.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.010e+57, 's^-1'),
        n = -14.8,
        Ea = (49804.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.710e+43, 's^-1'),
        n = -10.3,
        Ea = (47485.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.450e+21, 's^-1'),
        n = -3.45,
        Ea = (41383.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 712,
    label = "CH3CH(OOH)CH2OO <=> HO2 + CH3C(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.580e+63, 's^-1'),
        n = -16.7,
        Ea = (44481.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.170e+59, 's^-1'),
        n = -14.8,
        Ea = (44912.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.740e+47, 's^-1'),
        n = -10.9,
        Ea = (42146.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.790e+37, 's^-1'),
        n = -7.68,
        Ea = (39639.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.990e+26, 's^-1'),
        n = -4.15,
        Ea = (36105.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 713,
    label = "CH2CH(OOH)CH2OOH <=> OH + c-CH2OCH(CH2OOH)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.300e+11, 's^-1'),
        n = -0.635,
        Ea = (11041.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.610e+18, 's^-1'),
        n = -2.41,
        Ea = (14414.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.780e+24, 's^-1'),
        n = -4.13,
        Ea = (18110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.270e+21, 's^-1'),
        n = -3.0,
        Ea = (18125.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.120e+15, 's^-1'),
        n = -1.06,
        Ea = (16486.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 714,
    label = "CH2CH(OOH)CH2OOH <=> OH + CH3C(O)CH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.160e-25, 's^-1'),
        n = 10.4,
        Ea = (2788.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.600e-37, 's^-1'),
        n = 13.9,
        Ea = (-256.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.240e+08, 's^-1'),
        n = 0.082,
        Ea = (17439.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.110e+20, 's^-1'),
        n = -3.63,
        Ea = (24307.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.090e+05, 's^-1'),
        n = 0.938,
        Ea = (20653.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 715,
    label = "CH2CH(OOH)CH2OOH <=> OH + CH3CH(OOH)CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.610e-32, 's^-1'),
        n = 11.9,
        Ea = (4218.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (9.210e-42, 's^-1'),
        n = 14.8,
        Ea = (1990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.200e+06, 's^-1'),
        n = 0.02,
        Ea = (21511.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.280e+28, 's^-1'),
        n = -6.77,
        Ea = (33682.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.830e+08, 's^-1'),
        n = -0.63,
        Ea = (29961.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 716,
    label = "CH2CH(OOH)CH2OOH <=> HO2 + CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.430e-02, 's^-1'),
        n = 3.17,
        Ea = (9063.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.780e+13, 's^-1'),
        n = -1.39,
        Ea = (15409.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.850e+25, 's^-1'),
        n = -4.59,
        Ea = (21213.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.890e+22, 's^-1'),
        n = -3.45,
        Ea = (21661.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.710e+15, 's^-1'),
        n = -1.0,
        Ea = (19678.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 717,
    label = "CH2CH(OOH)CH2OOH <=> HO2 + CH3CHCHOOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.450e-32, 's^-1'),
        n = 12.1,
        Ea = (4948.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (8.980e-42, 's^-1'),
        n = 14.9,
        Ea = (2926.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.850e+07, 's^-1'),
        n = -0.22,
        Ea = (22938.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.100e+30, 's^-1'),
        n = -7.16,
        Ea = (35571.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (6.290e+10, 's^-1'),
        n = -1.14,
        Ea = (32271.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 718,
    label = "CH2CH(OOH)CH2OOH <=> HO2 + CH3C(OOH)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.180e-24, 's^-1'),
        n = 10.1,
        Ea = (5620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.460e-35, 's^-1'),
        n = 13.4,
        Ea = (2720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.290e+12, 's^-1'),
        n = -0.99,
        Ea = (21365.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.780e+26, 's^-1'),
        n = -5.03,
        Ea = (29085.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.660e+11, 's^-1'),
        n = -0.433,
        Ea = (25731.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 719,
    label = "OCHCH2CH2OOH <=> OCHCH2CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.410e+64, 's^-1'),
        n = -15.9,
        Ea = (55761.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.970e+61, 's^-1'),
        n = -14.6,
        Ea = (56011.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.070e+54, 's^-1'),
        n = -12.1,
        Ea = (54563.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.290e+43, 's^-1'),
        n = -8.74,
        Ea = (51568.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.060e+33, 's^-1'),
        n = -5.54,
        Ea = (48225.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
# *****************************************************************************
#    OCHCH2CH2OOH subset                                                      *
#    c-CH2OCH(CH2OOH) subset                                                  *
#    CH3C(O)CH2OOH subset                                                     *
#    CH3CH(OOH)CHO subset                                                     *
# *****************************************************************************
# *** Fuel Decomposition

entry(
    index = 720,
    label = "c-CH2OCH(CH2OOH) <=> c-CH2OCH(CH2O) + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.200e+64, 's^-1'),
        n = -15.9,
        Ea = (56650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.190e+60, 's^-1'),
        n = -14.2,
        Ea = (56480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.080e+52, 's^-1'),
        n = -11.5,
        Ea = (54580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.560e+41, 's^-1'),
        n = -7.97,
        Ea = (51321.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.030e+31, 's^-1'),
        n = -4.76,
        Ea = (47922.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# DH = ??

entry(
    index = 721,
    label = "CH3C(O)CH2OOH <=> CH3C(O)CH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.200e+64, 's^-1'),
        n = -15.9,
        Ea = (56650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.190e+60, 's^-1'),
        n = -14.2,
        Ea = (56480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.080e+52, 's^-1'),
        n = -11.5,
        Ea = (54580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.560e+41, 's^-1'),
        n = -7.97,
        Ea = (51321.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.030e+31, 's^-1'),
        n = -4.76,
        Ea = (47922.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

#  CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# not computed explicitly; taken by analogy from acetyl-methoxy + oh
#  DH = ??

entry(
    index = 722,
    label = "CH3CH(OOH)CHO <=> CH3CH(O)CHO + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.200e+64, 's^-1'),
        n = -15.9,
        Ea = (56650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.190e+60, 's^-1'),
        n = -14.2,
        Ea = (56480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.080e+52, 's^-1'),
        n = -11.5,
        Ea = (54580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.560e+41, 's^-1'),
        n = -7.97,
        Ea = (51321.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.030e+31, 's^-1'),
        n = -4.76,
        Ea = (47922.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

#  CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# not computed explicitly; taken by analogy from acetyl-methoxy + oh
#  DH = ??

entry(
    index = 723,
    label = "OCHCH2CH2O <=> CH2CHO + CH2O",
    kinetics = Arrhenius(
        A = (4.940e+10, 's^-1'),
        n = 0.857,
        Ea = (5809.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
#  CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# not computed explicitly; taken by analogy from acetyl-methoxy + oh
#  DH = ??
#  *** Radical Decomposition
entry(
    index = 724,
    label = "CH3C(O)CH2O <=> CH3CO + CH2O",
    kinetics = Arrhenius(
        A = (5.730e+13, 's^-1'),
        n = -0.025,
        Ea = (4473.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
entry(
    index = 725,
    label = "CH3CH(O)CHO <=> CH3 + OCHCHO",
    kinetics = Arrhenius(
        A = (1.740e+11, 's^-1'),
        n = 0.833,
        Ea = (9833.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
entry(
    index = 726,
    label = "CH3CH(O)CHO <=> HCO + CH3CHO",
    kinetics = Arrhenius(
        A = (2.120e+14, 's^-1'),
        n = -0.141,
        Ea = (1109.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
entry(
    index = 727,
    label = "CH2CHCH2 + H <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.000e+64, 'cm^3/(mol*s)'),
        n = -15.02,
        Ea = (23890.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.850e+40, 'cm^3/(mol*s)'),
        n = -8.59,
        Ea = (6466.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.400e+61, 'cm^3/(mol*s)'),
        n = -13.84,
        Ea = (24846.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.370e+34, 'cm^3/(mol*s)'),
        n = -6.64,
        Ea = (5193.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.000e+58, 'cm^3/(mol*s)'),
        n = -12.7,
        Ea = (25947.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (9.060e+29, 'cm^3/(mol*s)'),
        n = -5.1,
        Ea = (4172.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.680e+53, 'cm^3/(mol*s)'),
        n = -11.13,
        Ea = (25910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.780e+25, 'cm^3/(mol*s)'),
        n = -3.68,
        Ea = (3143.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.890e+44, 'cm^3/(mol*s)'),
        n = -8.62,
        Ea = (22842.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.100e+21, 'cm^3/(mol*s)'),
        n = -2.16,
        Ea = (1917.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
# *****************************************************************************
#    CH3CHCH2 subset                                                          *
#    c-CH2CH2CH2 subset                                                       *
# *****************************************************************************
# Fuel Radicals: CH2CHCH2,CH3CCH2,CH3CHCH
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition

entry(
    index = 728,
    label = "CH3CHCH + H <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.630e+57, 'cm^3/(mol*s)'),
        n = -14.37,
        Ea = (16568.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.510e+45, 'cm^3/(mol*s)'),
        n = -11.46,
        Ea = (6416.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (2.200e+62, 'cm^3/(mol*s)'),
        n = -15.25,
        Ea = (19327.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.970e+48, 'cm^3/(mol*s)'),
        n = -11.72,
        Ea = (7674.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.640e+60, 'cm^3/(mol*s)'),
        n = -14.23,
        Ea = (20781.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.060e+42, 'cm^3/(mol*s)'),
        n = -9.47,
        Ea = (6817.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (9.540e+56, 'cm^3/(mol*s)'),
        n = -12.72,
        Ea = (22415.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (3.280e+34, 'cm^3/(mol*s)'),
        n = -6.72,
        Ea = (5190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (5.460e+49, 'cm^3/(mol*s)'),
        n = -10.31,
        Ea = (21925.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.650e+26, 'cm^3/(mol*s)'),
        n = -4.09,
        Ea = (3350.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
    duplicate = True
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -86.3

entry(
    index = 729,
    label = "CH3CHCH + H <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.820e+56, 'cm^3/(mol*s)'),
        n = -14.28,
        Ea = (16407.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.950e+45, 'cm^3/(mol*s)'),
        n = -11.4,
        Ea = (6309.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.240e+62, 'cm^3/(mol*s)'),
        n = -15.22,
        Ea = (19112.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.650e+48, 'cm^3/(mol*s)'),
        n = -11.75,
        Ea = (7584.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (3.770e+60, 'cm^3/(mol*s)'),
        n = -14.24,
        Ea = (20603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (4.280e+42, 'cm^3/(mol*s)'),
        n = -9.54,
        Ea = (6789.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (9.100e+56, 'cm^3/(mol*s)'),
        n = -12.74,
        Ea = (22284.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.440e+34, 'cm^3/(mol*s)'),
        n = -6.79,
        Ea = (5170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.390e+49, 'cm^3/(mol*s)'),
        n = -10.35,
        Ea = (21902.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (5.110e+26, 'cm^3/(mol*s)'),
        n = -4.13,
        Ea = (3313.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
    duplicate = True
)

entry(
    index = 730,
    label = "CH3CCH2 + H <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.960e+60, 'cm^3/(mol*s)'),
        n = -15.16,
        Ea = (17958.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.490e+48, 'cm^3/(mol*s)'),
        n = -11.99,
        Ea = (7203.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.200e+62, 'cm^3/(mol*s)'),
        n = -15.13,
        Ea = (20123.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.770e+46, 'cm^3/(mol*s)'),
        n = -11.09,
        Ea = (7630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.310e+60, 'cm^3/(mol*s)'),
        n = -14.03,
        Ea = (21860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.090e+40, 'cm^3/(mol*s)'),
        n = -8.66,
        Ea = (6448.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.690e+54, 'cm^3/(mol*s)'),
        n = -11.97,
        Ea = (22107.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.380e+31, 'cm^3/(mol*s)'),
        n = -5.73,
        Ea = (4506.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.150e+50, 'cm^3/(mol*s)'),
        n = -10.37,
        Ea = (23293.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (5.690e+25, 'cm^3/(mol*s)'),
        n = -3.83,
        Ea = (3250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -109.9

entry(
    index = 731,
    label = "CH3CHCH2 <=> C2H2 + CH4",
    kinetics = Arrhenius(
        A = (2.500e+12, 's^-1'),
        n = 0.0,
        Ea = (70000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -106.3
entry(
    index = 732,
    label = "CH3CHCH2 <=> CH2CCH2 + H2",
    kinetics = Arrhenius(
        A = (3.000e+13, 's^-1'),
        n = 0.0,
        Ea = (80000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 30.4
entry(
    index = 733,
    label = "c-CH2CH2CH2 <=> CH3CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.600e+66, 's^-1'),
        n = -15.84,
        Ea = (87387.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.910e+43, 's^-1'),
        n = -9.67,
        Ea = (71470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (4.170e+67, 's^-1'),
        n = -15.76,
        Ea = (90989.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.920e+41, 's^-1'),
        n = -8.87,
        Ea = (71601.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.150e+68, 's^-1'),
        n = -15.6,
        Ea = (95345.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (8.930e+40, 's^-1'),
        n = -8.32,
        Ea = (73420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.330e+69, 's^-1'),
        n = -15.66,
        Ea = (101560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (6.760e+41, 's^-1'),
        n = -8.29,
        Ea = (75727.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (8.350e+64, 's^-1'),
        n = -13.97,
        Ea = (102660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.470e+34, 's^-1'),
        n = -5.92,
        Ea = (73409.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller - estimate
# DH = 38.8

entry(
    index = 734,
    label = "c-CH2CH2CH2 <=> CH2CHCH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.330e+63, 's^-1'),
        n = -14.55,
        Ea = (103320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.130e+40, 's^-1'),
        n = -8.37,
        Ea = (85836.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (7.030e+63, 's^-1'),
        n = -14.37,
        Ea = (107160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.060e+41, 's^-1'),
        n = -8.33,
        Ea = (88499.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.070e+64, 's^-1'),
        n = -14.29,
        Ea = (112340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (8.230e+43, 's^-1'),
        n = -8.88,
        Ea = (92907.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (4.920e+61, 's^-1'),
        n = -13.15,
        Ea = (114870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.270e+39, 's^-1'),
        n = -7.33,
        Ea = (93401.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (4.820e+57, 's^-1'),
        n = -11.73,
        Ea = (118250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.450e+28, 's^-1'),
        n = -4.02,
        Ea = (90995.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -8.0

entry(
    index = 735,
    label = "CH3CHCH2 + H <=> CH3 + C2H4",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.540e+09, 'cm^3/(mol*s)'),
        n = 1.355,
        Ea = (2542.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (7.890e+10, 'cm^3/(mol*s)'),
        n = 0.87,
        Ea = (3600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.670e+12, 'cm^3/(mol*s)'),
        n = 0.474,
        Ea = (5431.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.260e+22, 'cm^3/(mol*s)'),
        n = -2.55,
        Ea = (12898.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.240e+05, 'cm^3/(mol*s)'),
        n = 2.515,
        Ea = (3679.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.320e+23, 'cm^3/(mol*s)'),
        n = -2.425,
        Ea = (16500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.510e+03, 'cm^3/(mol*s)'),
        n = 2.909,
        Ea = (3981.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = 77.5
# *** Fuel + Radical

entry(
    index = 736,
    label = "CH3CHCH2 + H <=> CH2CHCH2 + H2",
    kinetics = Arrhenius(
        A = (-8.870e+08, 'cm^3/(mol*s)'),
        n = 1.307,
        Ea = (3412.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = -9.6
entry(
    index = 737,
    label = "CH3CHCH2 + H <=> CH2CHCH2 + H2",
    kinetics = Arrhenius(
        A = (5.490e+05, 'cm^3/(mol*s)'),
        n = 2.396,
        Ea = (2613.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 738,
    label = "CH3CHCH2 + O <=> C2H5 + HCO",
    kinetics = Arrhenius(
        A = (1.580e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-1216.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = -17.0
entry(
    index = 739,
    label = "CH3CHCH2 + O <=> CH2CHCH2 + OH",
    kinetics = Arrhenius(
        A = (5.240e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = -26.2
entry(
    index = 740,
    label = "CH3CHCH2 + OH <=> CH2CHOH + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.132, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.690e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (2708.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0013 atm (term 1)
        Arrhenius(
            A = (1.290e+06, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (1233.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0013 atm (term 2)
        Arrhenius(
            A = (3.760e+08, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (3068.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.820e+04, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (1162.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.200e+09, 'cm^3/(mol*s)'),
        n = 1.06,
        Ea = (3326.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 1)
        Arrhenius(
            A = (2.040e+03, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (1128.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 2)
        Arrhenius(
            A = (1.630e+10, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (3950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 1)
        Arrhenius(
            A = (2.880e+02, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (1152.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 2)
        Arrhenius(
            A = (2.090e+12, 'cm^3/(mol*s)'),
        n = 0.13,
        Ea = (5407.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.400e+01, 'cm^3/(mol*s)'),
        n = 3.21,
        Ea = (1208.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.130e+12, 'cm^3/(mol*s)'),
        n = 0.02,
        Ea = (5723.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm (term 1)
        Arrhenius(
            A = (7.710e+00, 'cm^3/(mol*s)'),
        n = 3.29,
        Ea = (1216.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm (term 2)
        Arrhenius(
            A = (8.730e+20, 'cm^3/(mol*s)'),
        n = -2.35,
        Ea = (11290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.130e+04, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3238.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.270e-02, 'cm^3/(mol*s)'),
        n = 4.03,
        Ea = (1952.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.420e+19, 'cm^3/(mol*s)'),
        n = -1.74,
        Ea = (13107.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.500e+22, 'cm^3/(mol*s)'),
        n = -2.58,
        Ea = (19256.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (3.300e-01, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (3665.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# W Tsang, JPCRD 20:221 (1991)
# DH = -15.4

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -8.8

entry(
    index = 742,
    label = "CH3CHCH2 + OH <=> CH3C(OH)CH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.132, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.340e+03, 'cm^3/(mol*s)'),
        n = 2.35,
        Ea = (2635.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0013 atm (term 1)
        Arrhenius(
            A = (2.870e+00, 'cm^3/(mol*s)'),
        n = 2.92,
        Ea = (625.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0013 atm (term 2)
        Arrhenius(
            A = (4.080e+04, 'cm^3/(mol*s)'),
        n = 2.17,
        Ea = (3048.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.840e-01, 'cm^3/(mol*s)'),
        n = 2.98,
        Ea = (704.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (6.440e+04, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (3186.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 1)
        Arrhenius(
            A = (3.130e-01, 'cm^3/(mol*s)'),
        n = 3.04,
        Ea = (721.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 2)
        Arrhenius(
            A = (2.570e+05, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (3598.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 1)
        Arrhenius(
            A = (9.340e-03, 'cm^3/(mol*s)'),
        n = 3.62,
        Ea = (677.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 2)
        Arrhenius(
            A = (1.510e+07, 'cm^3/(mol*s)'),
        n = 1.44,
        Ea = (4816.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (4.640e-05, 'cm^3/(mol*s)'),
        n = 4.48,
        Ea = (687.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (3.280e+07, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (5084.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm (term 1)
        Arrhenius(
            A = (2.710e-05, 'cm^3/(mol*s)'),
        n = 4.56,
        Ea = (707.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm (term 2)
        Arrhenius(
            A = (1.550e+10, 'cm^3/(mol*s)'),
        n = 0.62,
        Ea = (7544.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (7.650e-07, 'cm^3/(mol*s)'),
        n = 5.05,
        Ea = (874.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.480e-05, 'cm^3/(mol*s)'),
        n = 4.75,
        Ea = (2168.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.640e+15, 'cm^3/(mol*s)'),
        n = -0.8,
        Ea = (12728.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.850e+19, 'cm^3/(mol*s)'),
        n = -1.85,
        Ea = (19219.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.870e-04, 'cm^3/(mol*s)'),
        n = 4.32,
        Ea = (4020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -18.5

entry(
    index = 743,
    label = "CH3CHCH2 + OH <=> CH2CHCH2 + H2O",
    kinetics = Arrhenius(
        A = (-1.250e+08, 'cm^3/(mol*s)'),
        n = 1.73,
        Ea = (925.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -1.9
entry(
    index = 744,
    label = "CH3CHCH2 + OH <=> CH2CHCH2 + H2O",
    kinetics = Arrhenius(
        A = (1.880e+07, 'cm^3/(mol*s)'),
        n = 2.03,
        Ea = (684.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 745,
    label = "CH3CHCH2 + OH <=> CH3CCH2 + H2O",
    kinetics = Arrhenius(
        A = (4.670e+04, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (1748.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -31.5
entry(
    index = 746,
    label = "CH3CHCH2 + OH <=> CH3CCH2 + H2O",
    kinetics = Arrhenius(
        A = (5.720e-07, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (-3086.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 747,
    label = "CH3CHCH2 + OH <=> CH3CHCH + H2O",
    kinetics = Arrhenius(
        A = (7.590e+03, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (2193.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -11.5
entry(
    index = 748,
    label = "CH3CHCH2 + OH <=> CH3CHCH + H2O",
    kinetics = Arrhenius(
        A = (1.010e+00, 'cm^3/(mol*s)'),
        n = 3.51,
        Ea = (-101.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 749,
    label = "HO2 + CH3CHCH2 <=> OH + c-CH2OCH(CH3)",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.720e+04, 'cm^3/(mol*s)'),
        n = 2.29,
        Ea = (12336.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.090e+05, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (12535.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.660e+07, 'cm^3/(mol*s)'),
        n = 1.42,
        Ea = (14066.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.930e+12, 'cm^3/(mol*s)'),
        n = 0.107,
        Ea = (17385.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.300e+11, 'cm^3/(mol*s)'),
        n = 0.544,
        Ea = (19059.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -7.8

entry(
    index = 750,
    label = "CH3CHCH2 + C2H3 <=> CH2CHCHCH2 + CH3",
    kinetics = Arrhenius(
        A = (1.240e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, SJ Klippenstein, JA Miller, JPCA 115:10218 (2011).
# DH = -20.7
entry(
    index = 751,
    label = "CH3CHCH2 + HCO <=> CH2CHCH2 + CH2O",
    kinetics = Arrhenius(
        A = (1.080e+07, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, I Huzeifa, PR Abel, WH Green, PCI 32:139 (2009).
# DH = --14.5
entry(
    index = 752,
    label = "CH3CHCH2 + CH3 <=> CH2CHCH2 + CH4",
    kinetics = Arrhenius(
        A = (2.220e+00, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (5675.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = -0.3
entry(
    index = 753,
    label = "CH2CCH2 + H <=> CH2CHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.210e+61, 'cm^3/(mol*s)'),
        n = -15.25,
        Ea = (20076.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 1)
        Arrhenius(
            A = (2.800e+38, 'cm^3/(mol*s)'),
        n = -8.67,
        Ea = (8035.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 2)
        Arrhenius(
            A = (1.240e+52, 'cm^3/(mol*s)'),
        n = -12.02,
        Ea = (17839.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 1)
        Arrhenius(
            A = (6.930e+36, 'cm^3/(mol*s)'),
        n = -8.19,
        Ea = (7462.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 2)
        Arrhenius(
            A = (4.670e+51, 'cm^3/(mol*s)'),
        n = -11.45,
        Ea = (21340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.320e+30, 'cm^3/(mol*s)'),
        n = -5.78,
        Ea = (6913.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.750e+48, 'cm^3/(mol*s)'),
        n = -10.27,
        Ea = (22511.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.290e+26, 'cm^3/(mol*s)'),
        n = -4.32,
        Ea = (6163.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (4.230e+43, 'cm^3/(mol*s)'),
        n = -8.61,
        Ea = (22522.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.380e+21, 'cm^3/(mol*s)'),
        n = -2.71,
        Ea = (5187.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# W Tsang, JPCRD 20:221 (1991)
# DH = -17.1
# *** Fuel Radical Decomposition

entry(
    index = 754,
    label = "CH2CCH2 + H <=> CH3CCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.440e+102, 'cm^3/(mol*s)'),
        n = -27.51,
        Ea = (51768.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 1)
        Arrhenius(
            A = (1.100e+54, 'cm^3/(mol*s)'),
        n = -14.29,
        Ea = (10809.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm (term 2)
        Arrhenius(
            A = (1.550e+53, 'cm^3/(mol*s)'),
        n = -13.1,
        Ea = (14472.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 1)
        Arrhenius(
            A = (9.880e+44, 'cm^3/(mol*s)'),
        n = -11.21,
        Ea = (8212.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm (term 2)
        Arrhenius(
            A = (1.900e+53, 'cm^3/(mol*s)'),
        n = -12.59,
        Ea = (16726.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.810e+40, 'cm^3/(mol*s)'),
        n = -9.42,
        Ea = (7850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.950e+51, 'cm^3/(mol*s)'),
        n = -11.82,
        Ea = (18286.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.600e+35, 'cm^3/(mol*s)'),
        n = -7.57,
        Ea = (7147.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (4.210e+52, 'cm^3/(mol*s)'),
        n = -11.64,
        Ea = (22262.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (9.880e+29, 'cm^3/(mol*s)'),
        n = -5.53,
        Ea = (6581.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller, JP Senosiain, SJ Klippenstein, Y Georgievskii JPCA, 112:9429 (2008).
# DH = -55.8
# JA Miller, JP Senosiain, SJ Klippenstein, Y Georgievskii JPCA, 112:9429 (2008).
# DH = -35.9

# JA Miller, JP Senosiain, SJ Klippenstein, Y Georgievskii JPCA, 112:9429 (2008).
# DH = -34.8

entry(
    index = 757,
    label = "CH3CHCH2 + H <=> CH3CCH2 + H2",
    kinetics = Arrhenius(
        A = (1.490e+02, 'cm^3/(mol*s)'),
        n = 3.381,
        Ea = (8909.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, JP Senosiain, SJ Klippenstein, Y Georgievskii JPCA, 112:9429 (2008).
# DH = -31.1
# *** Fuel Radical + Stable
entry(
    index = 758,
    label = "CH3CHCH2 + H <=> CH3CHCH + H2",
    kinetics = Arrhenius(
        A = (5.100e+02, 'cm^3/(mol*s)'),
        n = 3.234,
        Ea = (12357.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = 3.0
entry(
    index = 759,
    label = "CH3CHCH2 + H <=> CH3CHCH + H2",
    kinetics = Arrhenius(
        A = (3.970e+02, 'cm^3/(mol*s)'),
        n = 3.252,
        Ea = (12007.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 760,
    label = "CH3CHCH2 + O <=> CH3CCH2 + OH",
    kinetics = Arrhenius(
        A = (6.030e+10, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# first trans then cis CHCH group in CH3CHCH
# DH = 6.6
entry(
    index = 761,
    label = "CH3CHCH2 + O <=> CH3CHCH + OH",
    kinetics = Arrhenius(
        A = (1.200e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8959.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = 4.6
entry(
    index = 762,
    label = "CH3CHCH2 + HO2 <=> CH2CHCH2 + H2O2",
    kinetics = Arrhenius(
        A = (7.710e-02, 'cm^3/(mol*s)'),
        n = 4.4,
        Ea = (13547.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = 8.3
entry(
    index = 763,
    label = "CH3CHCH2 + CH3 <=> CH3CCH2 + CH4",
    kinetics = Arrhenius(
        A = (8.430e-01, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (11656.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, SJ Klippenstein, JA Miller, JPCA 115:10218 (2011).
# DH = 0.2
entry(
    index = 764,
    label = "CH3CHCH2 + CH3 <=> CH3CHCH + CH4",
    kinetics = Arrhenius(
        A = (1.350e+00, 'cm^3/(mol*s)'),
        n = 3.5,
        Ea = (12848.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = 2.9
entry(
    index = 765,
    label = "CH2CHCH2 + O2 <=> CH2CHO + CH2O",
    kinetics = Arrhenius(
        A = (1.060e+10, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (12838.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = 6.6
# *** Fuel Radical + Radical
entry(
    index = 766,
    label = "CH2CHCH2 + O2 <=> C2H2 + CH2O + OH",
    kinetics = Arrhenius(
        A = (2.780e+25, 'cm^3/(mol*s)'),
        n = -4.8,
        Ea = (15468.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = -62.5
entry(
    index = 767,
    label = "CH2CHCH2 + H <=> CH2CCH2 + H2",
    kinetics = Arrhenius(
        A = (4.140e+04, 'cm^3/(mol*s)'),
        n = 2.743,
        Ea = (3591.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = -4.5
entry(
    index = 768,
    label = "CH2CHCH2 + H <=> CH3CCH + H2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein - unpublished.
# DH = -47.5
entry(
    index = 769,
    label = "CH2CHCH2 + H <=> C2H2 + CH4",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -48.6
entry(
    index = 770,
    label = "CH2CHCH2 + O <=> CH3 + CH2CO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -55.9
entry(
    index = 771,
    label = "CH2CHCH2 + OH <=> CH2CCH2 + H2O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -77.0
entry(
    index = 772,
    label = "CH2CHCH2 + OH <=> CH2O + C2H4",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -62.0
entry(
    index = 773,
    label = "CH2CHCH2 + HO2 <=> CH2CHCH2OOH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.910e+31, 'cm^3/(mol*s)'),
        n = -7.23,
        Ea = (1336.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.310e+42, 'cm^3/(mol*s)'),
        n = -10.3,
        Ea = (5569.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.030e+45, 'cm^3/(mol*s)'),
        n = -10.6,
        Ea = (7851.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.790e+37, 'cm^3/(mol*s)'),
        n = -7.92,
        Ea = (6498.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.730e+25, 'cm^3/(mol*s)'),
        n = -4.13,
        Ea = (2924.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -62.8

entry(
    index = 774,
    label = "CH2CHCH2 + HO2 <=> CH2CHCHO + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.090e+00, 'cm^3/(mol*s)'),
        n = 3.01,
        Ea = (-3421.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.350e+01, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (-2341.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.050e+05, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (595.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.100e+05, 'cm^3/(mol*s)'),
        n = 1.59,
        Ea = (2678.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.070e-05, 'cm^3/(mol*s)'),
        n = 4.59,
        Ea = (927.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = ??

entry(
    index = 775,
    label = "CH2CHCH2 + HO2 <=> CH2CHCH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.020e+13, 'cm^3/(mol*s)'),
        n = -0.158,
        Ea = (-1417.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.980e+14, 'cm^3/(mol*s)'),
        n = -0.642,
        Ea = (-349.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (7.770e+17, 'cm^3/(mol*s)'),
        n = -1.52,
        Ea = (2379.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.930e+15, 'cm^3/(mol*s)'),
        n = -0.684,
        Ea = (3615.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.640e+04, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (1144.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -116.8

entry(
    index = 776,
    label = "CH3CHCH2 + O2 <=> CH2CHCH2 + HO2",
    kinetics = Arrhenius(
        A = (1.040e+04, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (35726.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -10.6
entry(
    index = 777,
    label = "CH2CHCH2 + CH3 <=> CH2CCH2 + CH4",
    kinetics = Arrhenius(
        A = (3.020e+12, 'cm^3/(mol*s)'),
        n = -0.3,
        Ea = (-131.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = 38.4
entry(
    index = 778,
    label = "CH2CHCH2 + CHCCH <=> C6H6 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = -47.6
entry(
    index = 779,
    label = "CH3CHCH + H <=> CH2CHCH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.780e+16, 'cm^3/(mol*s)'),
        n = -0.82,
        Ea = (770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (6.610e+00, 'cm^3/(mol*s)'),
        n = 3.43,
        Ea = (-5164.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (4.440e+21, 'cm^3/(mol*s)'),
        n = -2.38,
        Ea = (3522.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (1.550e+12, 'cm^3/(mol*s)'),
        n = 0.41,
        Ea = (-461.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.090e+30, 'cm^3/(mol*s)'),
        n = -4.72,
        Ea = (10344.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.940e+13, 'cm^3/(mol*s)'),
        n = 0.14,
        Ea = (1059.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (8.400e+28, 'cm^3/(mol*s)'),
        n = -4.17,
        Ea = (13785.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.320e+10, 'cm^3/(mol*s)'),
        n = 0.91,
        Ea = (988.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (9.480e+28, 'cm^3/(mol*s)'),
        n = -4.02,
        Ea = (18931.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.540e+06, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (546.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
    duplicate = True
)

# JA Miller, SJ Klippenstein - estimate
# DH = ??

entry(
    index = 780,
    label = "CH3CHCH + H <=> CH2CHCH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.470e+16, 'cm^3/(mol*s)'),
        n = -0.84,
        Ea = (711.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.530e+02, 'cm^3/(mol*s)'),
        n = 2.94,
        Ea = (-4342.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.470e+21, 'cm^3/(mol*s)'),
        n = -2.26,
        Ea = (3180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.310e+11, 'cm^3/(mol*s)'),
        n = 0.59,
        Ea = (-749.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (1.750e+30, 'cm^3/(mol*s)'),
        n = -4.82,
        Ea = (10284.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.590e+13, 'cm^3/(mol*s)'),
        n = 0.16,
        Ea = (963.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (7.230e+28, 'cm^3/(mol*s)'),
        n = -4.17,
        Ea = (13614.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.240e+10, 'cm^3/(mol*s)'),
        n = 0.98,
        Ea = (842.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.740e+28, 'cm^3/(mol*s)'),
        n = -3.92,
        Ea = (18561.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.360e+06, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (447.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
    duplicate = True
)

entry(
    index = 781,
    label = "CH3CHCH + O2 <=> CH3CHO + HCO",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -23.6
entry(
    index = 782,
    label = "CH3CHCH + H <=> CH3CCH + H2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -93.7
entry(
    index = 783,
    label = "CH3CHCH + H <=> C2H3 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.220e+16, 'cm^3/(mol*s)'),
        n = -0.72,
        Ea = (4920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (9.480e+13, 'cm^3/(mol*s)'),
        n = -0.11,
        Ea = (599.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (6.970e+15, 'cm^3/(mol*s)'),
        n = -0.47,
        Ea = (3543.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (2.680e+14, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (1032.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (4.010e+22, 'cm^3/(mol*s)'),
        n = -2.39,
        Ea = (8462.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.580e+10, 'cm^3/(mol*s)'),
        n = 1.06,
        Ea = (1014.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (3.390e+25, 'cm^3/(mol*s)'),
        n = -3.07,
        Ea = (13482.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.150e+09, 'cm^3/(mol*s)'),
        n = 1.29,
        Ea = (1566.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (5.800e+26, 'cm^3/(mol*s)'),
        n = -3.29,
        Ea = (18849.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.530e+02, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (662.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
    duplicate = True
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -72.2

entry(
    index = 784,
    label = "CH3CHCH + H <=> C2H3 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.430e+16, 'cm^3/(mol*s)'),
        n = -0.59,
        Ea = (4573.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (4.310e+13, 'cm^3/(mol*s)'),
        n = -0.01,
        Ea = (435.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.760e+15, 'cm^3/(mol*s)'),
        n = -0.314,
        Ea = (3087.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (9.210e+13, 'cm^3/(mol*s)'),
        n = -0.22,
        Ea = (782.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.090e+22, 'cm^3/(mol*s)'),
        n = -2.34,
        Ea = (8157.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (9.240e+09, 'cm^3/(mol*s)'),
        n = 1.12,
        Ea = (844.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.760e+25, 'cm^3/(mol*s)'),
        n = -3.01,
        Ea = (13177.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (4.400e+08, 'cm^3/(mol*s)'),
        n = 1.41,
        Ea = (1351.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (9.720e+30, 'cm^3/(mol*s)'),
        n = -4.44,
        Ea = (22834.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.460e+12, 'cm^3/(mol*s)'),
        n = 0.22,
        Ea = (5469.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
    duplicate = True
)

entry(
    index = 785,
    label = "CH3CHCH + OH <=> CH3CCH + H2O",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -10.4
entry(
    index = 786,
    label = "CH3CHCH + HO2 <=> CH3CHCH2 + O2",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -86.7
entry(
    index = 787,
    label = "CH3CCH2 + O2 <=> CH3CO + CH2O",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -62.0
entry(
    index = 788,
    label = "CH3CCH2 + H <=> CH2CHCH2 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.110e+17, 'cm^3/(mol*s)'),
        n = -1.08,
        Ea = (1291.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (6.410e+03, 'cm^3/(mol*s)'),
        n = 2.61,
        Ea = (-3778.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (9.050e+29, 'cm^3/(mol*s)'),
        n = -4.91,
        Ea = (8539.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (5.190e+14, 'cm^3/(mol*s)'),
        n = -0.3,
        Ea = (1090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.980e+30, 'cm^3/(mol*s)'),
        n = -4.79,
        Ea = (12042.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (8.180e+11, 'cm^3/(mol*s)'),
        n = 0.49,
        Ea = (1185.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (8.220e+28, 'cm^3/(mol*s)'),
        n = -4.14,
        Ea = (15369.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (2.790e+09, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (1188.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (2.280e+29, 'cm^3/(mol*s)'),
        n = -4.12,
        Ea = (20887.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.750e+03, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (374.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller - estimate
# DH = -34.5

entry(
    index = 789,
    label = "CH3CCH2 + H <=> C2H3 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.320e+16, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (5203.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (8.040e+13, 'cm^3/(mol*s)'),
        n = -0.14,
        Ea = (1150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (9.040e+16, 'cm^3/(mol*s)'),
        n = -0.81,
        Ea = (4802.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (7.170e+10, 'cm^3/(mol*s)'),
        n = 0.67,
        Ea = (674.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (2.010e+24, 'cm^3/(mol*s)'),
        n = -2.86,
        Ea = (10929.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (9.970e+08, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (1596.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.750e+26, 'cm^3/(mol*s)'),
        n = -3.31,
        Ea = (15770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (7.410e+07, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (2109.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.150e+32, 'cm^3/(mol*s)'),
        n = -4.83,
        Ea = (26027.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (2.700e+12, 'cm^3/(mol*s)'),
        n = 0.32,
        Ea = (6792.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -20.0

entry(
    index = 790,
    label = "CH3CCH2 + H <=> CH3CCH + H2",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# L Ye, Y Georgievskii, SJ Klippenstein, PCI 35:223 (2015).
# DH = -6.8
entry(
    index = 791,
    label = "CH3CCH2 + O <=> CH2CO + CH3",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -68.6
entry(
    index = 792,
    label = "CH3CCH2 + OH <=> CH3CCH + H2O",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -97.0
entry(
    index = 793,
    label = "CH3CCH2 + HO2 <=> CH3CHCH2 + O2",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -83.0
entry(
    index = 794,
    label = "CH3CHCH2 + OH + O2 <=> CH3CHO + CH2O + OH",
    kinetics = Arrhenius(
        A = (3.000e+10, 'cm^6/(mol^2*s)'),
        n = 0.0,
        Ea = (-8280.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -58.3
# *** Termolecular

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -70.4
# *****************************************************************************
#     CH3CH2CHO subset                                                        *
#     CH3OCHCH2 subset                                                        *
#     CH2CHCH2OH subset                                                       *
#     CH3C(OH)CH2 subset                                                      *
#     CH3CHCHOH subset                                                        *
# *****************************************************************************
# Fuel Radicals: CH2CH2CHO, CH3CHCHO, CH3CH2CO
# Fuel Radicals: CH2OCHCH2, CH3OCCH2, CH3OCHCH
# Fuel Radicals: CHCHCH2OH, CH2CCH2OH, CH2CHCHOH, CH2CHCH2O
# Fuel Radicals: CH2C(OH)CH2, CH3C(O)CH2, CH3C(OH)CH
# Fuel Radicals: CH2CHCHOH, CH3CCHOH, CH3CHCOH, CH3CHCHO
# New Radicals Formed:
# New Fuels:
# *** Fuel + Radical

entry(
    index = 796,
    label = "CH3CHCH2 + OH <=> CH3CHCHOH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.132, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.500e+10, 'cm^3/(mol*s)'),
        n = 0.53,
        Ea = (7292.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0013 atm (term 1)
        Arrhenius(
            A = (3.480e+06, 'cm^3/(mol*s)'),
        n = 1.53,
        Ea = (4288.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0013 atm (term 2)
        Arrhenius(
            A = (2.270e+10, 'cm^3/(mol*s)'),
        n = 0.66,
        Ea = (6968.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.080e+07, 'cm^3/(mol*s)'),
        n = 1.34,
        Ea = (4576.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.810e+10, 'cm^3/(mol*s)'),
        n = 0.69,
        Ea = (6884.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 1)
        Arrhenius(
            A = (9.760e+06, 'cm^3/(mol*s)'),
        n = 1.33,
        Ea = (4589.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.013 atm (term 2)
        Arrhenius(
            A = (2.070e+10, 'cm^3/(mol*s)'),
        n = 0.68,
        Ea = (6899.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 1)
        Arrhenius(
            A = (5.140e+06, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (4594.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm (term 2)
        Arrhenius(
            A = (3.130e+11, 'cm^3/(mol*s)'),
        n = 0.36,
        Ea = (7785.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.130e+05, 'cm^3/(mol*s)'),
        n = 1.69,
        Ea = (4603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (7.290e+11, 'cm^3/(mol*s)'),
        n = 0.26,
        Ea = (8071.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm (term 1)
        Arrhenius(
            A = (1.390e+05, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (4603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.132 atm (term 2)
        Arrhenius(
            A = (2.910e+15, 'cm^3/(mol*s)'),
        n = -0.74,
        Ea = (11079.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.030e+02, 'cm^3/(mol*s)'),
        n = 2.83,
        Ea = (4530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (4.510e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (15763.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (3.400e-02, 'cm^3/(mol*s)'),
        n = 3.89,
        Ea = (4390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (3.790e+21, 'cm^3/(mol*s)'),
        n = -2.3,
        Ea = (20501.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.460e-06, 'cm^3/(mol*s)'),
        n = 5.03,
        Ea = (4132.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = 8.6

entry(
    index = 797,
    label = "CH2OCHCH2 <=> CH2CH2CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.010e-92, 's^-1'),
        n = 27.8,
        Ea = (-37321.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (7.780e-11, 's^-1'),
        n = 3.7,
        Ea = (-2767.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.110e+15, 's^-1'),
        n = -2.76,
        Ea = (15938.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.480e+25, 's^-1'),
        n = -5.2,
        Ea = (21532.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.970e+34, 's^-1'),
        n = -7.41,
        Ea = (28117.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.620e+22, 's^-1'),
        n = -3.56,
        Ea = (25807.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (2.510e+20, 's^-1'),
        n = -2.63,
        Ea = (29288.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = 2.4
# *** Fuel Radical Decomposition

entry(
    index = 798,
    label = "CH2OCHCH2 <=> CH2CHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.930e+24, 's^-1'),
        n = -5.05,
        Ea = (20108.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (2.140e+28, 's^-1'),
        n = -5.8,
        Ea = (22219.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.930e+32, 's^-1'),
        n = -6.64,
        Ea = (25108.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.600e+34, 's^-1'),
        n = -7.11,
        Ea = (28209.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.170e+34, 's^-1'),
        n = -6.64,
        Ea = (30648.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.170e+28, 's^-1'),
        n = -4.71,
        Ea = (31232.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (3.980e+18, 's^-1'),
        n = -1.62,
        Ea = (30130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -16.2

entry(
    index = 799,
    label = "CH2CHCH2O <=> CH2OCHCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.170e+20, 's^-1'),
        n = -4.15,
        Ea = (12121.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (4.790e+24, 's^-1'),
        n = -5.03,
        Ea = (14606.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.900e+26, 's^-1'),
        n = -5.16,
        Ea = (16124.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.510e+28, 's^-1'),
        n = -5.4,
        Ea = (18165.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.420e+28, 's^-1'),
        n = -5.17,
        Ea = (19691.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.570e+24, 's^-1'),
        n = -3.86,
        Ea = (19395.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (1.350e+18, 's^-1'),
        n = -1.73,
        Ea = (17386.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = 14.3

entry(
    index = 800,
    label = "CH2CHCH2O <=> CH2CH2CHO",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.250e-49, 's^-1'),
        n = 15.5,
        Ea = (-15640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.460e-88, 's^-1'),
        n = 27.6,
        Ea = (-35995.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.440e-22, 's^-1'),
        n = 8.38,
        Ea = (-3819.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.230e+12, 's^-1'),
        n = -1.44,
        Ea = (10829.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.480e+42, 's^-1'),
        n = -9.91,
        Ea = (25298.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.880e+38, 's^-1'),
        n = -8.16,
        Ea = (25974.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (1.670e+21, 's^-1'),
        n = -2.74,
        Ea = (20338.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -2.7

entry(
    index = 801,
    label = "CH2CHCH2O <=> CH2CHCHO + H",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.000e+15, 's^-1'),
        n = -2.31,
        Ea = (14668.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.500e+22, 's^-1'),
        n = -3.96,
        Ea = (18283.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.950e+23, 's^-1'),
        n = -3.99,
        Ea = (19143.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.150e+25, 's^-1'),
        n = -4.24,
        Ea = (20311.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.760e+28, 's^-1'),
        n = -4.89,
        Ea = (22765.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.410e+27, 's^-1'),
        n = -4.28,
        Ea = (23771.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        Arrhenius(
            A = (2.570e+20, 's^-1'),
        n = -2.06,
        Ea = (22040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1000.0 atm
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = -19.0

entry(
    index = 802,
    label = "CH3C(OH)CH <=> CH3C(O)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.137, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.470e+01, 's^-1'),
        n = 0.0,
        Ea = (7218.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (0.000e+00, 's^-1'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (7.410e-39, 's^-1'),
        n = 10.61,
        Ea = (-24800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (0.000e+00, 's^-1'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (1.530e+114, 's^-1'),
        n = -32.93,
        Ea = (60850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (0.000e+00, 's^-1'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (7.460e-127, 's^-1'),
        n = 40.81,
        Ea = (-32720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 1)
        Arrhenius(
            A = (9.900e-161, 's^-1'),
        n = 21.1,
        Ea = (-154900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 2)
        Arrhenius(
            A = (4.590e+67, 's^-1'),
        n = -17.76,
        Ea = (47730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.700e+37, 's^-1'),
        n = -16.07,
        Ea = (-964.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (1.540e-102, 's^-1'),
        n = 26.07,
        Ea = (-55040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.060e+47, 's^-1'),
        n = -10.91,
        Ea = (42080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (4.070e+51, 's^-1'),
        n = -11.66,
        Ea = (50020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (4.930e+26, 's^-1'),
        n = -4.92,
        Ea = (32250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# CF Goldsmith, SJ Klippenstein, WH Green, PCI 33:273 (2011).
# DH = 11.5

entry(
    index = 803,
    label = "CH2CHCH2OOH <=> CH2CHCHO + H2O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.990e+50, 's^-1'),
        n = -12.7,
        Ea = (53532.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (4.720e+47, 's^-1'),
        n = -11.5,
        Ea = (54361.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.500e+40, 's^-1'),
        n = -8.84,
        Ea = (53179.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.540e+28, 's^-1'),
        n = -5.0,
        Ea = (49919.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.480e+16, 's^-1'),
        n = -1.12,
        Ea = (45949.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -28.5
# *****************************************************************************
#     CH2CHCH2OOH subset                                                      *
# *****************************************************************************
# Fuel Radicals:
# New Radicals Formed:
# New Fuels:

entry(
    index = 804,
    label = "CH2CHCH2OOH <=> CH2CHCH2O + OH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.490e+58, 's^-1'),
        n = -13.9,
        Ea = (54267.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.800e+54, 's^-1'),
        n = -12.4,
        Ea = (54194.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.360e+46, 's^-1'),
        n = -9.81,
        Ea = (52468.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.390e+36, 's^-1'),
        n = -6.54,
        Ea = (49429.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.280e+27, 's^-1'),
        n = -3.61,
        Ea = (46333.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??

entry(
    index = 805,
    label = "CH2CCH2 <=> CH3CCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.030e+53, 's^-1'),
        n = -12.18,
        Ea = (84276.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (7.760e+39, 's^-1'),
        n = -7.8,
        Ea = (78446.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.790e+48, 's^-1'),
        n = -10.0,
        Ea = (88685.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??
# *****************************************************************************
#    CH3CCH subset                                                            *
#    CH2CCH2 subset                                                           *
#    c-CHCH2CH subset                                                         *
# *****************************************************************************
# *** Fuel Decomposition

entry(
    index = 806,
    label = "c-CHCH2CH <=> CH3CCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.510e+50, 's^-1'),
        n = -11.82,
        Ea = (50914.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.230e+37, 's^-1'),
        n = -7.51,
        Ea = (45551.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.660e+37, 's^-1'),
        n = -7.24,
        Ea = (48013.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -1.1

entry(
    index = 807,
    label = "c-CHCH2CH <=> CH2CCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.770e+43, 's^-1'),
        n = -9.97,
        Ea = (56007.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.510e+26, 's^-1'),
        n = -4.56,
        Ea = (43922.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.010e+35, 's^-1'),
        n = -6.87,
        Ea = (51298.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -23.9

entry(
    index = 808,
    label = "CH2CCH + H <=> CH3CCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.630e+36, 'cm^3/(mol*s)'),
        n = -7.36,
        Ea = (6039.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (7.940e+29, 'cm^3/(mol*s)'),
        n = -5.06,
        Ea = (4861.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.070e+24, 'cm^3/(mol*s)'),
        n = -3.15,
        Ea = (3261.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -22.8

entry(
    index = 809,
    label = "CH2CCH + H <=> CH2CCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.390e+36, 'cm^3/(mol*s)'),
        n = -7.41,
        Ea = (6337.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (3.160e+29, 'cm^3/(mol*s)'),
        n = -5.0,
        Ea = (4711.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.710e+23, 'cm^3/(mol*s)'),
        n = -3.2,
        Ea = (3255.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -90.3

entry(
    index = 810,
    label = "CH2CCH + H <=> c-CHCH2CH",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.910e+112, 'cm^3/(mol*s)'),
        n = -28.26,
        Ea = (83611.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.070e+21, 'cm^3/(mol*s)'),
        n = -2.95,
        Ea = (2687.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.240e+18, 'cm^3/(mol*s)'),
        n = -2.05,
        Ea = (2053.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -89.2

entry(
    index = 811,
    label = "CH3CCH + H <=> CH2CCH + H2",
    kinetics = Arrhenius(
        A = (3.570e+04, 'cm^3/(mol*s)'),
        n = 2.825,
        Ea = (4821.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -66.4
# *** Fuel + Radical


# JA Miller, JP Senosiain, SJ Klippenstein, JPCA 112:9429 (2008).
# DH = -13.0

entry(
    index = 813,
    label = "CH3CCH + O <=> HCCO + CH3",
    kinetics = Arrhenius(
        A = (2.040e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2250.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, JP Senosiain, SJ Klippenstein, JPCA 112:9429 (2008).
# DH = -7.2
entry(
    index = 814,
    label = "CH3CCH + O <=> C2H4 + CO",
    kinetics = Arrhenius(
        A = (5.800e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2250.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -27.0
entry(
    index = 815,
    label = "CH3CCH + OH <=> CH2CCH + H2O",
    kinetics = Arrhenius(
        A = (3.870e+05, 'cm^3/(mol*s)'),
        n = 2.34,
        Ea = (2173.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -117.9
entry(
    index = 816,
    label = "CH3CCH + OH <=> CH2CCH + H2O",
    kinetics = Arrhenius(
        A = (4.930e+04, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (-62.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 817,
    label = "CH3CCH + OH <=> CH2CO + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.137, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.660e+19, 'cm^3/(mol*s)'),
        n = -2.65,
        Ea = (3168.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (5.970e+05, 'cm^3/(mol*s)'),
        n = 1.79,
        Ea = (30.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (2.650e+23, 'cm^3/(mol*s)'),
        n = -3.76,
        Ea = (6001.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.770e+06, 'cm^3/(mol*s)'),
        n = 1.67,
        Ea = (651.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (1.070e+26, 'cm^3/(mol*s)'),
        n = -4.36,
        Ea = (9186.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (8.170e+06, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (1900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (1.250e+26, 'cm^3/(mol*s)'),
        n = -4.35,
        Ea = (9552.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 1)
        Arrhenius(
            A = (8.400e+06, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2055.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 2)
        Arrhenius(
            A = (4.070e+26, 'cm^3/(mol*s)'),
        n = -4.29,
        Ea = (12560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (4.680e+06, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3216.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (1.620e+25, 'cm^3/(mol*s)'),
        n = -3.63,
        Ea = (16000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (2.580e+04, 'cm^3/(mol*s)'),
        n = 2.24,
        Ea = (4381.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (1.600e+23, 'cm^3/(mol*s)'),
        n = -2.8,
        Ea = (20820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (2.470e+02, 'cm^3/(mol*s)'),
        n = 2.59,
        Ea = (5447.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -27.5

entry(
    index = 818,
    label = "CH3CCH + OH <=> CH3C(OH)CH",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.137, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.720e+56, 'cm^3/(mol*s)'),
        n = -14.84,
        Ea = (13950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (1.450e+37, 'cm^3/(mol*s)'),
        n = -9.01,
        Ea = (5016.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (3.080e+50, 'cm^3/(mol*s)'),
        n = -12.55,
        Ea = (12860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (7.760e+38, 'cm^3/(mol*s)'),
        n = -9.39,
        Ea = (5859.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (9.420e+48, 'cm^3/(mol*s)'),
        n = -11.7,
        Ea = (13990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (4.150e+35, 'cm^3/(mol*s)'),
        n = -8.1,
        Ea = (5646.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (4.820e+48, 'cm^3/(mol*s)'),
        n = -11.56,
        Ea = (14120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 1)
        Arrhenius(
            A = (1.060e+35, 'cm^3/(mol*s)'),
        n = -7.88,
        Ea = (5565.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 2)
        Arrhenius(
            A = (5.380e+45, 'cm^3/(mol*s)'),
        n = -10.36,
        Ea = (14810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (3.810e+29, 'cm^3/(mol*s)'),
        n = -5.96,
        Ea = (4629.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (5.690e+39, 'cm^3/(mol*s)'),
        n = -8.25,
        Ea = (14510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (6.090e+24, 'cm^3/(mol*s)'),
        n = -4.28,
        Ea = (3734.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (3.780e+34, 'cm^3/(mol*s)'),
        n = -6.46,
        Ea = (14750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (9.420e+16, 'cm^3/(mol*s)'),
        n = -1.62,
        Ea = (2073.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -30.0

entry(
    index = 819,
    label = "CH3CCH + OH <=> CH3CCHOH",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.137, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.450e+58, 'cm^3/(mol*s)'),
        n = -15.46,
        Ea = (14000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (5.000e+38, 'cm^3/(mol*s)'),
        n = -9.39,
        Ea = (4926.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (1.190e+51, 'cm^3/(mol*s)'),
        n = -12.69,
        Ea = (12080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (3.160e+40, 'cm^3/(mol*s)'),
        n = -9.81,
        Ea = (5704.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (1.310e+50, 'cm^3/(mol*s)'),
        n = -12.02,
        Ea = (13260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (9.980e+37, 'cm^3/(mol*s)'),
        n = -8.76,
        Ea = (5709.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (9.000e+49, 'cm^3/(mol*s)'),
        n = -11.92,
        Ea = (13420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 1)
        Arrhenius(
            A = (3.580e+37, 'cm^3/(mol*s)'),
        n = -8.59,
        Ea = (5671.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 2)
        Arrhenius(
            A = (5.360e+47, 'cm^3/(mol*s)'),
        n = -10.93,
        Ea = (14280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (3.150e+33, 'cm^3/(mol*s)'),
        n = -7.11,
        Ea = (5101.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (9.760e+43, 'cm^3/(mol*s)'),
        n = -9.47,
        Ea = (15070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.030e+27, 'cm^3/(mol*s)'),
        n = -4.84,
        Ea = (3902.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (3.050e+38, 'cm^3/(mol*s)'),
        n = -7.55,
        Ea = (15160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (5.510e+20, 'cm^3/(mol*s)'),
        n = -2.69,
        Ea = (2617.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -30.8

entry(
    index = 820,
    label = "CH3CCH + CH3 <=> CH2CCH + CH4",
    kinetics = Arrhenius(
        A = (1.800e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (7700.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -30.3
entry(
    index = 821,
    label = "CH2CHCHCH2 + H <=> CH3CCH + CH3",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (7000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -13.1
entry(
    index = 822,
    label = "CH3CCH + CH2 <=> CH3CCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 0.3
entry(
    index = 823,
    label = "CH3CCH + CH2 <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -11.7
entry(
    index = 824,
    label = "CH3CCH + CH2(S) <=> CH3CCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -9.6
entry(
    index = 825,
    label = "CH3CCH + CH2(S) <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -20.8
entry(
    index = 826,
    label = "CH3CCH + C2H <=> C2H2 + CH2CCH",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -18.7
entry(
    index = 827,
    label = "CH2CCH2 + H <=> CH2CCH + H2",
    kinetics = Arrhenius(
        A = (6.630e+03, 'cm^3/(mol*s)'),
        n = 3.095,
        Ea = (5522.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -41.3
entry(
    index = 828,
    label = "CH2CCH2 + H <=> CH3CCH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.490e+10, 'cm^3/(mol*s)'),
        n = 0.89,
        Ea = (2503.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (1.480e+13, 'cm^3/(mol*s)'),
        n = 0.26,
        Ea = (4103.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.480e+15, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (6436.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.350e+25, 'cm^3/(mol*s)'),
        n = -3.23,
        Ea = (13165.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.740e+07, 'cm^3/(mol*s)'),
        n = 1.98,
        Ea = (4521.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.020e+24, 'cm^3/(mol*s)'),
        n = -2.67,
        Ea = (15552.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (4.630e+04, 'cm^3/(mol*s)'),
        n = 2.62,
        Ea = (4466.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller, JP Senosiain, SJ Klippenstein, JPCA 112:9429 (2008).
# DH = -14.1

entry(
    index = 829,
    label = "CH2CCH2 + H <=> C2H2 + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.00132, 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.230e+08, 'cm^3/(mol*s)'),
        n = 1.53,
        Ea = (4737.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00132 atm
        Arrhenius(
            A = (2.720e+09, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (6834.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.260e+20, 'cm^3/(mol*s)'),
        n = -1.83,
        Ea = (15003.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (1.230e+04, 'cm^3/(mol*s)'),
        n = 2.68,
        Ea = (6335.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.680e+16, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (14754.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (3.310e+08, 'cm^3/(mol*s)'),
        n = 1.14,
        Ea = (8886.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (1.370e+17, 'cm^3/(mol*s)'),
        n = -0.79,
        Ea = (17603.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.280e+06, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (9774.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller, JP Senosiain, SJ Klippenstein, JPCA 112:9429 (2008).
# DH = -1.1

entry(
    index = 830,
    label = "CH2CCH2 + O <=> C2H4 + CO",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, JP Senosiain, SJ Klippenstein, JPCA 112:9429 (2008).
# DH = -8.3
entry(
    index = 831,
    label = "CH2CCH2 + OH <=> CH2CCH + H2O",
    kinetics = Arrhenius(
        A = (5.050e+05, 'cm^3/(mol*s)'),
        n = 2.36,
        Ea = (2879.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -119.0
entry(
    index = 832,
    label = "CH2CCH2 + OH <=> CH2CCH + H2O",
    kinetics = Arrhenius(
        A = (5.950e+04, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (661.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
entry(
    index = 833,
    label = "CH2CCH2 + OH <=> CH2CO + CH3",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.137, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.030e+22, 'cm^3/(mol*s)'),
        n = -3.01,
        Ea = (6341.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (8.330e+08, 'cm^3/(mol*s)'),
        n = 1.01,
        Ea = (27.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (3.460e+26, 'cm^3/(mol*s)'),
        n = -4.03,
        Ea = (10860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (4.230e+07, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (765.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (4.270e+25, 'cm^3/(mol*s)'),
        n = -3.56,
        Ea = (13980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (7.900e+05, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (1082.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (2.060e+25, 'cm^3/(mol*s)'),
        n = -3.45,
        Ea = (14320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 1)
        Arrhenius(
            A = (3.450e+06, 'cm^3/(mol*s)'),
        n = 1.55,
        Ea = (1330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 2)
        Arrhenius(
            A = (4.070e+25, 'cm^3/(mol*s)'),
        n = -3.41,
        Ea = (18370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (1.510e+04, 'cm^3/(mol*s)'),
        n = 2.2,
        Ea = (1759.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (4.470e+20, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (20040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (1.290e-03, 'cm^3/(mol*s)'),
        n = 4.35,
        Ea = (1625.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (7.910e+12, 'cm^3/(mol*s)'),
        n = 0.32,
        Ea = (19980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (3.100e-12, 'cm^3/(mol*s)'),
        n = 6.76,
        Ea = (656.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015); with factor of 2 correction by JA Miller
# DH = -28.6

entry(
    index = 834,
    label = "CH2CCH2 + OH <=> CH2CCH2OH",
    kinetics = PDepArrhenius(
        pressures = ([0.000987, 0.00987, 0.0987, 0.137, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.130e+64, 'cm^3/(mol*s)'),
        n = -17.33,
        Ea = (15220.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 1)
        Arrhenius(
            A = (8.440e+37, 'cm^3/(mol*s)'),
        n = -9.1,
        Ea = (4180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.000987 atm (term 2)
        Arrhenius(
            A = (9.710e+54, 'cm^3/(mol*s)'),
        n = -13.91,
        Ea = (13150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 1)
        Arrhenius(
            A = (1.750e+35, 'cm^3/(mol*s)'),
        n = -7.98,
        Ea = (4068.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.00987 atm (term 2)
        Arrhenius(
            A = (4.590e+47, 'cm^3/(mol*s)'),
        n = -11.22,
        Ea = (12070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 1)
        Arrhenius(
            A = (1.610e+35, 'cm^3/(mol*s)'),
        n = -7.87,
        Ea = (4353.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0987 atm (term 2)
        Arrhenius(
            A = (2.470e+47, 'cm^3/(mol*s)'),
        n = -11.09,
        Ea = (12230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 1)
        Arrhenius(
            A = (4.590e+34, 'cm^3/(mol*s)'),
        n = -7.66,
        Ea = (4288.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.137 atm (term 2)
        Arrhenius(
            A = (2.590e+44, 'cm^3/(mol*s)'),
        n = -9.87,
        Ea = (12970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 1)
        Arrhenius(
            A = (4.770e+29, 'cm^3/(mol*s)'),
        n = -5.88,
        Ea = (3477.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.987 atm (term 2)
        Arrhenius(
            A = (3.260e+39, 'cm^3/(mol*s)'),
        n = -8.08,
        Ea = (13360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 1)
        Arrhenius(
            A = (5.000e+22, 'cm^3/(mol*s)'),
        n = -3.47,
        Ea = (2109.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.87 atm (term 2)
        Arrhenius(
            A = (5.730e+32, 'cm^3/(mol*s)'),
        n = -5.83,
        Ea = (12740.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 1)
        Arrhenius(
            A = (3.600e+16, 'cm^3/(mol*s)'),
        n = -1.38,
        Ea = (780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.7 atm (term 2)
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -31.2

entry(
    index = 835,
    label = "CH2CHCH2 + O2 <=> CH2CCH2 + HO2",
    kinetics = Arrhenius(
        A = (4.990e+15, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (22428.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# J Zador, JA Miller, PCI 35:181 (2015).
# DH = -26.4
entry(
    index = 836,
    label = "CH2CCH2 + CH3 <=> CH2CCH + CH4",
    kinetics = Arrhenius(
        A = (1.300e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (7700.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = 7.8
entry(
    index = 837,
    label = "CH2CHCHCH2 + H <=> CH2CCH2 + CH3",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (7000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -14.2
entry(
    index = 838,
    label = "CH2CCH2 + CH2 <=> CH3CCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 1.4
entry(
    index = 839,
    label = "CH2CCH2 + CH2 <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -12.8
entry(
    index = 840,
    label = "CH2CCH2 + CH2(S) <=> CH3CCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -10.7
entry(
    index = 841,
    label = "CH2CCH2 + CH2(S) <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -21.9
entry(
    index = 842,
    label = "CH2CCH2 + C2H <=> C2H2 + CH2CCH",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -19.8
entry(
    index = 843,
    label = "CH2CCH <=> c-CHCCH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.180e+42, 's^-1'),
        n = -8.89,
        Ea = (96510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (8.290e+40, 's^-1'),
        n = -8.43,
        Ea = (96650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (1.830e+39, 's^-1'),
        n = -7.84,
        Ea = (96560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.430e+37, 's^-1'),
        n = -7.21,
        Ea = (96190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (9.210e+34, 's^-1'),
        n = -6.43,
        Ea = (95480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.870e+32, 's^-1'),
        n = -5.64,
        Ea = (94580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (2.920e+29, 's^-1'),
        n = -4.72,
        Ea = (93370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.350e+26, 's^-1'),
        n = -3.86,
        Ea = (92150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (4.430e+23, 's^-1'),
        n = -2.96,
        Ea = (90860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.070e+21, 's^-1'),
        n = -2.29,
        Ea = (90150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (5.650e+19, 's^-1'),
        n = -1.74,
        Ea = (90150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -42.4
# *** Fuel Radical Decomposition

entry(
    index = 844,
    label = "CH2CCH <=> CHCCH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.300e+38, 's^-1'),
        n = -8.1,
        Ea = (105600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.001 atm
        Arrhenius(
            A = (1.390e+41, 's^-1'),
        n = -8.52,
        Ea = (106100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.003 atm
        Arrhenius(
            A = (6.690e+42, 's^-1'),
        n = -8.79,
        Ea = (107100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (3.380e+43, 's^-1'),
        n = -8.81,
        Ea = (108000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm
        Arrhenius(
            A = (2.720e+43, 's^-1'),
        n = -8.6,
        Ea = (108700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.930e+42, 's^-1'),
        n = -8.2,
        Ea = (109000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm
        Arrhenius(
            A = (7.050e+40, 's^-1'),
        n = -7.55,
        Ea = (109000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.290e+38, 's^-1'),
        n = -6.76,
        Ea = (108600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm
        Arrhenius(
            A = (1.500e+35, 's^-1'),
        n = -5.69,
        Ea = (107600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.890e+31, 's^-1'),
        n = -4.57,
        Ea = (106200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm
        Arrhenius(
            A = (3.030e+27, 's^-1'),
        n = -3.32,
        Ea = (104500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# SJ Klippenstein, JA Miller, AW Jasper, JPCA 119:7780 (2015).
# DH = 85.7

entry(
    index = 845,
    label = "CH3CCH + HO2 <=> CH2CCH + H2O2",
    kinetics = Arrhenius(
        A = (7.710e-02, 'cm^3/(mol*s)'),
        n = 4.4,
        Ea = (13547.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, AW Jasper, JPCA 119:7780 (2015).
# DH = 96.4
# *** Fuel Radical + Stable
entry(
    index = 846,
    label = "CH2CCH2 + HO2 <=> CH2CCH + H2O2",
    kinetics = Arrhenius(
        A = (7.710e-02, 'cm^3/(mol*s)'),
        n = 4.4,
        Ea = (13547.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 4.2
entry(
    index = 847,
    label = "CH2CCH + C2H2 <=> C5H5(L)",
    kinetics = Arrhenius(
        A = (5.620e+32, 'cm^3/(mol*s)'),
        n = -7.3,
        Ea = (6758.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 3.1
entry(
    index = 848,
    label = "CH2CCH + C2H2 <=> C5H5",
    kinetics = Arrhenius(
        A = (7.390e+53, 'cm^3/(mol*s)'),
        n = -12.5,
        Ea = (57313.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 849,
    label = "CH2CCH + O2 <=> CH2CO + HCO",
    kinetics = Arrhenius(
        A = (1.700e+05, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (1500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
# *** Fuel Radical + Radical
entry(
    index = 850,
    label = "CH2CCH + H <=> CHCCH + H2",
    kinetics = Arrhenius(
        A = (2.140e+05, 'cm^3/(mol*s)'),
        n = 2.52,
        Ea = (7453.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# DK Hahn, SJ Klippenstein, JA Miller, Faraday Disc. 119:79 (2001).
# DH = -85.6
entry(
    index = 851,
    label = "CH2CCH + H <=> CHCCH(S) + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.950e+09, 'cm^3/(mol*s)'),
        n = 1.28,
        Ea = (13474.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.100e+10, 'cm^3/(mol*s)'),
        n = 1.13,
        Ea = (13929.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.310e+13, 'cm^3/(mol*s)'),
        n = 0.195,
        Ea = (17579.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller, SJ Klippenstein, JPCA 107:2680 (2003).
# DH = -6.9

entry(
    index = 852,
    label = "CH2CCH + H <=> CH2CC + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.690e+09, 'cm^3/(mol*s)'),
        n = 1.05,
        Ea = (5371.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.880e+13, 'cm^3/(mol*s)'),
        n = -0.03,
        Ea = (9448.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.000e+18, 'cm^3/(mol*s)'),
        n = -1.23,
        Ea = (15111.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
    duplicate = True,
)

# JA Miller - estimate
# DH = ??

entry(
    index = 853,
    label = "CH2CCH + H <=> c-CHCCH + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.070e+07, 'cm^3/(mol*s)'),
        n = 1.37,
        Ea = (15557.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.350e+07, 'cm^3/(mol*s)'),
        n = 1.34,
        Ea = (15560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (7.240e+09, 'cm^3/(mol*s)'),
        n = 0.606,
        Ea = (18356.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -3.9

entry(
    index = 854,
    label = "CH2CCH + O <=> CH2O + C2H",
    kinetics = Arrhenius(
        A = (1.400e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -17.6
entry(
    index = 855,
    label = "CH2CCH + OH <=> CHCCH + H2O",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (8000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,  
)
# IR Slagle, GW Gmurczyk, L Batt, D Gutman, PCI 23:115 (1990).
# DH = -34.4
entry(
    index = 856,
    label = "CH2CCH + OH <=> CH2O + C2H2",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate (2007).
# DH = -21.3
entry(
    index = 857,
    label = "CH2CCH + OH <=> C2H3 + HCO",
    kinetics = Arrhenius(
        A = (7.600e+13, 'cm^3/(mol*s)'),
        n = -0.15,
        Ea = (-45.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate (2007).
# DH = -64.3
entry(
    index = 858,
    label = "CH2CCH + OH <=> C2H4 + CO",
    kinetics = Arrhenius(
        A = (7.600e+13, 'cm^3/(mol*s)'),
        n = -0.15,
        Ea = (-45.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - unpublished (2013).
# DH = -12.0
entry(
    index = 859,
    label = "CH2CCH + OH <=> CHCCH(S) + H2O",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - unpublished (2013).
# DH = -106.5
entry(
    index = 860,
    label = "CH2CCH + OH <=> CH2CC + H2O",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    duplicate = True,
)
# JA Miller - estimate (2007).
# DH = ??
entry(
    index = 861,
    label = "CH2CCH + HO2 <=> CH2O + CHCOH",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate (2007).
# DH = -18.4
entry(
    index = 862,
    label = "CH2CCH + HO2 <=> CH3CCH + O2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate (2014).
# DH = -90.9
entry(
    index = 863,
    label = "CH2CCH + HO2 <=> CH2CCH2 + O2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate (2014).
# DH = -42.3
entry(
    index = 864,
    label = "CH2CCH + HCO <=> CH3CCH + CO",
    kinetics = Arrhenius(
        A = (2.500e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate (2014).
# DH = -41.2
entry(
    index = 865,
    label = "CH2CCH + HCO <=> CH2CCH2 + CO",
    kinetics = Arrhenius(
        A = (2.500e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SG Davis, CK Law, H Wang, JPCA 103:5889 (1999).
# DH = -75.6
entry(
    index = 866,
    label = "CH2CCH + CH3 <=> CH2CCHCH3",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1500000000000.0, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.6e+57, 'cm^6/(mol^2*s)'), n=-11.94, Ea=(9770.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000.0, 'K'),
        T2 = (9769.8, 'K'),
        efficiencies = { '[H][H]': 2.0, 'C': 2.0, 'O': 6.0, '[C-]#[O+]': 1.5, 'CC': 3.0, '[Ar]': 0.7, 'O=C=O': 2.0 }
    ),
)

entry(
    index = 867,
    label = "CH2CCH + CH2 <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (8.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH =-78.3
entry(
    index = 868,
    label = "CH2CCH + CH <=> CH2CCCH + H",
    kinetics = Arrhenius(
        A = (7.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
entry(
    index = 869,
    label = "CH2CCH + CH <=> CHCHCCH + H",
    kinetics = Arrhenius(
        A = (7.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
entry(
    index = 870,
    label = "CH2CCH + C2H <=> H2CCCCCH + H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
entry(
    index = 871,
    label = "CH2CCH + C2H <=> HCCCHCCH + H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
entry(
    index = 872,
    label = "CH2CCH + C2H3 <=> C5H5 + H",
    kinetics = Arrhenius(
        A = (9.630e+40, 'cm^3/(mol*s)'),
        n = -7.8,
        Ea = (28820.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
entry(
    index = 873,
    label = "FULVENE + H <=> C6H6 + H",
    kinetics = Arrhenius(
        A = (3.000e+12, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (2000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 874,
    label = "CH2CCH + CH2CCH <=> C6H5 + H",
    kinetics = Arrhenius(
        A = (2.020e+33, 'cm^3/(mol*s)'),
        n = -6.05,
        Ea = (15940.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, MJ Castaldi, CF Melius, W Tsang, CST 128:295 (1997).
# Marinov et al., CS&T 128:295-342 (1997).
# DH = ??
entry(
    index = 875,
    label = "CH2CCH + CH2CCH <=> C4H5C2H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (6.480e+68, 'cm^3/(mol*s)'),
        n = -16.686,
        Ea = (28720.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),

)
# JA Miller, SJ Klippenstein, JPCA 107:7783 (2003).
# DH = ??
entry(
    index = 876,
    label = "CH2CCH + CH2CCH <=> C4H5C2H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.540e+36, 'cm^3/(mol*s)'),
        n = -7.797,
        Ea = (5580.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),

)
entry(
    index = 877,
    label = "CH2CCH + CH2CCH <=> FULVENE",
    duplicate = True,
    kinetics = Arrhenius(
        A = (7.250e+65, 'cm^3/(mol*s)'),
        n = -16.015,
        Ea = (25035.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),

)
# JA Miller, SJ Klippenstein, JPCA 107:7783 (2003).
# DH = ??
entry(
    index = 878,
    label = "CH2CCH + CH2CCH <=> FULVENE",
    duplicate = True,
    kinetics = Arrhenius(
        A = (4.190e+39, 'cm^3/(mol*s)'),
        n = -8.958,
        Ea = (6098.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),

)
entry(
    index = 879,
    label = "CH2CCH + CH2CCH <=> C6H6",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.640e+66, 'cm^3/(mol*s)'),
        n = -15.902,
        Ea = (27529.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)
# JA Miller, SJ Klippenstein, JPCA 107:7783 (2003).
# DH = ??
entry(
    index = 880,
    label = "CH2CCH + CH2CCH <=> C6H6",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.200e+35, 'cm^3/(mol*s)'),
        n = -7.435,
        Ea = (5058.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)
entry(
    index = 881,
    label = "CHCCH(S) <=> CHCCH",
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),
        efficiencies = None,
    ),
    
)

# JA Miller, SJ Klippenstein, JPCA 107:7783 (2003).
# DH = ??
# *****************************************************************************
#    CHCCH subset                                                             *
#    CH2CC subset                                                             *
#    CHCCH(S) subset                                                          *
#    c-CHCCH subset                                                           *
# *****************************************************************************
# Fuel Radicals: C3H
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition
entry(
    index = 882,
    label = "CHCCH + O2 <=> HCCO + CO + H",
    kinetics = Arrhenius(
        A = (2.550e+06, 'cm^3/(mol*s)'),
        n = 2.245,
        Ea = (368.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
# *** Fuel + Radical
entry(
    index = 883,
    label = "CH2CC + O2 <=> CO2 + C2H2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -62.6
entry(
    index = 884,
    label = "CHCCH(S) + H <=> CH2CC + H",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -171.7
entry(
    index = 885,
    label = "c-CHCCH + O2 <=> C2H2 + CO2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 886,
    label = "CHCCH + H <=> c-CHCCH + H",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.360e+26, 'cm^3/(mol*s)'),
        n = -3.76,
        Ea = (20930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.470e+26, 'cm^3/(mol*s)'),
        n = -3.92,
        Ea = (3253.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.470e+27, 'cm^3/(mol*s)'),
        n = -4.2,
        Ea = (4024.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 1)
        Arrhenius(
            A = (1.460e+26, 'cm^3/(mol*s)'),
        n = -3.58,
        Ea = (19400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 2)
        Arrhenius(
            A = (3.450e+32, 'cm^3/(mol*s)'),
        n = -5.23,
        Ea = (28620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.930e+27, 'cm^3/(mol*s)'),
        n = -4.37,
        Ea = (5005.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (6.860e+48, 'cm^3/(mol*s)'),
        n = -9.45,
        Ea = (52170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 1)
        Arrhenius(
            A = (7.200e+27, 'cm^3/(mol*s)'),
        n = -4.34,
        Ea = (5866.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 2)
        Arrhenius(
            A = (8.710e+123, 'cm^3/(mol*s)'),
        n = -29.01,
        Ea = (153600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.140e+27, 'cm^3/(mol*s)'),
        n = -4.14,
        Ea = (6731.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.440e+34, 'cm^3/(mol*s)'),
        n = -6.13,
        Ea = (12210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 1)
        Arrhenius(
            A = (8.620e+17, 'cm^3/(mol*s)'),
        n = -1.52,
        Ea = (2679.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 2)
        Arrhenius(
            A = (2.030e+37, 'cm^3/(mol*s)'),
        n = -6.99,
        Ea = (16570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (8.510e+19, 'cm^3/(mol*s)'),
        n = -2.04,
        Ea = (4869.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (4.370e+34, 'cm^3/(mol*s)'),
        n = -6.13,
        Ea = (17030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 1)
        Arrhenius(
            A = (1.200e+18, 'cm^3/(mol*s)'),
        n = -1.53,
        Ea = (4783.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 2)
        Arrhenius(
            A = (5.580e+31, 'cm^3/(mol*s)'),
        n = -5.21,
        Ea = (17640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (7.810e+16, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (5011.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# JA Miller - estimate
# DH = -158.0

entry(
    index = 887,
    label = "CH2CC + H <=> c-CHCCH + H",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.170e+23, 'cm^3/(mol*s)'),
        n = -3.23,
        Ea = (2385.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (2.410e+12, 'cm^3/(mol*s)'),
        n = 0.26,
        Ea = (9107.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (1.830e+24, 'cm^3/(mol*s)'),
        n = -3.42,
        Ea = (2841.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 1)
        Arrhenius(
            A = (3.550e+12, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (8850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 2)
        Arrhenius(
            A = (1.430e+16, 'cm^3/(mol*s)'),
        n = -0.72,
        Ea = (14120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (6.730e+24, 'cm^3/(mol*s)'),
        n = -3.56,
        Ea = (3611.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.420e+24, 'cm^3/(mol*s)'),
        n = -3.5,
        Ea = (4328.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 1)
        Arrhenius(
            A = (3.320e+26, 'cm^3/(mol*s)'),
        n = -3.39,
        Ea = (29480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 2)
        Arrhenius(
            A = (1.340e+24, 'cm^3/(mol*s)'),
        n = -3.28,
        Ea = (5104.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (7.640e+37, 'cm^3/(mol*s)'),
        n = -6.27,
        Ea = (48940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (2.250e+26, 'cm^3/(mol*s)'),
        n = -3.89,
        Ea = (7605.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 1)
        Arrhenius(
            A = (1.950e-04, 'cm^3/(mol*s)'),
        n = 4.53,
        Ea = (-8317.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 2)
        Arrhenius(
            A = (5.420e+29, 'cm^3/(mol*s)'),
        n = -4.85,
        Ea = (11330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.380e+08, 'cm^3/(mol*s)'),
        n = 1.27,
        Ea = (-1152.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (5.040e+33, 'cm^3/(mol*s)'),
        n = -5.95,
        Ea = (16070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 1)
        Arrhenius(
            A = (1.070e+12, 'cm^3/(mol*s)'),
        n = 0.23,
        Ea = (2073.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 2)
        Arrhenius(
            A = (1.110e+34, 'cm^3/(mol*s)'),
        n = -5.96,
        Ea = (19250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (6.780e+10, 'cm^3/(mol*s)'),
        n = 0.58,
        Ea = (2743.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# SJ Klippenstein, JA Miller, AW Jasper, JPCA 119:7780 (2015).
# DH = -10.7

entry(
    index = 888,
    label = "CH2CC + H <=> CHCCH + H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.930e-22, 'cm^3/(mol*s)'),
        n = 9.64,
        Ea = (-17240.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 1)
        Arrhenius(
            A = (1.820e+14, 'cm^3/(mol*s)'),
        n = 0.07,
        Ea = (1462.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm (term 2)
        Arrhenius(
            A = (3.810e-08, 'cm^3/(mol*s)'),
        n = 5.85,
        Ea = (-8176.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 1)
        Arrhenius(
            A = (5.470e+14, 'cm^3/(mol*s)'),
        n = -0.07,
        Ea = (1805.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.03 atm (term 2)
        Arrhenius(
            A = (8.470e+18, 'cm^3/(mol*s)'),
        n = -1.36,
        Ea = (4261.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 1)
        Arrhenius(
            A = (3.120e+10, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (212.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm (term 2)
        Arrhenius(
            A = (5.780e+20, 'cm^3/(mol*s)'),
        n = -1.87,
        Ea = (5601.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 1)
        Arrhenius(
            A = (5.140e+10, 'cm^3/(mol*s)'),
        n = 1.05,
        Ea = (841.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.3 atm (term 2)
        Arrhenius(
            A = (1.530e+24, 'cm^3/(mol*s)'),
        n = -2.86,
        Ea = (8239.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (2.140e+12, 'cm^3/(mol*s)'),
        n = 0.62,
        Ea = (2224.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.530e+25, 'cm^3/(mol*s)'),
        n = -3.07,
        Ea = (9906.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 1)
        Arrhenius(
            A = (2.000e+11, 'cm^3/(mol*s)'),
        n = 0.91,
        Ea = (2347.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 3.0 atm (term 2)
        Arrhenius(
            A = (5.150e+28, 'cm^3/(mol*s)'),
        n = -4.04,
        Ea = (13590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.260e+13, 'cm^3/(mol*s)'),
        n = 0.44,
        Ea = (4156.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (6.150e+29, 'cm^3/(mol*s)'),
        n = -4.26,
        Ea = (16090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 1)
        Arrhenius(
            A = (1.280e+13, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (5074.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 30.0 atm (term 2)
        Arrhenius(
            A = (1.080e+29, 'cm^3/(mol*s)'),
        n = -3.95,
        Ea = (17890.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (1.400e+12, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5533.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# SJ Klippenstein, JA Miller, AW Jasper, JPCA 119:7780 (2015).
# DH = -13.6

entry(
    index = 889,
    label = "CHCCH + H <=> C3H + H2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, AW Jasper, JPCA 119:7780 (2015).
# DH = -2.9
entry(
    index = 890,
    label = "CHCCH + O <=> C2H2 + CO",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 891,
    label = "CHCCH + OH <=> C2H2 + HCO",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -161.1
entry(
    index = 892,
    label = "CHCCH + CH3 <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -74.1
entry(
    index = 893,
    label = "CHCCH + CH2 <=> CH2CCCH + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -42.9
entry(
    index = 894,
    label = "CHCCH + CH2(S) <=> CH2CCCH + H",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -52.7
entry(
    index = 895,
    label = "CHCCH + HCCO <=> CHCHCCH + CO",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -61.8
entry(
    index = 896,
    label = "CHCCH + CH2CCH <=> C6H4 + H",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -68.0
entry(
    index = 897,
    label = "C3H + O2 <=> HCCO + CO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 898,
    label = "C3H + O <=> C2H + CO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 899,
    label = "CH2CHCHCH2 <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (5.700e+36, 's^-1'),
        n = -6.27,
        Ea = (112353.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
# *****************************************************************************
#    CH2CHCHCH2 subset                                                        *
#    CH2CCHCH3 subset                                                         *
#    CH3CCCH3 subset                                                          *
# *****************************************************************************
# Fuel Radicals: CH3CCCH2,CH2CHCCH2,CH2CHCHCH
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition
entry(
    index = 900,
    label = "CH2CCHCH3 <=> CH2CHCHCH2",
    kinetics = Arrhenius(
        A = (3.000e+13, 's^-1'),
        n = 0.0,
        Ea = (65000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 100.0
entry(
    index = 901,
    label = "CH2CHCHCH2 <=> CH2CHCHCH + H",
    kinetics = Arrhenius(
        A = (5.300e+44, 's^-1'),
        n = -8.62,
        Ea = (123608.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -12.3
entry(
    index = 902,
    label = "CH2CCHCH3 <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (4.200e+15, 's^-1'),
        n = 0.0,
        Ea = (92600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 110.6
entry(
    index = 903,
    label = "CH3CCCH3 <=> CH2CHCHCH2",
    kinetics = Arrhenius(
        A = (3.000e+13, 's^-1'),
        n = 0.0,
        Ea = (65000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 87.8
entry(
    index = 904,
    label = "CH3CCCH3 <=> CH2CCHCH3",
    kinetics = Arrhenius(
        A = (3.000e+13, 's^-1'),
        n = 0.0,
        Ea = (67000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -8.2
entry(
    index = 905,
    label = "C2H4 + C2H3 <=> CH2CHCHCH2 + H",
    kinetics = Arrhenius(
        A = (4.750e+05, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (2841.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 4.1
# *** Fuel + Radical
entry(
    index = 906,
    label = "CH2CHCHCH2 + H <=> CH2CHCCH2 + H2",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (6000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# I Huzeifa, CF Goldsmith, PR Abel, PT Howe, A Fahr, JB Halpern, LE Jusinski, Y Georgievskii, CA Taatjes, WH Green, JPCA 111:6843 (2007).
# products assumed JA Miller
# DH = -4.8
entry(
    index = 907,
    label = "CH2CHCHCH2 + O <=> CH2CHCCH2 + OH",
    kinetics = Arrhenius(
        A = (7.500e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3740.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -3.3
entry(
    index = 908,
    label = "CH2CHCHCH2 + O <=> HCO + CH2CHCH2",
    kinetics = Arrhenius(
        A = (6.020e+08, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (-858.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -1.7
entry(
    index = 909,
    label = "CH2CHCHCH2 + OH <=> CH2CHCCH2 + H2O",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (2000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# W Tsang, JPCRD 20:221 (1991)
# DH = -36.3
entry(
    index = 910,
    label = "CH2CHCHCH2 + OH <=> CH2CHCHCH + H2O",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -17.8
entry(
    index = 911,
    label = "CH2CHCHCH2 + OH <=> CH3CHO + C2H3",
    kinetics = Arrhenius(
        A = (6.300e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-874.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -7.2
entry(
    index = 912,
    label = "CH2CHCHCH2 + OH <=> CH2CHCH2 + CH2O",
    kinetics = Arrhenius(
        A = (6.300e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (-874.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Liu, WA Mulac, CD Jonah, JPC 92:131 (1988).
# DH = -4.0
entry(
    index = 913,
    label = "CH2CHCHCH2 + CH3 <=> CH2CHCCH2 + CH4",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (19800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Liu, WA Mulac, CD Jonah, JPC 92:131 (1988).
# DH = -21.2
entry(
    index = 914,
    label = "CH2CHCHCH2 + C2H3 <=> CH2CHCCH2 + C2H4",
    kinetics = Arrhenius(
        A = (2.500e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (19800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -3.4
entry(
    index = 915,
    label = "CH2CCHCH3 + H <=> CH2CHCHCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -9.2
entry(
    index = 916,
    label = "CH2CCHCH3 + O <=> CH2CO + C2H4",
    kinetics = Arrhenius(
        A = (1.200e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (327.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -12.3
entry(
    index = 917,
    label = "CH2CCHCH3 + OH <=> CH2CHCCH2 + H2O",
    kinetics = Arrhenius(
        A = (3.100e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (-298.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -97.7
entry(
    index = 918,
    label = "CH2CCHCH3 + CH3 <=> CH2CHCCH2 + CH4",
    kinetics = Arrhenius(
        A = (7.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (18500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -30.
entry(
    index = 919,
    label = "CH2CCH + CH3 <=> CH3CCCH2 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -15.6
entry(
    index = 920,
    label = "CH2CCHCH3 + H <=> CH2CHCCH2 + H2",
    kinetics = Arrhenius(
        A = (1.700e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (2490.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 7.3
entry(
    index = 921,
    label = "CH2CCHCH3 + H <=> CH2CCH2 + CH3",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -15.6
entry(
    index = 922,
    label = "CH2CCHCH3 + H <=> CH3CCH + CH3",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (2000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -10.9
entry(
    index = 923,
    label = "CH2CCHCH3 + O <=> CH2CHCCH2 + OH",
    kinetics = Arrhenius(
        A = (1.800e+11, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5880.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -12.0
entry(
    index = 924,
    label = "CH3CCCH3 + H <=> CH3 + CH3CCH",
    kinetics = Arrhenius(
        A = (2.600e+05, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -13.9
entry(
    index = 925,
    label = "CH3CCCH3 + H <=> CH2CCHCH3 + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -7.9
entry(
    index = 926,
    label = "CH2CHCCH2 <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (3.150e+58, 's^-1'),
        n = -13.954,
        Ea = (64898.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 4.1
# *** Fuel Radical Decomposition
entry(
    index = 927,
    label = "CH2CHCCH2 <=> c-CH2CHCHCH",
    kinetics = Arrhenius(
        A = (3.720e+50, 's^-1'),
        n = -12.58,
        Ea = (40676.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = 44.1
entry(
    index = 928,
    label = "c-CH2CHCHCH <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (2.260e+40, 's^-1'),
        n = -9.0,
        Ea = (49484.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = 3.6
entry(
    index = 929,
    label = "CH2CHCHCH <=> CH2CHCCH + H",
    kinetics = Arrhenius(
        A = (1.120e+47, 's^-1'),
        n = -10.997,
        Ea = (48397.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = 40.6
entry(
    index = 930,
    label = "CH2CHCHCH2 + H <=> CH2CHCHCH + H2",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (13000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA 106:9267 (2002).
# DH = 33.5
# *** Fuel Radical + Stable
entry(
    index = 931,
    label = "CH2CHCHCH2 + HO2 <=> CH2CHCCH2 + H2O2",
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (9920.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 7.3
entry(
    index = 932,
    label = "CH2CHCHCH2 + HO2 <=> CH2CHCHCH + H2O2",
    kinetics = Arrhenius(
        A = (2.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (12600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Dagaut, M Cathonnet, CST 140:225 (1998).
# DH = 13.9
entry(
    index = 933,
    label = "CH2CHCHCH2 + CH3 <=> CH2CHCHCH + CH4",
    kinetics = Arrhenius(
        A = (2.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (22800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Dagaut, M Cathonnet, CST 140:225 (1998).
# DH = 24.5
entry(
    index = 934,
    label = "CH2CHCHCH2 + C2H3 <=> CH2CHCHCH + C2H4",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (22800.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 7.2
entry(
    index = 935,
    label = "CH2CHCHCH2 + CH2CCH <=> CH2CHCHCH + CH2CCH2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (22500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 1.4
entry(
    index = 936,
    label = "CH2CHCHCH2 + CH2CHCH2 <=> CH2CHCCH2 + CH3CHCH2",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (19500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 21.4
entry(
    index = 937,
    label = "CH2CHCHCH2 + CH2CHCH2 <=> CH2CHCHCH + CH3CHCH2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (22500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 13.7
entry(
    index = 938,
    label = "CH2CHCHCH2 + CH2CCH <=> CH2CHCCH2 + CH2CCH2",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (19500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 24.3
entry(
    index = 939,
    label = "C2H2 + CH2CHCCH2 <=> H + C6H6",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.470e+23, 'cm^3/(mol*s)'),
        n = -3.28,
        Ea = (24907.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.470e+23, 'cm^3/(mol*s)'),
        n = -3.28,
        Ea = (24907.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.470e+23, 'cm^3/(mol*s)'),
        n = -3.28,
        Ea = (24907.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.670e+23, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (24959.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.250e+24, 'cm^3/(mol*s)'),
        n = -3.76,
        Ea = (24562.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.370e+32, 'cm^3/(mol*s)'),
        n = -5.84,
        Ea = (35023.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 10.8

entry(
    index = 940,
    label = "C2H2 + CH2CHCCH2 <=> H + FULVENE",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.500e+24, 'cm^3/(mol*s)'),
        n = -3.44,
        Ea = (20319.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.010e+34, 'cm^3/(mol*s)'),
        n = -5.94,
        Ea = (28786.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (6.500e+24, 'cm^3/(mol*s)'),
        n = -3.44,
        Ea = (20319.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.800e+24, 'cm^3/(mol*s)'),
        n = -3.45,
        Ea = (20337.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.700e+25, 'cm^3/(mol*s)'),
        n = -3.76,
        Ea = (21326.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.220e+41, 'cm^3/(mol*s)'),
        n = -7.94,
        Ea = (39597.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??

entry(
    index = 941,
    label = "C2H2 + CH2CHCCH2 <=> H + C4H5C2H",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.590e+18, 'cm^3/(mol*s)'),
        n = -1.43,
        Ea = (30341.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.700e+18, 'cm^3/(mol*s)'),
        n = -1.43,
        Ea = (30351.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (7.290e+18, 'cm^3/(mol*s)'),
        n = -1.46,
        Ea = (30465.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (5.590e+18, 'cm^3/(mol*s)'),
        n = -1.43,
        Ea = (30341.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.620e+19, 'cm^3/(mol*s)'),
        n = -1.69,
        Ea = (31434.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (4.700e+23, 'cm^3/(mol*s)'),
        n = -2.73,
        Ea = (36142.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??

entry(
    index = 942,
    label = "C2H2 + CH2CHCCH2 <=> H + CHCCH2CHCCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.440e+15, 'cm^3/(mol*s)'),
        n = -0.52,
        Ea = (38439.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (6.440e+15, 'cm^3/(mol*s)'),
        n = -0.52,
        Ea = (38439.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (6.440e+15, 'cm^3/(mol*s)'),
        n = -0.52,
        Ea = (38439.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (6.620e+15, 'cm^3/(mol*s)'),
        n = -0.53,
        Ea = (38452.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (9.940e+15, 'cm^3/(mol*s)'),
        n = -0.57,
        Ea = (38647.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.670e+17, 'cm^3/(mol*s)'),
        n = -1.04,
        Ea = (40582.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??

entry(
    index = 943,
    label = "C2H2 + CH2CHCHCH <=> H + C6H6",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.370e+16, 'cm^3/(mol*s)'),
        n = -1.0,
        Ea = (4477.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (2.930e+16, 'cm^3/(mol*s)'),
        n = -1.09,
        Ea = (4660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.370e+16, 'cm^3/(mol*s)'),
        n = -1.0,
        Ea = (4478.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.380e+16, 'cm^3/(mol*s)'),
        n = -1.0,
        Ea = (4479.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.690e+16, 'cm^3/(mol*s)'),
        n = -1.03,
        Ea = (4513.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.640e+16, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (4771.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??

entry(
    index = 944,
    label = "C2H2 + CH2CHCHCH <=> H + FULVENE",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.510e+15, 'cm^3/(mol*s)'),
        n = -0.76,
        Ea = (4412.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.510e+15, 'cm^3/(mol*s)'),
        n = -0.76,
        Ea = (4412.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.520e+15, 'cm^3/(mol*s)'),
        n = -0.76,
        Ea = (4413.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (4.610e+15, 'cm^3/(mol*s)'),
        n = -0.89,
        Ea = (4601.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.730e+19, 'cm^3/(mol*s)'),
        n = -1.86,
        Ea = (6232.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (1.230e+20, 'cm^3/(mol*s)'),
        n = -2.0,
        Ea = (8129.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??

entry(
    index = 945,
    label = "C2H2 + CH2CHCHCH <=> H + CH2CHCHCHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.120e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (8723.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.140e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (8727.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (1.450e+09, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (8777.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (1.120e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        Ea = (8723.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.080e+09, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (9065.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (2.960e+10, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (9784.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??

entry(
    index = 946,
    label = "CH2CHCHCH2 + O <=> CH2CHCHCH + OH",
    kinetics = Arrhenius(
        A = (7.500e+06, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (3740.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, JA Miller, JPCA 111:3740 (2007).
# DH = ??
# *** Fuel Radical + Radical
entry(
    index = 947,
    label = "CH3CCCH2 + O2 <=> CH3CO + CH2CO",
    kinetics = Arrhenius(
        A = (1.700e+05, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (1500.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = 8.9
entry(
    index = 948,
    label = "CH3CCCH2 + H <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -88.0
entry(
    index = 949,
    label = "CH3CCCH2 + OH <=> CH3CO + C2H3",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 2.1
entry(
    index = 950,
    label = "CH3CCCH2 + OH <=> CH2O + CH3CCH",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -14.3
entry(
    index = 951,
    label = "CH3CCCH2 + HO2 <=> OH + C2H2 + CH3CO",
    kinetics = Arrhenius(
        A = (8.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -64.5
entry(
    index = 952,
    label = "CH2CHCHCH + H <=> CH2CHCCH2 + H",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# A Laskin, H Wang, CK Law, IJCK 32:589 (2000).
# DH = -17.2
entry(
    index = 953,
    label = "CH2CHCCH2 + O2 <=> CH2CHO + CH2CO",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -10.6
entry(
    index = 954,
    label = "CH2CHCCH2 + H <=> CH2CCH + CH3",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -97.8
entry(
    index = 955,
    label = "CH2CHCCH2 + H <=> C2H2 + C2H4",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -9.4
entry(
    index = 956,
    label = "CH2CHCCH2 + O <=> C2H3 + CH2CO",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -60.9
entry(
    index = 957,
    label = "CH2CHCCH2 + O <=> CH2O + CH2CCH",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -76.3
entry(
    index = 958,
    label = "CH2CHCCH2 + OH <=> CH2CHCCH + H2O",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -77.9
entry(
    index = 959,
    label = "CH2CHCCH2 + OH <=> C2H4 + CH2CO",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -73.7
entry(
    index = 960,
    label = "CH2CHCCH2 + OH <=> CH2O + CH2CCH2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -83.7
entry(
    index = 961,
    label = "CH2CHCCH2 + OH <=> CH2OH + CH2CCH",
    kinetics = Arrhenius(
        A = (3.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -65.4
entry(
    index = 962,
    label = "CH2CHCHCH2 + O2 <=> CH2CHCCH2 + HO2",
    kinetics = Arrhenius(
        A = (1.400e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (50600.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -5.2
entry(
    index = 963,
    label = "CH2CHCCH2 + C2H <=> FULVENE",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# P Dagaut, M Cathonnet, CST 140:225 (1998).
# DH = 52.0
entry(
    index = 964,
    label = "CH2CHCCH2 + C2H <=> C6H5 + H",
    kinetics = Arrhenius(
        A = (6.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 965,
    label = "CH2CHCCH2 + C2H <=> CH2CCH + CH2CCH",
    kinetics = Arrhenius(
        A = (4.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 966,
    label = "CH2CHCCH2 + C2H <=> CH2CHCCH + C2H2",
    kinetics = Arrhenius(
        A = (3.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -43.5
entry(
    index = 967,
    label = "CH2CHCHCH + O2 <=> CH2CO + CH2CHO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -87.5
entry(
    index = 968,
    label = "CH2CHCHCH + H <=> CH2CHCCH + H2",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -94.0
entry(
    index = 969,
    label = "CH2CHCHCH + OH <=> CH2CHCCH + H2O",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -69.8
entry(
    index = 970,
    label = "CH2CHCHCH + OH <=> HCO + CH2CHCH2",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -84.3
entry(
    index = 971,
    label = "CH2CHCHCH + C2H <=> FULVENE",
    kinetics = Arrhenius(
        A = (4.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -45.2
entry(
    index = 972,
    label = "CH2CHCHCH + C2H <=> C6H5 + H",
    kinetics = Arrhenius(
        A = (1.600e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 973,
    label = "CH2CHCHCH + C2H <=> CH2CHCCH + C2H2",
    kinetics = Arrhenius(
        A = (3.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 974,
    label = "CH2CCCH + H <=> CH2CHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.770e+52, 'cm^3/(mol*s)'),
        n = -12.51,
        Ea = (13040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (4.230e+50, 'cm^3/(mol*s)'),
        n = -13.36,
        Ea = (2448.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (8.160e+59, 'cm^3/(mol*s)'),
        n = -14.09,
        Ea = (20770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (5.880e+91, 'cm^3/(mol*s)'),
        n = -24.7,
        Ea = (26410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.980e+65, 'cm^3/(mol*s)'),
        n = -15.12,
        Ea = (30460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.140e+56, 'cm^3/(mol*s)'),
        n = -13.08,
        Ea = (16980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (4.500e+49, 'cm^3/(mol*s)'),
        n = -11.12,
        Ea = (15160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (5.490e+59, 'cm^3/(mol*s)'),
        n = -13.21,
        Ea = (31300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.240e+49, 'cm^3/(mol*s)'),
        n = -9.97,
        Ea = (28460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (5.860e+38, 'cm^3/(mol*s)'),
        n = -7.84,
        Ea = (10640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.320e+47, 'cm^3/(mol*s)'),
        n = -9.2,
        Ea = (33830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.270e+20, 'cm^3/(mol*s)'),
        n = -2.08,
        Ea = (3352.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

# JA Miller - estimate
# DH = -98.1
# *****************************************************************************
#    CH2CHCCH subset                                                          *
# *****************************************************************************
# Fuel Radicals: CH2CCCH, CHCHCCH
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition

entry(
    index = 975,
    label = "CH2CHCCH <=> CH2CCC + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.320e+58, 's^-1'),
        n = -13.86,
        Ea = (116500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (3.490e+127, 's^-1'),
        n = -36.18,
        Ea = (136800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.330e+66, 's^-1'),
        n = -15.61,
        Ea = (126400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.620e+65, 's^-1'),
        n = -16.15,
        Ea = (117800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.190e+69, 's^-1'),
        n = -16.01,
        Ea = (133700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (9.560e+59, 's^-1'),
        n = -14.1,
        Ea = (119400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.700e+64, 's^-1'),
        n = -14.46,
        Ea = (136100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (2.610e+55, 's^-1'),
        n = -12.64,
        Ea = (120200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.260e+46, 's^-1'),
        n = -9.84,
        Ea = (119000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (4.380e+56, 's^-1'),
        n = -11.92,
        Ea = (136900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (4.490e+44, 's^-1'),
        n = -8.37,
        Ea = (135300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (8.670e+35, 's^-1'),
        n = -6.88,
        Ea = (117900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

# fit btw. 600 and 2500 K with MAE of 3.2%, 10.3%
# fit btw. 600 and 2500 K with MAE of 1.5%, 5.0%
# fit btw. 600 and 2500 K with MAE of 0.9%, 1.9%
# fit btw. 600 and 2500 K with MAE of 2.0%, 4.6%
# fit btw. 600 and 2500 K with MAE of 2.6%, 7.3%
# fit btw. 600 and 2500 K with MAE of 1.6%, 3.5%

entry(
    index = 976,
    label = "CH2CHCCH <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.890e+56, 's^-1'),
        n = -13.27,
        Ea = (111000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (6.630e+158, 's^-1'),
        n = -45.78,
        Ea = (143100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.790e+61, 's^-1'),
        n = -14.05,
        Ea = (119400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.870e+79, 's^-1'),
        n = -20.54,
        Ea = (118000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.370e+63, 's^-1'),
        n = -14.18,
        Ea = (127100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.690e+53, 's^-1'),
        n = -12.07,
        Ea = (111900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.510e+47, 's^-1'),
        n = -10.04,
        Ea = (110500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.580e+57, 's^-1'),
        n = -12.07,
        Ea = (127400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (3.110e+46, 's^-1'),
        n = -8.81,
        Ea = (123500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.950e+37, 's^-1'),
        n = -7.01,
        Ea = (106900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.500e+34, 's^-1'),
        n = -5.23,
        Ea = (117000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (3.640e+26, 's^-1'),
        n = -3.66,
        Ea = (102500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 977,
    label = "CH2CCCH2 <=> CH2CHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.420e+64, 's^-1'),
        n = -15.26,
        Ea = (96560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.550e+198, 's^-1'),
        n = -57.65,
        Ea = (140200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (3.510e+66, 's^-1'),
        n = -15.52,
        Ea = (101800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.210e+96, 's^-1'),
        n = -25.69,
        Ea = (103800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (4.560e+73, 's^-1'),
        n = -17.15,
        Ea = (112700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (6.210e+46, 's^-1'),
        n = -10.03,
        Ea = (87180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (4.120e+54, 's^-1'),
        n = -12.34,
        Ea = (92140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.310e+64, 's^-1'),
        n = -14.32,
        Ea = (109300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (9.360e+47, 's^-1'),
        n = -10.29,
        Ea = (91660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.880e+58, 's^-1'),
        n = -12.4,
        Ea = (109400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.090e+49, 's^-1'),
        n = -9.57,
        Ea = (108000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (7.310e+39, 's^-1'),
        n = -7.95,
        Ea = (89810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 978,
    label = "CH2CCCH2 <=> CH2CCC + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.590e+187, 's^-1'),
        n = -46.33,
        Ea = (328500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.690e+49, 's^-1'),
        n = -11.46,
        Ea = (102300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.480e+52, 's^-1'),
        n = -11.83,
        Ea = (105600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (3.690e+194, 's^-1'),
        n = -57.12,
        Ea = (152000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.160e+59, 's^-1'),
        n = -13.33,
        Ea = (113300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.400e+90, 's^-1'),
        n = -23.86,
        Ea = (117500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.280e+46, 's^-1'),
        n = -9.83,
        Ea = (103600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (2.100e+65, 's^-1'),
        n = -14.64,
        Ea = (123300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.130e+48, 's^-1'),
        n = -10.25,
        Ea = (104500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.130e+58, 's^-1'),
        n = -12.36,
        Ea = (121700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (9.550e+48, 's^-1'),
        n = -9.5,
        Ea = (118500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.470e+39, 's^-1'),
        n = -7.48,
        Ea = (101300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 979,
    label = "CH2CCCH2 <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.230e+49, 's^-1'),
        n = -11.36,
        Ea = (94840.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (6.390e+190, 's^-1'),
        n = -56.33,
        Ea = (140800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.020e+53, 's^-1'),
        n = -11.98,
        Ea = (100700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.110e+93, 's^-1'),
        n = -25.25,
        Ea = (108200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.410e+39, 's^-1'),
        n = -8.18,
        Ea = (90610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (3.580e+58, 's^-1'),
        n = -13.12,
        Ea = (110200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (8.330e+41, 's^-1'),
        n = -8.92,
        Ea = (91940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.120e+52, 's^-1'),
        n = -11.0,
        Ea = (108600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.110e+45, 's^-1'),
        n = -8.85,
        Ea = (106200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.990e+36, 's^-1'),
        n = -7.15,
        Ea = (89940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.350e+37, 's^-1'),
        n = -6.5,
        Ea = (102600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (5.650e+28, 's^-1'),
        n = -4.81,
        Ea = (87060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 980,
    label = "c-(CHCHC)CH2 <=> CH2CHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.390e+59, 's^-1'),
        n = -13.52,
        Ea = (89830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.530e+51, 's^-1'),
        n = -12.17,
        Ea = (55540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.080e+65, 's^-1'),
        n = -14.55,
        Ea = (102000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (7.020e+48, 's^-1'),
        n = -11.14,
        Ea = (56230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (6.750e+92, 's^-1'),
        n = -21.42,
        Ea = (145500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.880e+44, 's^-1'),
        n = -9.49,
        Ea = (56000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.570e+183, 's^-1'),
        n = -44.43,
        Ea = (285500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (8.810e+37, 's^-1'),
        n = -7.39,
        Ea = (54640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.050e+37, 's^-1'),
        n = -6.85,
        Ea = (57240.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.890e+113, 's^-1'),
        n = -31.33,
        Ea = (79760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (5.810e+47, 's^-1'),
        n = -9.59,
        Ea = (71720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (4.450e+23, 's^-1'),
        n = -3.1,
        Ea = (47920.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 981,
    label = "c-(CHCHC)CH2 <=> CH2CCCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.370e+82, 's^-1'),
        n = -19.77,
        Ea = (128100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (3.920e+41, 's^-1'),
        n = -9.35,
        Ea = (69820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (9.400e+27, 's^-1'),
        n = -4.84,
        Ea = (78110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.300e+27, 's^-1'),
        n = -5.01,
        Ea = (62120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.560e+46, 's^-1'),
        n = -9.49,
        Ea = (92970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.750e+40, 's^-1'),
        n = -8.67,
        Ea = (65830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (8.110e+106, 's^-1'),
        n = -25.06,
        Ea = (175100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (2.720e+43, 's^-1'),
        n = -9.15,
        Ea = (69330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.900e+42, 's^-1'),
        n = -8.39,
        Ea = (72040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.100e+183, 's^-1'),
        n = -53.24,
        Ea = (117700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.550e+58, 's^-1'),
        n = -12.46,
        Ea = (90580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (7.940e+29, 's^-1'),
        n = -4.79,
        Ea = (64880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 982,
    duplicate = True,
    label = "c-(CHCHC)CH2 <=> CH2CCC + H2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.570e+39, 's^-1'),
        n = -8.19,
        Ea = (105000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (9.150e+43, 's^-1'),
        n = -10.38,
        Ea = (85820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (2.300e+53, 's^-1'),
        n = -11.51,
        Ea = (120500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.330e+42, 's^-1'),
        n = -9.41,
        Ea = (87900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (3.090e+73, 's^-1'),
        n = -16.52,
        Ea = (149000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (4.070e+37, 's^-1'),
        n = -7.61,
        Ea = (89200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (7.260e+22, 's^-1'),
        n = -2.66,
        Ea = (108800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.210e+25, 's^-1'),
        n = -3.76,
        Ea = (83970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (3.400e+28, 's^-1'),
        n = -4.54,
        Ea = (87150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (3.910e+22, 's^-1'),
        n = -4.84,
        Ea = (69840.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (4.040e+40, 's^-1'),
        n = -7.59,
        Ea = (101000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (9.280e+46, 's^-1'),
        n = -10.5,
        Ea = (93670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 983,
    label = "c-(CHCHC)CH2 <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.940e+45, 's^-1'),
        n = -9.62,
        Ea = (106800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (9.610e+39, 's^-1'),
        n = -8.99,
        Ea = (79110.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.010e+60, 's^-1'),
        n = -13.05,
        Ea = (126300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.590e+36, 's^-1'),
        n = -7.42,
        Ea = (81260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.740e+98, 's^-1'),
        n = -22.83,
        Ea = (177500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.020e+28, 's^-1'),
        n = -4.66,
        Ea = (80190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.090e+20, 's^-1'),
        n = -2.3,
        Ea = (77890.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.750e+144, 's^-1'),
        n = -42.36,
        Ea = (112500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (6.360e+21, 's^-1'),
        n = -2.41,
        Ea = (80820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.440e+133, 's^-1'),
        n = -37.96,
        Ea = (116500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (5.050e+25, 's^-1'),
        n = -3.3,
        Ea = (87990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (7.340e+49, 's^-1'),
        n = -11.69,
        Ea = (88850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 984,
    label = "c-CHCHCHCH <=> CH2CHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.300e+10, 's^-1'),
        n = -1.0,
        Ea = (55950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (6.560e+13, 's^-1'),
        n = -2.19,
        Ea = (49570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (6.670e+16, 's^-1'),
        n = -2.15,
        Ea = (69560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (8.770e+20, 's^-1'),
        n = -3.81,
        Ea = (52520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.660e+58, 's^-1'),
        n = -13.01,
        Ea = (106300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (4.040e+46, 's^-1'),
        n = -10.84,
        Ea = (66460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (2.540e+82, 's^-1'),
        n = -18.83,
        Ea = (141800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.300e+47, 's^-1'),
        n = -10.48,
        Ea = (68810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (4.180e+186, 's^-1'),
        n = -45.53,
        Ea = (287200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.430e+43, 's^-1'),
        n = -8.96,
        Ea = (69580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.890e+40, 's^-1'),
        n = -7.67,
        Ea = (71500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.250e+179, 's^-1'),
        n = -51.57,
        Ea = (117600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 985,
    label = "c-CHCHCHCH <=> CH2CCCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.190e+15, 's^-1'),
        n = -2.77,
        Ea = (59880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (4.320e+15, 's^-1'),
        n = -2.92,
        Ea = (56080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (4.160e+11, 's^-1'),
        n = -1.19,
        Ea = (62190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (9.120e+14, 's^-1'),
        n = -2.26,
        Ea = (56200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.090e+13, 's^-1'),
        n = -1.06,
        Ea = (73310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.470e+17, 's^-1'),
        n = -2.6,
        Ea = (58290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.360e+84, 's^-1'),
        n = -19.59,
        Ea = (150500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.410e+33, 's^-1'),
        n = -6.92,
        Ea = (69860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (3.450e+171, 's^-1'),
        n = -42.09,
        Ea = (270600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (4.560e+35, 's^-1'),
        n = -7.1,
        Ea = (76280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.840e+40, 's^-1'),
        n = -8.0,
        Ea = (85130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (2.060e+179, 's^-1'),
        n = -52.47,
        Ea = (128200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 986,
    label = "c-CHCHCHCH <=> c-(CHCHC)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.150e+14, 's^-1'),
        n = -3.06,
        Ea = (51230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.550e+52, 's^-1'),
        n = -12.24,
        Ea = (112600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.300e+24, 's^-1'),
        n = -5.5,
        Ea = (55910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (4.290e+67, 's^-1'),
        n = -15.88,
        Ea = (132400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (6.760e+14, 's^-1'),
        n = -1.5,
        Ea = (73200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.420e+45, 's^-1'),
        n = -11.17,
        Ea = (66910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.080e+34, 's^-1'),
        n = -6.41,
        Ea = (96280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.340e+46, 's^-1'),
        n = -10.88,
        Ea = (70090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (7.640e+133, 's^-1'),
        n = -32.16,
        Ea = (224600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (6.800e+42, 's^-1'),
        n = -9.38,
        Ea = (73130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (5.800e+34, 's^-1'),
        n = -8.86,
        Ea = (57540.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (2.270e+45, 's^-1'),
        n = -9.53,
        Ea = (81020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 987,
    label = "c-CHCHCHCH <=> CH2CCC + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.200e-03, 's^-1'),
        n = 3.01,
        Ea = (68500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (5.280e-06, 's^-1'),
        n = 2.38,
        Ea = (55000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (3.480e-07, 's^-1'),
        n = 4.24,
        Ea = (63060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (3.440e-08, 's^-1'),
        n = 3.97,
        Ea = (57670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (6.260e-05, 's^-1'),
        n = 3.85,
        Ea = (70270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.370e-01, 's^-1'),
        n = 2.78,
        Ea = (64070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (2.130e+02, 's^-1'),
        n = 2.62,
        Ea = (89030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.440e+06, 's^-1'),
        n = 0.92,
        Ea = (70130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.600e+121, 's^-1'),
        n = -28.73,
        Ea = (226700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (6.490e+19, 's^-1'),
        n = -2.65,
        Ea = (81230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (2.400e+165, 's^-1'),
        n = -39.52,
        Ea = (310400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (6.000e+20, 's^-1'),
        n = -2.66,
        Ea = (86580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 988,
    label = "c-CHCHCHCH <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.490e-03, 's^-1'),
        n = 2.7,
        Ea = (57780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.360e+44, 's^-1'),
        n = -9.39,
        Ea = (110400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (4.340e-03, 's^-1'),
        n = 3.0,
        Ea = (59070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.500e+55, 's^-1'),
        n = -11.97,
        Ea = (125300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.020e+03, 's^-1'),
        n = 1.7,
        Ea = (62490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (6.980e+57, 's^-1'),
        n = -12.24,
        Ea = (134700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (7.730e+06, 's^-1'),
        n = 0.97,
        Ea = (64940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.660e+78, 's^-1'),
        n = -17.24,
        Ea = (165000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.870e+69, 's^-1'),
        n = -14.54,
        Ea = (161100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (3.070e+17, 's^-1'),
        n = -1.79,
        Ea = (72700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (2.040e+159, 's^-1'),
        n = -37.6,
        Ea = (293000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (4.400e+16, 's^-1'),
        n = -1.19,
        Ea = (76390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 989,
    label = "C2H2 + C2H2 <=> CH2CHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.280e+54, 'cm^3/(mol*s)'),
        n = -12.65,
        Ea = (68650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.770e+88, 'cm^3/(mol*s)'),
        n = -24.08,
        Ea = (73900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (3.090e+36, 'cm^3/(mol*s)'),
        n = -7.64,
        Ea = (56790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.490e+62, 'cm^3/(mol*s)'),
        n = -14.56,
        Ea = (79730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.690e+52, 'cm^3/(mol*s)'),
        n = -11.49,
        Ea = (76010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.480e+41, 'cm^3/(mol*s)'),
        n = -9.12,
        Ea = (58940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (2.640e+44, 'cm^3/(mol*s)'),
        n = -8.98,
        Ea = (74000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.000e+33, 'cm^3/(mol*s)'),
        n = -6.64,
        Ea = (56150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (4.300e+23, 'cm^3/(mol*s)'),
        n = -3.6,
        Ea = (52310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (7.660e+33, 'cm^3/(mol*s)'),
        n = -5.84,
        Ea = (69450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (6.500e+26, 'cm^3/(mol*s)'),
        n = -3.75,
        Ea = (67720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (9.560e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (47720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 990,
    label = "C2H2 + C2H2 <=> CH2CCCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.530e+50, 'cm^3/(mol*s)'),
        n = -11.91,
        Ea = (67620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.460e+184, 'cm^3/(mol*s)'),
        n = -54.26,
        Ea = (112000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (6.260e+53, 'cm^3/(mol*s)'),
        n = -12.45,
        Ea = (74780.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.150e+84, 'cm^3/(mol*s)'),
        n = -22.68,
        Ea = (78610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (8.700e+45, 'cm^3/(mol*s)'),
        n = -10.54,
        Ea = (68460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (6.170e+56, 'cm^3/(mol*s)'),
        n = -12.92,
        Ea = (83720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.180e+52, 'cm^3/(mol*s)'),
        n = -11.31,
        Ea = (86560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.400e+42, 'cm^3/(mol*s)'),
        n = -9.51,
        Ea = (69760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (6.840e+43, 'cm^3/(mol*s)'),
        n = -8.81,
        Ea = (87380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.530e+34, 'cm^3/(mol*s)'),
        n = -7.0,
        Ea = (69730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (2.700e+32, 'cm^3/(mol*s)'),
        n = -5.5,
        Ea = (85670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.090e+23, 'cm^3/(mol*s)'),
        n = -3.8,
        Ea = (68210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 991,
    label = "C2H2 + C2H2 <=> c-(CHCHC)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.270e+60, 'cm^3/(mol*s)'),
        n = -13.88,
        Ea = (104000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (4.570e+28, 'cm^3/(mol*s)'),
        n = -6.11,
        Ea = (54550.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (5.280e+70, 'cm^3/(mol*s)'),
        n = -16.37,
        Ea = (121700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (8.550e+20, 'cm^3/(mol*s)'),
        n = -3.58,
        Ea = (52260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (9.260e+102, 'cm^3/(mol*s)'),
        n = -24.65,
        Ea = (165000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (3.660e+13, 'cm^3/(mol*s)'),
        n = -1.22,
        Ea = (49730.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.740e+09, 'cm^3/(mol*s)'),
        n = 0.31,
        Ea = (63910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (9.420e+10, 'cm^3/(mol*s)'),
        n = -0.29,
        Ea = (49960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (3.070e+148, 'cm^3/(mol*s)'),
        n = -44.22,
        Ea = (95820.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (7.900e+11, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (53880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (6.410e+52, 'cm^3/(mol*s)'),
        n = -13.59,
        Ea = (67630.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.970e+17, 'cm^3/(mol*s)'),
        n = -1.68,
        Ea = (62800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 992,
    label = "C2H2 + C2H2 <=> c-CHCHCHCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (9.010e+31, 'cm^3/(mol*s)'),
        n = -6.85,
        Ea = (57270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.990e+47, 'cm^3/(mol*s)'),
        n = -11.8,
        Ea = (50070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (3.440e+54, 'cm^3/(mol*s)'),
        n = -12.46,
        Ea = (86480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (3.770e+45, 'cm^3/(mol*s)'),
        n = -10.94,
        Ea = (50790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.980e+49, 'cm^3/(mol*s)'),
        n = -10.57,
        Ea = (89450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (7.790e+42, 'cm^3/(mol*s)'),
        n = -9.82,
        Ea = (51360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.650e+109, 'cm^3/(mol*s)'),
        n = -25.98,
        Ea = (174600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (6.460e+37, 'cm^3/(mol*s)'),
        n = -8.03,
        Ea = (50850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.210e-04, 'cm^3/(mol*s)'),
        n = 3.89,
        Ea = (27670.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (8.500e+39, 'cm^3/(mol*s)'),
        n = -8.35,
        Ea = (55170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.250e+29, 'cm^3/(mol*s)'),
        n = -4.98,
        Ea = (51280.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.190e+97, 'cm^3/(mol*s)'),
        n = -26.79,
        Ea = (70800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 993,
    label = "C2H2 + C2H2 <=> CH2CCC + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.910e+47, 'cm^3/(mol*s)'),
        n = -10.53,
        Ea = (84970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (8.500e+25, 'cm^3/(mol*s)'),
        n = -4.37,
        Ea = (66480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.520e+84, 'cm^3/(mol*s)'),
        n = -23.57,
        Ea = (83420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (9.900e+32, 'cm^3/(mol*s)'),
        n = -6.27,
        Ea = (72990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.660e+39, 'cm^3/(mol*s)'),
        n = -7.9,
        Ea = (80830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (6.780e+91, 'cm^3/(mol*s)'),
        n = -25.24,
        Ea = (93440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.770e+31, 'cm^3/(mol*s)'),
        n = -5.98,
        Ea = (78610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (4.670e+47, 'cm^3/(mol*s)'),
        n = -10.06,
        Ea = (94330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (3.890e+43, 'cm^3/(mol*s)'),
        n = -8.72,
        Ea = (99370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (4.320e+33, 'cm^3/(mol*s)'),
        n = -6.74,
        Ea = (83300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (4.480e+33, 'cm^3/(mol*s)'),
        n = -5.81,
        Ea = (101200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (2.800e+23, 'cm^3/(mol*s)'),
        n = -3.86,
        Ea = (83430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 994,
    label = "C2H2 + C2H2 <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.120e+30, 'cm^3/(mol*s)'),
        n = -4.93,
        Ea = (81210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.950e+14, 'cm^3/(mol*s)'),
        n = -0.67,
        Ea = (58690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (7.910e+60, 'cm^3/(mol*s)'),
        n = -13.19,
        Ea = (113600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.020e+17, 'cm^3/(mol*s)'),
        n = -1.26,
        Ea = (63530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (9.530e+25, 'cm^3/(mol*s)'),
        n = -3.66,
        Ea = (73450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.220e+12, 'cm^3/(mol*s)'),
        n = -0.15,
        Ea = (62260.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (6.300e+34, 'cm^3/(mol*s)'),
        n = -5.94,
        Ea = (85460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (7.190e+17, 'cm^3/(mol*s)'),
        n = -1.65,
        Ea = (68130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.680e+32, 'cm^3/(mol*s)'),
        n = -5.13,
        Ea = (89400.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.630e+20, 'cm^3/(mol*s)'),
        n = -2.54,
        Ea = (70490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (7.440e+19, 'cm^3/(mol*s)'),
        n = -1.59,
        Ea = (85290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.160e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (67530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 995,
    label = "C2H2 + CH2C <=> CH2CHCCH",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.840e+54, 'cm^3/(mol*s)'),
        n = -12.74,
        Ea = (25960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (8.660e+84, 'cm^3/(mol*s)'),
        n = -23.01,
        Ea = (29990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (7.160e+46, 'cm^3/(mol*s)'),
        n = -10.9,
        Ea = (17460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.030e+56, 'cm^3/(mol*s)'),
        n = -12.92,
        Ea = (31680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.800e+53, 'cm^3/(mol*s)'),
        n = -11.79,
        Ea = (33000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (4.550e+43, 'cm^3/(mol*s)'),
        n = -9.81,
        Ea = (16960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (2.460e+46, 'cm^3/(mol*s)'),
        n = -9.65,
        Ea = (31320.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (2.180e+38, 'cm^3/(mol*s)'),
        n = -8.06,
        Ea = (16130.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.250e+30, 'cm^3/(mol*s)'),
        n = -5.49,
        Ea = (14830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (7.060e+38, 'cm^3/(mol*s)'),
        n = -7.38,
        Ea = (28900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.930e+23, 'cm^3/(mol*s)'),
        n = -3.56,
        Ea = (13350.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (6.620e+32, 'cm^3/(mol*s)'),
        n = -5.55,
        Ea = (28950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 996,
    label = "C2H2 + CH2C <=> CH2CCCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.800e+49, 'cm^3/(mol*s)'),
        n = -11.69,
        Ea = (23950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (7.220e+187, 'cm^3/(mol*s)'),
        n = -55.43,
        Ea = (69940.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.510e+52, 'cm^3/(mol*s)'),
        n = -12.03,
        Ea = (29790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (8.710e+82, 'cm^3/(mol*s)'),
        n = -22.44,
        Ea = (33430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.050e+43, 'cm^3/(mol*s)'),
        n = -9.83,
        Ea = (20210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (5.740e+53, 'cm^3/(mol*s)'),
        n = -12.15,
        Ea = (35830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (2.220e+50, 'cm^3/(mol*s)'),
        n = -10.96,
        Ea = (36720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.100e+41, 'cm^3/(mol*s)'),
        n = -9.11,
        Ea = (20750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.150e+46, 'cm^3/(mol*s)'),
        n = -9.63,
        Ea = (37430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (6.630e+37, 'cm^3/(mol*s)'),
        n = -8.01,
        Ea = (21750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.470e+40, 'cm^3/(mol*s)'),
        n = -7.69,
        Ea = (37990.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (5.370e+30, 'cm^3/(mol*s)'),
        n = -5.91,
        Ea = (20700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 997,
    label = "C2H2 + CH2C <=> c-(CHCHC)CH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.890e+55, 'cm^3/(mol*s)'),
        n = -12.76,
        Ea = (56640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (6.500e+29, 'cm^3/(mol*s)'),
        n = -6.45,
        Ea = (12170.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (2.950e+58, 'cm^3/(mol*s)'),
        n = -13.08,
        Ea = (65610.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.220e+22, 'cm^3/(mol*s)'),
        n = -4.02,
        Ea = (9796.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (4.590e+35, 'cm^3/(mol*s)'),
        n = -6.79,
        Ea = (42620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.570e+12, 'cm^3/(mol*s)'),
        n = -1.12,
        Ea = (1857.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.340e+42, 'cm^3/(mol*s)'),
        n = -8.31,
        Ea = (50710.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.690e+33, 'cm^3/(mol*s)'),
        n = -6.98,
        Ea = (11060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.730e+176, 'cm^3/(mol*s)'),
        n = -42.89,
        Ea = (237200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.580e+32, 'cm^3/(mol*s)'),
        n = -6.23,
        Ea = (13020.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (3.710e+33, 'cm^3/(mol*s)'),
        n = -6.21,
        Ea = (18270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (5.910e+74, 'cm^3/(mol*s)'),
        n = -19.73,
        Ea = (26960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 998,
    label = "C2H2 + CH2C <=> c-CHCHCHCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.580e-05, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (4328.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (4.580e+54, 'cm^3/(mol*s)'),
        n = -13.25,
        Ea = (65430.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.100e+02, 'cm^3/(mol*s)'),
        n = 0.72,
        Ea = (6258.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (7.840e+52, 'cm^3/(mol*s)'),
        n = -12.33,
        Ea = (68900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (7.920e+47, 'cm^3/(mol*s)'),
        n = -10.55,
        Ea = (70880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.210e+08, 'cm^3/(mol*s)'),
        n = -0.77,
        Ea = (9183.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.360e+10, 'cm^3/(mol*s)'),
        n = -1.02,
        Ea = (12360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (2.620e+70, 'cm^3/(mol*s)'),
        n = -16.1,
        Ea = (106300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.000e+63, 'cm^3/(mol*s)'),
        n = -13.94,
        Ea = (104300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.800e+22, 'cm^3/(mol*s)'),
        n = -4.16,
        Ea = (23190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (3.350e+168, 'cm^3/(mol*s)'),
        n = -40.98,
        Ea = (256500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.450e+25, 'cm^3/(mol*s)'),
        n = -4.6,
        Ea = (30030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 999,
    label = "C2H2 + CH2C <=> C2H2 + C2H2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.330e-03, 'cm^3/(mol*s)'),
        n = -5.93,
        Ea = (-68950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.530e+30, 'cm^3/(mol*s)'),
        n = -5.51,
        Ea = (19370.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.830e+36, 'cm^3/(mol*s)'),
        n = -7.12,
        Ea = (26390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.100e+62, 'cm^3/(mol*s)'),
        n = -16.26,
        Ea = (28570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.180e+44, 'cm^3/(mol*s)'),
        n = -9.13,
        Ea = (37290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (3.390e+33, 'cm^3/(mol*s)'),
        n = -6.77,
        Ea = (23470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.110e+43, 'cm^3/(mol*s)'),
        n = -8.81,
        Ea = (42530.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.730e+34, 'cm^3/(mol*s)'),
        n = -7.05,
        Ea = (26100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.420e+35, 'cm^3/(mol*s)'),
        n = -6.36,
        Ea = (42720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.330e+26, 'cm^3/(mol*s)'),
        n = -4.65,
        Ea = (25800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.320e+21, 'cm^3/(mol*s)'),
        n = -2.43,
        Ea = (37750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (3.110e+12, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (23250.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1000,
    label = "C2H2 + CH2C <=> CH2CCC + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.690e+161, 'cm^3/(mol*s)'),
        n = -38.82,
        Ea = (244100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (1.970e+16, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (19720.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (9.870e+107, 'cm^3/(mol*s)'),
        n = -24.95,
        Ea = (162600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (5.260e+20, 'cm^3/(mol*s)'),
        n = -2.61,
        Ea = (23900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.610e+23, 'cm^3/(mol*s)'),
        n = -3.21,
        Ea = (28380.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (3.830e+09, 'cm^3/(mol*s)'),
        n = -3.61,
        Ea = (-9687.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.580e+25, 'cm^3/(mol*s)'),
        n = -3.82,
        Ea = (34060.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.370e+98, 'cm^3/(mol*s)'),
        n = -27.35,
        Ea = (54270.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.140e+31, 'cm^3/(mol*s)'),
        n = -5.25,
        Ea = (44200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.360e+12, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (26660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (2.480e+27, 'cm^3/(mol*s)'),
        n = -4.01,
        Ea = (47490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (8.780e+17, 'cm^3/(mol*s)'),
        n = -2.11,
        Ea = (32100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1001,
    label = "C2H2 + CH2C <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.200e+14, 'cm^3/(mol*s)'),
        n = -0.46,
        Ea = (21960.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (9.190e+12, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (14560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (2.830e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (56090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (7.170e+14, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (18970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.370e+20, 'cm^3/(mol*s)'),
        n = -2.07,
        Ea = (25870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.080e+132, 'cm^3/(mol*s)'),
        n = -37.85,
        Ea = (60870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.140e+27, 'cm^3/(mol*s)'),
        n = -3.97,
        Ea = (37160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (7.070e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (21140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.130e+24, 'cm^3/(mol*s)'),
        n = -2.88,
        Ea = (40520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (9.320e+14, 'cm^3/(mol*s)'),
        n = -1.03,
        Ea = (25210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.160e+14, 'cm^3/(mol*s)'),
        n = -0.05,
        Ea = (38930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (3.860e+05, 'cm^3/(mol*s)'),
        n = 1.67,
        Ea = (24490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1002,
    label = "CH2CCCH + H <=> c-(CHCHC)CH2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (3.770e+52, 'cm^3/(mol*s)'),
        n = -12.51,
        Ea = (13040.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (4.230e+50, 'cm^3/(mol*s)'),
        n = -13.36,
        Ea = (2448.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (8.160e+59, 'cm^3/(mol*s)'),
        n = -14.09,
        Ea = (20770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (5.880e+91, 'cm^3/(mol*s)'),
        n = -24.7,
        Ea = (26410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.980e+65, 'cm^3/(mol*s)'),
        n = -15.12,
        Ea = (30460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.140e+56, 'cm^3/(mol*s)'),
        n = -13.08,
        Ea = (16980.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (4.500e+49, 'cm^3/(mol*s)'),
        n = -11.12,
        Ea = (15160.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (5.490e+59, 'cm^3/(mol*s)'),
        n = -13.21,
        Ea = (31300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.240e+49, 'cm^3/(mol*s)'),
        n = -9.97,
        Ea = (28460.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (5.860e+38, 'cm^3/(mol*s)'),
        n = -7.84,
        Ea = (10640.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.320e+47, 'cm^3/(mol*s)'),
        n = -9.2,
        Ea = (33830.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.270e+20, 'cm^3/(mol*s)'),
        n = -2.08,
        Ea = (3352.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1003,
    label = "CH2CCCH + H <=> CH2CCCH2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.450e+164, 'cm^3/(mol*s)'),
        n = -40.68,
        Ea = (203100.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (2.970e+47, 'cm^3/(mol*s)'),
        n = -11.29,
        Ea = (10360.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (9.320e+48, 'cm^3/(mol*s)'),
        n = -11.25,
        Ea = (12150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (6.980e+41, 'cm^3/(mol*s)'),
        n = -12.13,
        Ea = (-12080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.970e+55, 'cm^3/(mol*s)'),
        n = -12.6,
        Ea = (18810.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (3.280e+105, 'cm^3/(mol*s)'),
        n = -28.96,
        Ea = (31290.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (8.710e+44, 'cm^3/(mol*s)'),
        n = -9.62,
        Ea = (11590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.060e+63, 'cm^3/(mol*s)'),
        n = -14.33,
        Ea = (29850.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (3.500e+56, 'cm^3/(mol*s)'),
        n = -12.18,
        Ea = (28620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (7.540e+47, 'cm^3/(mol*s)'),
        n = -10.46,
        Ea = (13180.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (8.390e+47, 'cm^3/(mol*s)'),
        n = -9.52,
        Ea = (25910.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (3.930e+39, 'cm^3/(mol*s)'),
        n = -7.87,
        Ea = (10200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1004,
    label = "CH2CCCH + H <=> c-(CHCHC)CH2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.540e+30, 'cm^3/(mol*s)'),
        n = -6.01,
        Ea = (21390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (2.610e+44, 'cm^3/(mol*s)'),
        n = -10.96,
        Ea = (9592.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (6.930e+43, 'cm^3/(mol*s)'),
        n = -9.3,
        Ea = (34860.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (7.060e+42, 'cm^3/(mol*s)'),
        n = -9.98,
        Ea = (11150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (2.570e+64, 'cm^3/(mol*s)'),
        n = -14.44,
        Ea = (62490.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (9.380e+36, 'cm^3/(mol*s)'),
        n = -7.83,
        Ea = (11420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.520e+26, 'cm^3/(mol*s)'),
        n = -3.95,
        Ea = (29760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.190e+26, 'cm^3/(mol*s)'),
        n = -4.42,
        Ea = (7390.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (8.100e-05, 'cm^3/(mol*s)'),
        n = -4.12,
        Ea = (-71150.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.080e+25, 'cm^3/(mol*s)'),
        n = -3.91,
        Ea = (7963.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.260e+34, 'cm^3/(mol*s)'),
        n = -6.18,
        Ea = (18600.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (6.060e+70, 'cm^3/(mol*s)'),
        n = -18.39,
        Ea = (24760.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),

)

entry(
    index = 1005,
    label = "CH2CCCH + H <=> c-CHCHCHCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (7.560e+13, 'cm^3/(mol*s)'),
        n = -3.21,
        Ea = (3247.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (2.030e+45, 'cm^3/(mol*s)'),
        n = -10.6,
        Ea = (45090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (2.290e+15, 'cm^3/(mol*s)'),
        n = -3.1,
        Ea = (3692.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (6.000e+45, 'cm^3/(mol*s)'),
        n = -10.36,
        Ea = (48200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (3.370e+10, 'cm^3/(mol*s)'),
        n = -1.19,
        Ea = (2402.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (2.360e+54, 'cm^3/(mol*s)'),
        n = -12.21,
        Ea = (64340.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.790e+05, 'cm^3/(mol*s)'),
        n = 0.51,
        Ea = (773.2, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (2.940e+88, 'cm^3/(mol*s)'),
        n = -20.8,
        Ea = (113300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.280e+77, 'cm^3/(mol*s)'),
        n = -17.44,
        Ea = (107700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.110e+12, 'cm^3/(mol*s)'),
        n = -1.08,
        Ea = (5283.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (2.550e+155, 'cm^3/(mol*s)'),
        n = -37.45,
        Ea = (223900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (4.050e+12, 'cm^3/(mol*s)'),
        n = -0.95,
        Ea = (8932.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1006,
    label = "CH2CCCH + H <=> C2H2 + C2H2",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (8.830e+52, 'cm^3/(mol*s)'),
        n = -10.86,
        Ea = (59080.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (7.180e+26, 'cm^3/(mol*s)'),
        n = -4.28,
        Ea = (6208.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (3.300e+50, 'cm^3/(mol*s)'),
        n = -10.21,
        Ea = (52880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (2.710e+31, 'cm^3/(mol*s)'),
        n = -5.54,
        Ea = (10190.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (1.470e+00, 'cm^3/(mol*s)'),
        n = -6.48,
        Ea = (-77520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (1.450e+34, 'cm^3/(mol*s)'),
        n = -6.18,
        Ea = (15230.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (2.480e+47, 'cm^3/(mol*s)'),
        n = -10.86,
        Ea = (19420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (3.400e+40, 'cm^3/(mol*s)'),
        n = -7.79,
        Ea = (25480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.130e+29, 'cm^3/(mol*s)'),
        n = -5.34,
        Ea = (14880.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.520e+40, 'cm^3/(mol*s)'),
        n = -7.52,
        Ea = (32560.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (5.190e+27, 'cm^3/(mol*s)'),
        n = -3.97,
        Ea = (29420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (1.220e+19, 'cm^3/(mol*s)'),
        n = -2.48,
        Ea = (11420.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1007,
    label = "CH2CCCH + H <=> C2H2 + CH2C",
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.310e-04, 'cm^3/(mol*s)'),
        n = 4.42,
        Ea = (-12090.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (3.230e+25, 'cm^3/(mol*s)'),
        n = -3.48,
        Ea = (5329.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (4.430e+101, 'cm^3/(mol*s)'),
        n = -22.99,
        Ea = (127700.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (8.330e+27, 'cm^3/(mol*s)'),
        n = -4.12,
        Ea = (7874.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (5.420e+17, 'cm^3/(mol*s)'),
        n = -4.83,
        Ea = (-20970.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (3.730e+30, 'cm^3/(mol*s)'),
        n = -4.78,
        Ea = (12200.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (1.860e+33, 'cm^3/(mol*s)'),
        n = -5.43,
        Ea = (17950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (1.610e+86, 'cm^3/(mol*s)'),
        n = -22.76,
        Ea = (30870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (6.770e+22, 'cm^3/(mol*s)'),
        n = -2.81,
        Ea = (11450.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (1.270e+36, 'cm^3/(mol*s)'),
        n = -6.09,
        Ea = (25930.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.450e+33, 'cm^3/(mol*s)'),
        n = -5.17,
        Ea = (29660.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (9.480e+23, 'cm^3/(mol*s)'),
        n = -3.28,
        Ea = (15120.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1008,
    label = "CH2CCCH + H <=> CH2CCC + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.110e+14, 'cm^3/(mol*s)'),
        n = -0.36,
        Ea = (5281.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (2.340e+10, 'cm^3/(mol*s)'),
        n = -1.88,
        Ea = (-13770.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (1.340e+15, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (43410.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (3.260e+15, 'cm^3/(mol*s)'),
        n = -0.69,
        Ea = (6275.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (3.220e+106, 'cm^3/(mol*s)'),
        n = -24.2,
        Ea = (144500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (5.250e+18, 'cm^3/(mol*s)'),
        n = -1.56,
        Ea = (9301.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (3.190e+04, 'cm^3/(mol*s)'),
        n = -2.42,
        Ea = (-32010.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (5.190e+21, 'cm^3/(mol*s)'),
        n = -2.32,
        Ea = (13620.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (1.260e+26, 'cm^3/(mol*s)'),
        n = -3.43,
        Ea = (20680.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (2.060e+84, 'cm^3/(mol*s)'),
        n = -22.44,
        Ea = (34870.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (2.880e+18, 'cm^3/(mol*s)'),
        n = -1.84,
        Ea = (13440.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (2.730e+29, 'cm^3/(mol*s)'),
        n = -4.2,
        Ea = (29580.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1009,
    label = "CH2CCCH + H <=> CHCCCH + H2",
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.0009869, 0.009869, 0.09869, 0.9869, 9.869, 98.69], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (4.010e+49, 'cm^3/(mol*s)'),
        n = -9.48,
        Ea = (63470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 1)
        Arrhenius(
            A = (3.360e+12, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (1914.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0009869 atm (term 2)
        Arrhenius(
            A = (3.590e+41, 'cm^3/(mol*s)'),
        n = -7.31,
        Ea = (52480.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 1)
        Arrhenius(
            A = (1.180e+15, 'cm^3/(mol*s)'),
        n = -0.56,
        Ea = (4030.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.009869 atm (term 2)
        Arrhenius(
            A = (6.660e+162, 'cm^3/(mol*s)'),
        n = -38.76,
        Ea = (221800.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 1)
        Arrhenius(
            A = (4.590e+16, 'cm^3/(mol*s)'),
        n = -0.94,
        Ea = (6807.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.09869 atm (term 2)
        Arrhenius(
            A = (5.650e+19, 'cm^3/(mol*s)'),
        n = -1.7,
        Ea = (12350.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 1)
        Arrhenius(
            A = (4.600e+69, 'cm^3/(mol*s)'),
        n = -18.07,
        Ea = (24690.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.9869 atm (term 2)
        Arrhenius(
            A = (2.820e+23, 'cm^3/(mol*s)'),
        n = -2.59,
        Ea = (21300.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 1)
        Arrhenius(
            A = (4.500e+12, 'cm^3/(mol*s)'),
        n = -0.04,
        Ea = (7451.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 9.869 atm (term 2)
        Arrhenius(
            A = (1.310e+16, 'cm^3/(mol*s)'),
        n = -0.49,
        Ea = (20510.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 1)
        Arrhenius(
            A = (5.670e+07, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (6348.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 98.69 atm (term 2)
        ],
    ),
)

entry(
    index = 1010,
    label = "CH2CHCCH + H <=> CH2CCCH + H2",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# Zdor, Fellows, Miller: Initiation Reactions in Acetylene Pyrolysis
# Journal of Physical Chemistry A
# *** Fuel + Radical
entry(
    index = 1011,
    label = "CH2CHCCH + OH <=> CHCHCCH + H2O",
    kinetics = Arrhenius(
        A = (7.500e+06, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -3.9
entry(
    index = 1012,
    label = "CH2CHCCH + OH <=> CH2CCCH + H2O",
    kinetics = Arrhenius(
        A = (1.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (2000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -6.0
entry(
    index = 1013,
    label = "CH2CHCCH + OH <=> HCCO + C2H4",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -18.3
entry(
    index = 1014,
    label = "CH2CHCCH + OH <=> CH2O + CH2CCH",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -23.1
entry(
    index = 1015,
    label = "CH2CHCCH + CH2 <=> C5H5 + H",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -20.4
entry(
    index = 1016,
    label = "CHCCCH + H <=> CH2CCCH",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(43100000000.0, 'cm^3/(mol*s)'), n=1.158, Ea=(1753.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(2.3e+45, 'cm^6/(mol^2*s)'), n=-8.095, Ea=(2507.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.0748,
        T3 = (1e-50, 'K'),
        T1 = (-4215.9, 'K'),
        T2 = (1e+50, 'K'),
        efficiencies = { '[H][H]': 2.0, '[C-]#[O+]': 2.0, 'O=C=O': 3.0, 'O': 5.0 }
    ),
)

entry(
    index = 1017,
    label = "CHCCCH + H <=> CHCHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.0263, 0.118, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.440e+63, 'cm^3/(mol*s)'),
        n = -15.66,
        Ea = (24018.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0263 atm (term 1)
        Arrhenius(
            A = (4.170e+32, 'cm^3/(mol*s)'),
        n = -6.493,
        Ea = (9726.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0263 atm (term 2)
        Arrhenius(
            A = (1.890e+57, 'cm^3/(mol*s)'),
        n = -13.616,
        Ea = (22832.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.118 atm (term 1)
        Arrhenius(
            A = (1.610e+30, 'cm^3/(mol*s)'),
        n = -5.613,
        Ea = (9389.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.118 atm (term 2)
        Arrhenius(
            A = (7.310e+49, 'cm^3/(mol*s)'),
        n = -11.049,
        Ea = (21571.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 1)
        Arrhenius(
            A = (3.470e+26, 'cm^3/(mol*s)'),
        n = -4.333,
        Ea = (8703.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm (term 2)
        Arrhenius(
            A = (1.910e+41, 'cm^3/(mol*s)'),
        n = -8.18,
        Ea = (19790.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 1)
        Arrhenius(
            A = (1.050e+25, 'cm^3/(mol*s)'),
        n = -3.791,
        Ea = (8466.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm (term 2)
        Arrhenius(
            A = (5.860e+35, 'cm^3/(mol*s)'),
        n = -6.329,
        Ea = (19322.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 1)
        Arrhenius(
            A = (5.530e+20, 'cm^3/(mol*s)'),
        n = -2.319,
        Ea = (7604.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm (term 2)
        ],
    ),
)

# SJ Klippenstein, JA Miller, JPCA, 109:4285 (2005).
# DH = -42.6

entry(
    index = 1018,
    label = "CH2CHCCH + H <=> CHCHCCH + H2",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (15000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA, 109:4285 (2005).
# DH = -30.3
# *** Fuel Radical + Stable
entry(
    index = 1019,
    label = "CHCHCCH + C2H2 <=> C6H5",
    kinetics = Arrhenius(
        A = (1.670e+10, 'cm^3/(mol*s)'),
        n = 0.446,
        Ea = (7719.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 8.5
entry(
    index = 1020,
    label = "CH2CCCH + O2 <=> CH2CO + HCCO",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# CJ Pope, JA Miller, PCI 28:1519 (2000).
# DH = ??
# *** Fuel Radical + Radical
entry(
    index = 1021,
    label = "CH2CCCH + O <=> CH2CO + C2H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -87.0
entry(
    index = 1022,
    label = "CH2CCCH + O <=> H2C4O + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -53.9
entry(
    index = 1023,
    label = "CH2CCCH + OH <=> CHCCCH + H2O",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -72.1
entry(
    index = 1024,
    label = "CH2CCCH + CH3 <=> C5H5(L) + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -75.2
entry(
    index = 1025,
    label = "CH2CCCH + CH2 <=> CH2CCH2 + C2H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# SJ Klippenstein, JA Miller, JPCA, 109:4285 (2005).
# DH = ??
entry(
    index = 1026,
    label = "CH2CCCH + C2H3 <=> FULVENE",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -30.4
entry(
    index = 1027,
    label = "CH2CCCH + C2H3 <=> C6H5 + H",
    kinetics = Arrhenius(
        A = (6.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1028,
    label = "CH2CCCH + C2H3 <=> CH2CCH + CH2CCH",
    kinetics = Arrhenius(
        A = (4.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1029,
    label = "CH2CCCH + C2H3 <=> CHCCCH + C2H4",

    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -21.2
entry(
    index = 1030,
    label = "CH2CCCH + C2H3 <=> CH2CHCCH + C2H2",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -66.6
entry(
    index = 1031,
    label = "H + CHCHCCH <=> CH2CCCH + H",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -65.1
entry(
    index = 1032,
    label = "H + CHCHCCH <=> C2H2 + C2H2",
    kinetics = Arrhenius(
        A = (5.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -12.4
entry(
    index = 1033,
    label = "CHCHCCH + CH3 <=> C5H5 + H",
    kinetics = Arrhenius(
        A = (3.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -73.3
entry(
    index = 1034,
    label = "CHCHCCH + C2H3 <=> FULVENE",
    kinetics = Arrhenius(
        A = (4.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = ??
entry(
    index = 1035,
    label = "CHCHCCH + C2H3 <=> C6H5 + H",
    kinetics = Arrhenius(
        A = (1.600e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1036,
    label = "CHCHCCH + C2H3 <=> CHCCCH + C2H4",
    kinetics = Arrhenius(
        A = (1.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1037,
    label = "CHCHCCH + C2H3 <=> CH2CHCCH + C2H2",
    kinetics = Arrhenius(
        A = (2.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -78.9
entry(
    index = 1038,
    label = "CHCCCH + OH <=> CO + CH2CCH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.580e+19, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (3034.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (1.690e+28, 'cm^3/(mol*s)'),
        n = -4.59,
        Ea = (20140.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (7.650e+20, 'cm^3/(mol*s)'),
        n = -2.83,
        Ea = (4638.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (2.110e+23, 'cm^3/(mol*s)'),
        n = -3.47,
        Ea = (7590.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.630e+26, 'cm^3/(mol*s)'),
        n = -4.18,
        Ea = (13082.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.200e+31, 'cm^3/(mol*s)'),
        n = -5.36,
        Ea = (31879.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -77.5
# *****************************************************************************
#    CHCCCH subset                                                            *
# *****************************************************************************
# Fuel Radicals: C4H
# New Radicals Formed:
# New Fuels:
# *** Fuel + Radical

entry(
    index = 1039,
    label = "CHCCCH + OH <=> H + H2C4O",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.630e+15, 'cm^3/(mol*s)'),
        n = -1.13,
        Ea = (2549.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (5.520e+19, 'cm^3/(mol*s)'),
        n = -2.35,
        Ea = (7229.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (4.610e+23, 'cm^3/(mol*s)'),
        n = -3.35,
        Ea = (13059.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (8.190e+16, 'cm^3/(mol*s)'),
        n = -1.59,
        Ea = (4204.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.220e+22, 'cm^3/(mol*s)'),
        n = -2.77,
        Ea = (17186.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (3.100e+18, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (22113.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, PCI 31:185 (2007).
# DH = -61.1

entry(
    index = 1040,
    label = "CHCCCH + OH <=> H + OCCHCCH",
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.025, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.370e+07, 'cm^3/(mol*s)'),
        n = 1.29,
        Ea = (8866.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.01 atm
        Arrhenius(
            A = (7.050e+07, 'cm^3/(mol*s)'),
        n = 1.26,
        Ea = (8967.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.025 atm
        Arrhenius(
            A = (2.910e+08, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (9506.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.1 atm
        Arrhenius(
            A = (3.930e+11, 'cm^3/(mol*s)'),
        n = 0.24,
        Ea = (12464.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (1.010e+16, 'cm^3/(mol*s)'),
        n = -0.92,
        Ea = (17756.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        Arrhenius(
            A = (5.310e+19, 'cm^3/(mol*s)'),
        n = -1.84,
        Ea = (24834.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 100.0 atm
        ],
    ),
)

# JP Senosiain, SJ Klippenstein, JA Miller, PCI 31:185 (2007).
# DH = -13.0

entry(
    index = 1041,
    label = "CH2 + CHCCCH <=> H2CCCCCH + H",
    kinetics = Arrhenius(
        A = (1.300e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4326.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, PCI 31:185 (2007).
# DH = -17.2
entry(
    index = 1042,
    label = "CHCCCH + O <=> CHCCH + CO",
    kinetics = Arrhenius(
        A = (1.200e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# T Bohland, F Temps, HGg Wagner, PCI 21:841 (1986).
# DH = -15.4
entry(
    index = 1043,
    label = "CH2(S) + CHCCCH <=> H2CCCCCH + H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.540e+16, 'cm^3/(mol*s)'),
        n = -0.9,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, RE Mitchell, MD Smookte, RJ Kee, PCI 19:181 (1982).
# JA Miller - estimate
# DH = -66.4
entry(
    index = 1044,
    label = "CH2(S) + CHCCCH <=> HCCCHCCH + H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.540e+16, 'cm^3/(mol*s)'),
        n = -0.9,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -24.5
entry(
    index = 1045,
    label = "CH + CHCCCH <=> C5H2 + H",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller, SJ Klippenstein - estimate
# DH = -22.4
entry(
    index = 1046,
    label = "CHCCCH + C2H <=> C6H2 + H",
    kinetics = Arrhenius(
        A = (4.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -25.8
entry(
    index = 1047,
    label = "CHCCCH + OH <=> H2O + C4H",
    kinetics = Arrhenius(
        A = (9.150e+09, 'cm^3/(mol*s)'),
        n = 1.03,
        Ea = (21746.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
# *** Fuel Radical + Stable
entry(
    index = 1048,
    label = "C4H + H2 <=> CHCCCH + H",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JP Senosiain, SJ Klippenstein, JA Miller, PCI 31:185 (2007).
# DH = 16.2
entry(
    index = 1049,
    label = "C4H + O2 <=> CO + CO + C2H",
    kinetics = Arrhenius(
        A = (1.200e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -30.6
# *** Fuel Radical + Radical
entry(
    index = 1050,
    label = "H2C4O + OH <=> C2H2 + CO + HCO",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -111.6
# *****************************************************************************
#    H2C4O subset                                                             *
# *****************************************************************************
# Fuel Radicals:
# New Radicals Formed:
# New Fuels:
entry(
    index = 1051,
    label = "CH2CCH + CH2CCH <=> HCCCHCCH + CH3",
    kinetics = Arrhenius(
        A = (5.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -25.8
# *****************************************************************************
#     C5H3 subset                                                             *
# *****************************************************************************
# Fuel Radicals: C5H3
# New Radicals Formed:
entry(
    index = 1052,
    label = "CHCCH + C2H2 <=> HCCCHCCH + H",
    kinetics = Arrhenius(
        A = (5.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 4.6
entry(
    index = 1053,
    label = "C5H6 + O2 <=> C5H5 + HO2",
    kinetics = Arrhenius(
        A = (2.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (25000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = 5.7
# *****************************************************************************
#     C5H6 subset                                                             *
# *****************************************************************************
# Fuel Radicals: C5H5
# New Radicals Formed: C5H5(L)
# *** Fuel + Radical
entry(
    index = 1054,
    label = "H + C5H6 <=> CH2CHCH2 + C2H2",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (12000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1055,
    label = "C5H6 + H <=> C5H5 + H2",
    kinetics = Arrhenius(
        A = (2.190e+08, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (3000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1056,
    label = "C5H6 + O <=> C5H5 + OH",
    kinetics = Arrhenius(
        A = (1.810e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (3080.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1057,
    label = "C5H6 + OH <=> C5H5 + H2O",
    kinetics = Arrhenius(
        A = (3.430e+09, 'cm^3/(mol*s)'),
        n = 1.2,
        Ea = (-447.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1058,
    label = "C5H6 + HO2 <=> C5H5 + H2O2",
    kinetics = Arrhenius(
        A = (1.990e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (11660.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1059,
    label = "C5H5 <=> C5H5(L)",
    kinetics = Arrhenius(
        A = (4.090e+47, 's^-1'),
        n = -10.4,
        Ea = (54874.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
# *** Fuel Radical Decomposition
entry(
    index = 1060,
    label = "C5H5 + H <=> C5H6",
    kinetics = Arrhenius(
        A = (2.920e+29, 'cm^3/(mol*s)'),
        n = -4.7,
        Ea = (6148.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
# *** Fuel Radical + Stable
# *** Fuel Radical + Radical
entry(
    index = 1061,
    label = "C5H4 + H2 <=> C5H5 + H",
    kinetics = Arrhenius(
        A = (3.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (7000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1062,
    label = "C5H4 + H2O <=> C5H5 + OH",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1063,
    label = "C5H5 + O <=> CH2CHCHCH + CO",
    kinetics = Arrhenius(
        A = (1.000e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1064,
    label = "H2CCCCCH + H <=> C5H2 + H2",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
# *****************************************************************************
#    H2CCCCCH subset                                                          *
# *****************************************************************************
# Fuel Radicals: H2CCCCCH
# New Radicals Formed:
# New Fuels:
entry(
    index = 1065,
    label = "H2CCCCCH + CH3 <=> FULVENE",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
entry(
    index = 1066,
    label = "H2CCCCCH + CH3 <=> C6H5 + H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1067,
    label = "H2CCCCCH + CH3 <=> C6H6",
    kinetics = Arrhenius(
        A = (5.000e+10, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1068,
    label = "H2CCCCCH + CH3 <=> C5H2 + CH4",
    duplicate = True,
    kinetics = Arrhenius(
        A = (3.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1069,
    label = "HCCCHCCH + H <=> C5H2 + H2",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -13.9
entry(
    index = 1070,
    label = "HCCCHCCH + H <=> H2CCCCCH + H",
    kinetics = Arrhenius(
        A = (1.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -15.9
entry(
    index = 1071,
    label = "HCCCHCCH + CH3 <=> FULVENE",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -2.1
entry(
    index = 1072,
    label = "HCCCHCCH + CH3 <=> C6H5 + H",
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.000e+11, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1073,
    label = "HCCCHCCH + CH3 <=> C5H2 + CH4",
    duplicate = True,
    kinetics = Arrhenius(
        A = (3.000e+12, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (5000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1074,
    label = "C6H5 + H2 <=> C6H6 + H",
    kinetics = Arrhenius(
        A = (5.710e+04, 'cm^3/(mol*s)'),
        n = 2.43,
        Ea = (6277.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = -15.9
# *****************************************************************************
#    C6H6 subset                                                              *
# *****************************************************************************
# Fuel Radicals: C6H5
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition
# *** Fuel + Radical
entry(
    index = 1075,
    label = "C6H6 + O <=> C6H5 + OH",
    kinetics = Arrhenius(
        A = (2.400e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (4700.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# AM Mebel, MC Lin, T Yu, K Morokuma, JPCA 101:3189 (1997).
# DH = ??
entry(
    index = 1076,
    label = "C6H6 + OH <=> C6H5 + H2O",
    kinetics = Arrhenius(
        A = (4.030e+02, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (1455.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# T Ko, GY Adusei, A Fontijn, JPC 95:8745 (1991).
# DH = ??
entry(
    index = 1077,
    label = "C6H5 + CH4 <=> CH3 + C6H6",
    kinetics = Arrhenius(
        A = (3.890e-03, 'cm^3/(mol*s)'),
        n = 4.57,
        Ea = (5256.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# IV Tokmakov, MC Lin, JPCA 106:11309 (2002).
# DH = ??
entry(
    index = 1078,
    label = "CH2(S) + C6H6 <=> C6H5 + CH3",
    kinetics = Arrhenius(
        A = (1.700e+14, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# IV Tokmakov, J Park, S Gheyas, MC Lin, JPCA 103:3636 (1999)
# DH = ??
entry(
    index = 1079,
    label = "C6H5 <=> C6H4 + H",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4300000000000.0, 's^-1'), n=0.62, Ea=(77294.0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(1e+84, 'cm^3/(mol*s)'), n=-18.87, Ea=(90091.0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.902,
        T3 = (696.0, 'K'),
        T1 = (358.0, 'K'),
        T2 = (3856.0, 'K'),
        efficiencies = { '[H][H]': 2.0, '[C-]#[O+]': 2.0, 'O=C=O': 3.0, 'O': 5.0 }
    ),
)

entry(
    index = 1080,
    label = "H + C6H5 <=> C6H4 + H2",
    kinetics = Arrhenius(
        A = (2.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# H Wang, A Laskin, NW Moriarty, M Frenklach, PCI 28:1545 (2000).
# DH = ??
# *** Fuel Radical + Stable
entry(
    index = 1081,
    label = "C6H5 + O <=> C5H5 + CO",
    kinetics = Arrhenius(
        A = (9.000e+13, 'cm^3/(mol*s)'),
        n = 0.0,
        Ea = (0.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# JA Miller - estimate
# DH = ??
entry(
    index = 1082,
    label = "C6H5 + OH <=> C6H4 + H2O",
    kinetics = Arrhenius(
        A = (1.000e+07, 'cm^3/(mol*s)'),
        n = 2.0,
        Ea = (1000.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    
)
# NM Marinov, WJ Pitz, CK Westbrook, AE Lutz, AM Vincitore, SM Senkan, PCI 27:905 (1998).
# H Richter, WJ Grieco, JB Howard, CF 119:1 (1999).
# DH = ??
entry(
    index = 1083,
    label = "C4H5C2H <=> FULVENE",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.750e+76, 's^-1'),
        n = -18.67,
        Ea = (95531.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.340e+56, 's^-1'),
        n = -12.55,
        Ea = (86405.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (4.900e+26, 's^-1'),
        n = -4.144,
        Ea = (65424.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# CJ Pope - estimate
# DH = ??

entry(
    index = 1084,
    label = "C4H5C2H <=> C6H6",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (6.760e+98, 's^-1'),
        n = -24.58,
        Ea = (122310.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.620e+53, 's^-1'),
        n = -11.34,
        Ea = (100210.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.820e+51, 's^-1'),
        n = -10.68,
        Ea = (106950.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = ??

entry(
    index = 1085,
    label = "C4H5C2H <=> C6H5 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.690e+84, 's^-1'),
        n = -20.14,
        Ea = (121900.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (4.170e+77, 's^-1'),
        n = -17.68,
        Ea = (133520.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (3.090e+43, 's^-1'),
        n = -7.928,
        Ea = (118650.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = ??

entry(
    index = 1086,
    label = "FULVENE <=> C6H6",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (5.620e+81, 's^-1'),
        n = -19.36,
        Ea = (121500.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (1.450e+45, 's^-1'),
        n = -8.9,
        Ea = (96999.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (2.950e+31, 's^-1'),
        n = -4.97,
        Ea = (88465.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = ??

entry(
    index = 1087,
    label = "FULVENE <=> C6H5 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (2.570e+97, 's^-1'),
        n = -23.16,
        Ea = (153470.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (2.240e+68, 's^-1'),
        n = -14.65,
        Ea = (142570.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (8.510e+24, 's^-1'),
        n = -2.505,
        Ea = (113330.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = ??

entry(
    index = 1088,
    label = "C6H6 <=> C6H5 + H",
    kinetics = PDepArrhenius(
        pressures = ([0.0395, 1.0, 10.0], 'atm'),
        arrhenius = [
        Arrhenius(
            A = (1.350e+108, 's^-1'),
        n = -25.81,
        Ea = (181750.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 0.0395 atm
        Arrhenius(
            A = (6.310e+60, 's^-1'),
        n = -12.4,
        Ea = (148070.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 1.0 atm
        Arrhenius(
            A = (5.500e+38, 's^-1'),
        n = -6.178,
        Ea = (132000.0, 'cal/mol'),
        T0 = (1, 'K'),
        ),  # at P = 10.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = ??
# JA Miller - estimate
# DH = ??




entry(
    index = 37,
    label = "CH2O <=> HCO + H",
    kinetics = PDepArrhenius(
                pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.290e+22, 's^-1'), n=-4.007, Ea=(92728.5, 'cal/mol'), T0=(1, 'K')),  # at 0.001 atm
            Arrhenius(A=(3.577e+22, 's^-1'), n=-3.999, Ea=(92631.9, 'cal/mol'), T0=(1, 'K')),  # at 0.003 atm
            Arrhenius(A=(1.100e+23, 's^-1'), n=-3.990, Ea=(92443.9, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(3.120e+23, 's^-1'), n=-3.983, Ea=(92285.1, 'cal/mol'), T0=(1, 'K')),  # at 0.03 atm
            Arrhenius(A=(1.060e+24, 's^-1'), n=-3.985, Ea=(92869.3, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(3.670e+24, 's^-1'), n=-4.000, Ea=(91170.0, 'cal/mol'), T0=(1, 'K')),  # at 0.3 atm
            Arrhenius(A=(1.480e+25, 's^-1'), n=-4.022, Ea=(91010.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(1.070e+26, 's^-1'), n=-4.121, Ea=(90850.0, 'cal/mol'), T0=(1, 'K')),  # at 3.0 atm
            Arrhenius(A=(5.830e+27, 's^-1'), n=-4.443, Ea=(91187.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(1.370e+29, 's^-1'), n=-4.669, Ea=(91822.0, 'cal/mol'), T0=(1, 'K')),  # at 30.0 atm
            Arrhenius(A=(7.770e+29, 's^-1'), n=-4.712, Ea=(92510.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

entry(
    index = 41,
    label = "CH2O + H <=> HCO + H2",
    kinetics = PDepArrhenius(
                pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.713e+03, 'cm^3/(mol*s)'), n=3.130, Ea=(-808.9, 'cal/mol'), T0=(1, 'K')),  # at 0.03947 atm
            Arrhenius(A=(2.051e+03, 'cm^3/(mol*s)'), n=3.130, Ea=(-514.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(2.324e+03, 'cm^3/(mol*s)'), n=3.130, Ea=(-304.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
        ],
    ),
)
# JA Miller - estimate
# DH = ??
# *** Fuel + Radical
# CH2O + O2 is endothermic


entry(
    index = 47,
    label = "CH2O + OH <=> HCO + H2O",
    kinetics = PDepArrhenius(
                pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(7.820e+07, 'cm^3/(mol*s)'), n=1.630, Ea=(-817.3, 'cal/mol'), T0=(1, 'K')),  # at 0.03947 atm
            Arrhenius(A=(7.820e+07, 'cm^3/(mol*s)'), n=1.630, Ea=(-877.6, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(7.820e+07, 'cm^3/(mol*s)'), n=1.630, Ea=(-917.2, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
        ],
    ),
)

# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al.
# JPCRD 34:757 (2005)
# ΔH = -15.0 kcal/mol


entry(
    index = 50,
    label = "CH2O + HO2 <=> HCO + H2O2",
    kinetics = PDepArrhenius(
                pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.094e+04, 'cm^3/(mol*s)'), n=2.500, Ea=(10777.5, 'cal/mol'), T0=(1, 'K')),  # at 0.03947 atm
            Arrhenius(A=(4.096e+04, 'cm^3/(mol*s)'), n=2.500, Ea=(10696.6, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(4.093e+04, 'cm^3/(mol*s)'), n=2.500, Ea=(10634.1, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
        ],
    ),
)

# Fit by R. Sivaramakrishnan to unpublished results from SJK
# The low pressure limit has been scaled by 1.42 to set N2 as the bath gas (3.688E+30 x 1.42 = 5.237E+30)
# ΔH = -20.2 kcal/mol
# *** Fuel Radical Decomposition
# Included in CO submechanism
# *** Fuel Radical + Stable
# FNEMECHGEN: This reaction has had fne factor applied

entry(
    index = 59,
    label = "CH2O + O2 <=> HCO + HO2",
    kinetics = PDepArrhenius(
                pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(8.070e+15, 'cm^3/(mol*s)'), n=0.000, Ea=(53417.0, 'cal/mol'), T0=(1, 'K')),  # at 0.03947 atm
            Arrhenius(A=(8.070e+15, 'cm^3/(mol*s)'), n=0.000, Ea=(53417.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(8.070e+15, 'cm^3/(mol*s)'), n=0.000, Ea=(53417.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
        ],
    ),
)
#  W Tsang, RF Hampson, JPCRD 15:1087 (1986).
#  DH = -42.6
# FNEMECHGEN: This reaction has had fne factor applied

entry(
    index = 102,
    label = "CH2O + CH3 <=> HCO + CH4",
    kinetics = PDepArrhenius(
                pressures = ([0.03947, 1.0, 10.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.688e+01, 'cm^3/(mol*s)'), n=3.360, Ea=(4312.0, 'cal/mol'), T0=(1, 'K')),  # at 0.03947 atm
            Arrhenius(A=(2.756e+01, 'cm^3/(mol*s)'), n=3.360, Ea=(4312.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(2.807e+01, 'cm^3/(mol*s)'), n=3.360, Ea=(4312.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
        ],
    ),
)

#  JP Senosiain, SJ Klippenstein, JA Miller, JPCA 110:6960 (2006).
#  DH = 10.3
# FNEMECHGEN: This reaction has had fne factor applied

entry(
    index = 239,
    label = "C2H5 + H <=> C2H6",
    kinetics = PDepArrhenius(
                pressures = ([0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.280e+20, 'cm^3/(mol*s)'), n=-5.010, Ea=(5057.0, 'cal/mol'), T0=(1, 'K')),  # at 0.001 atm
            Arrhenius(A=(1.650e+39, 'cm^3/(mol*s)'), n=-9.790, Ea=(18060.0, 'cal/mol'), T0=(1, 'K')),  # at 0.003 atm
            Arrhenius(A=(1.040e+41, 'cm^3/(mol*s)'), n=-10.130, Ea=(15110.0, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(6.260e+43, 'cm^3/(mol*s)'), n=-10.730, Ea=(13430.0, 'cal/mol'), T0=(1, 'K')),  # at 0.03 atm
            Arrhenius(A=(1.930e+46, 'cm^3/(mol*s)'), n=-11.180, Ea=(12210.0, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(9.870e+48, 'cm^3/(mol*s)'), n=-11.700, Ea=(12670.0, 'cal/mol'), T0=(1, 'K')),  # at 0.3 atm
            Arrhenius(A=(5.420e+51, 'cm^3/(mol*s)'), n=-12.200, Ea=(14210.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(1.620e+52, 'cm^3/(mol*s)'), n=-12.090, Ea=(14980.0, 'cal/mol'), T0=(1, 'K')),  # at 3.0 atm
            Arrhenius(A=(6.030e+51, 'cm^3/(mol*s)'), n=-11.710, Ea=(15800.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(4.180e+50, 'cm^3/(mol*s)'), n=-11.160, Ea=(16450.0, 'cal/mol'), T0=(1, 'K')),  # at 30.0 atm
            Arrhenius(A=(2.670e+48, 'cm^3/(mol*s)'), n=-10.320, Ea=(16830.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -81.6
# *****************************************************************************
#    C2H6 subset                                                              *
# *****************************************************************************
# Fuel Radicals: C2H5
# New Radicals Formed: CH3CH2OO, CH2CH2OH
# New Fuels: CH3CHO, c-CH2CH2O
# *** Fuel Decomposition


entry(
    index = 454,
    label = "CH3C(OH)CH <=> CH2CO + CH3",
    kinetics = PDepArrhenius(
                pressures = ([0.000987, 0.00987, 0.0987, 0.131, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
            Arrhenius(A=(6.130e+21, 's^-1'), n=-4.410, Ea=(23590.0, 'cal/mol'), T0=(1, 'K')),  # at 0.000987 atm
            Arrhenius(A=(3.100e+24, 's^-1'), n=-4.450, Ea=(30460.0, 'cal/mol'), T0=(1, 'K')),  # at 0.00987 atm
            Arrhenius(A=(1.610e+24, 's^-1'), n=-4.590, Ea=(27290.0, 'cal/mol'), T0=(1, 'K')),  # at 0.0987 atm
            Arrhenius(A=(3.860e+19, 's^-1'), n=-2.780, Ea=(29820.0, 'cal/mol'), T0=(1, 'K')),  # at 0.131 atm
            Arrhenius(A=(3.880e+45, 's^-1'), n=-10.250, Ea=(43340.0, 'cal/mol'), T0=(1, 'K')),  # at 0.987 atm
            Arrhenius(A=(1.170e+41, 's^-1'), n=-8.560, Ea=(44710.0, 'cal/mol'), T0=(1, 'K')),  # at 9.87 atm
            Arrhenius(A=(6.800e+31, 's^-1'), n=-5.550, Ea=(44620.0, 'cal/mol'), T0=(1, 'K')),  # at 98.7 atm
        ],
    ),
)


# DL Baulch, CT Bowman, CJ Cobos, RA Cox, T Just, et al., JPCRD 34:757 (2005).
# DH = -56.3



entry(
    index = 472,
    label = "HCCO + OH <=> CH2 + CO2",
    kinetics = PDepArrhenius(
                pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.020e+19, 'cm^3/(mol*s)'), n=-2.080, Ea=(44.0, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(1.400e+19, 'cm^3/(mol*s)'), n=-2.120, Ea=(88.0, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(7.110e+19, 'cm^3/(mol*s)'), n=-2.300, Ea=(824.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(1.790e+20, 'cm^3/(mol*s)'), n=-2.340, Ea=(2421.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(2.701e+02, 'cm^3/(mol*s)'), n=2.870, Ea=(-6214.1, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# SZ Xiong, Q Yao, ZR Li, XY Li, CF 161:885 (2014).
# DH = -103.8


entry(
    index = 487,
    label = "CH2CHOO <=> CO + CH3O",
    kinetics = PDepArrhenius(
                pressures = ([1.0, 3.16, 10.0, 31.6, 100.0], 'atm'),
        arrhenius = [

            Arrhenius(A=(3.830e+33, 's^-1'), n=-7.200, Ea=(35100.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(1.280e+79, 's^-1'), n=-19.610, Ea=(74870.0, 'cal/mol'), T0=(1, 'K')),  # at 3.16 atm
            Arrhenius(A=(4.070e+32, 's^-1'), n=-6.620, Ea=(37210.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(6.860e+44, 's^-1'), n=-10.040, Ea=(47030.0, 'cal/mol'), T0=(1, 'K')),  # at 31.6 atm
            Arrhenius(A=(2.665e+04, 's^-1'), n=1.330, Ea=(14197.8, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -86.5


entry(
    index = 509,
    label = "CH3 + C2H2 <=> CH3CHCH",
    kinetics = PDepArrhenius(
                pressures = ([ 0.0395, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [

            Arrhenius(A=(6.810e+48, 'cm^3/(mol*s)'), n=-12.270, Ea=(16642.0, 'cal/mol'), T0=(1, 'K')),  # at 0.0395 atm
            Arrhenius(A=(1.190e+44, 'cm^3/(mol*s)'), n=-10.190, Ea=(18728.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(6.020e+43, 'cm^3/(mol*s)'), n=-9.740, Ea=(20561.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(1.420e+42, 'cm^3/(mol*s)'), n=-8.910, Ea=(22235.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# CF Goldsmith, LB Harding, Y Georgievskii, JA Miller, SJ Klippenstein, JPCA 119:7766 (2015).
# DH = -56.2
# C2H2+HCO=C2H3+CO
# ## Missing Reaction


entry(
    index = 535,
    label = "OCCHO <=> HCO + CO",
    kinetics = PDepArrhenius(
                pressures = ([0.01, 0.1, 1.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.800e+12, 's^-1'), n=0.000, Ea=(8610.0, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(3.800e+13, 's^-1'), n=0.000, Ea=(8665.0, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(4.100e+14, 's^-1'), n=0.000, Ea=(8765.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(1.100e+14, 's^-1'), n=0.133, Ea=(10140.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# JA Miller - estimate
# DH = -62.8
# *****************************************************************************
#    OCHCHO subset                                                            *
# *****************************************************************************
# Fuel Radicals: OCCHO
# New Radicals Formed:
# New Fuels:
# *** Fuel Decomposition

entry(
    index = 590,
    label = "CH3CHCHO <=> CH2CHCHOH",
    kinetics = PDepArrhenius(
                pressures = ([0.000987, 0.00987, 0.0987, 0.987, 9.87, 98.7], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.120e+43, 's^-1'), n=-10.330, Ea=(41010.0, 'cal/mol'), T0=(1, 'K')),  # at 0.000987 atm
            Arrhenius(A=(3.130e-10, 's^-1'), n=4.870, Ea=(16270.0, 'cal/mol'), T0=(1, 'K')),  # at 0.00987 atm
            Arrhenius(A=(1.110e+14, 's^-1'), n=-1.820, Ea=(24810.0, 'cal/mol'), T0=(1, 'K')),  # at 0.0987 atm
            Arrhenius(A=(3.420e+08, 's^-1'), n=0.030, Ea=(16130.3, 'cal/mol'), T0=(1, 'K')),  # at 0.987 atm
            Arrhenius(A=(5.940e+23, 's^-1'), n=-3.690, Ea=(38040.0, 'cal/mol'), T0=(1, 'K')),  # at 9.87 atm
            Arrhenius(A=(3.510e+16, 's^-1'), n=-1.470, Ea=(35170.0, 'cal/mol'), T0=(1, 'K')),  # at 98.7 atm
        ],
    ),
)

# J Zador, JA Miller, PCI 35:181 (2015).
# DH = 11.3

entry(
    index = 610,
    label = "CH3CHCH2 + H <=> CH3CH2CH2",
    kinetics = PDepArrhenius(
                pressures = ([ 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [

            Arrhenius(A=(1.040e+49, 'cm^3/(mol*s)'), n=-11.500, Ea=(15359.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(6.200e+41, 'cm^3/(mol*s)'), n=-8.892, Ea=(14637.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(6.450e+31, 'cm^3/(mol*s)'), n=-5.851, Ea=(8178.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# JA Miller, SJ Klippenstein, JPCA 117:2718 (2013).
# DH = -34.8

entry(
    index = 662,
    label = "CH3CHCH2OOH <=> CH2CH2CH2OOH",
    kinetics = PDepArrhenius(
                 pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.240e-31, 's^-1'), n=12.726, Ea=(12862.0, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(2.790e-37, 's^-1'), n=13.523, Ea=(2976.0, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(3.480e+58, 's^-1'), n=-12.866, Ea=(51487.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(1.140e+36, 's^-1'), n=-6.503, Ea=(41002.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(1.200e-22, 's^-1'), n=9.661, Ea=(13329.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# CF Goldsmith, WH Green, SJ Klippenstein, JPCA 116:3325 (2012).
# DH = ??


entry(
    index = 741,
    label = "CH3CHCH2 + OH <=> CH3CHO + CH3",
    kinetics = PDepArrhenius(
                pressures = ([0.0013, 0.01, 0.013, 0.025, 0.1, 0.132, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.440e+07, 'cm^3/(mol*s)'), n=0.890, Ea=(1216.5, 'cal/mol'), T0=(1, 'K')),  # at 0.0013 atm
            Arrhenius(A=(1.870e+19, 'cm^3/(mol*s)'), n=-2.960, Ea=(4951.0, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(2.610e+15, 'cm^3/(mol*s)'), n=-1.670, Ea=(3823.0, 'cal/mol'), T0=(1, 'K')),  # at 0.013 atm
            Arrhenius(A=(3.310e+14, 'cm^3/(mol*s)'), n=-1.290, Ea=(3996.0, 'cal/mol'), T0=(1, 'K')),  # at 0.025 atm
            Arrhenius(A=(9.460e+14, 'cm^3/(mol*s)'), n=-1.300, Ea=(5272.0, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(1.610e+15, 'cm^3/(mol*s)'), n=-1.350, Ea=(5603.0, 'cal/mol'), T0=(1, 'K')),  # at 0.132 atm
            Arrhenius(A=(5.170e+16, 'cm^3/(mol*s)'), n=-1.670, Ea=(8264.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(5.130e+18, 'cm^3/(mol*s)'), n=-2.110, Ea=(12359.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(7.410e+19, 'cm^3/(mol*s)'), n=-2.290, Ea=(17262.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)

# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -8.8




# J Zador, AW Jasper, JA Miller, PCCP 11:11040 (2009).
# DH = -70.4
# *****************************************************************************
#     CH3CH2CHO subset                                                        *
#     CH3OCHCH2 subset                                                        *
#     CH2CHCH2OH subset                                                       *
#     CH3C(OH)CH2 subset                                                      *
#     CH3CHCHOH subset                                                        *
# *****************************************************************************
# Fuel Radicals: CH2CH2CHO, CH3CHCHO, CH3CH2CO
# Fuel Radicals: CH2OCHCH2, CH3OCCH2, CH3OCHCH
# Fuel Radicals: CHCHCH2OH, CH2CCH2OH, CH2CHCHOH, CH2CHCH2O
# Fuel Radicals: CH2C(OH)CH2, CH3C(O)CH2, CH3C(OH)CH
# Fuel Radicals: CH2CHCHOH, CH3CCHOH, CH3CHCOH, CH3CHCHO
# New Radicals Formed:
# New Fuels:
# *** Fuel + Radical



entry(
    index = 473,
    label = "HCCO + OH <=> CHOH + CO",
    kinetics = PDepArrhenius(
                pressures = ([0.01, 0.1, 1.0, 10.0, 100.0], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.770e+13, 'cm^3/(mol*s)'), n=0.090, Ea=(-20.0, 'cal/mol'), T0=(1, 'K')),  # at 0.01 atm
            Arrhenius(A=(2.770e+13, 'cm^3/(mol*s)'), n=0.090, Ea=(-20.0, 'cal/mol'), T0=(1, 'K')),  # at 0.1 atm
            Arrhenius(A=(2.770e+13, 'cm^3/(mol*s)'), n=0.090, Ea=(-20.0, 'cal/mol'), T0=(1, 'K')),  # at 1.0 atm
            Arrhenius(A=(4.340e+14, 'cm^3/(mol*s)'), n=-0.287, Ea=(354.0, 'cal/mol'), T0=(1, 'K')),  # at 10.0 atm
            Arrhenius(A=(3.950e+14, 'cm^3/(mol*s)'), n=-0.273, Ea=(384.0, 'cal/mol'), T0=(1, 'K')),  # at 100.0 atm
        ],
    ),
)
# SZ Xiong, Q Yao, ZR Li, XY Li, CF 161:885 (2014).
# DH = -51.8





