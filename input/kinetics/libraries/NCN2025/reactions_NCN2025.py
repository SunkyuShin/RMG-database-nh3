#!/usr/bin/env python
# encoding: utf-8

name = "NCN2025"
shortDesc = u"NCN2025"
longDesc = u"""

reaction index 1: 
Sebastian Hesse, Laila Nazari, Gernot Friedrichs
Investigation of the reactions NCN + CH3, NCN + OH, and CH3 + OH behind shock waves
Combustion and Flame

reaction index 2 and 3:
Applications in Energy and Combustion Science
Modeling Combustion Chemistry using C3MechV4.0: an extension to mixtures of hydrogen, ammonia, alkanes, and cycloalkanes


reaction index 4 and 5:
Journal of the Energy Institute
Improvement in modeling NH3/CH4 combustion based on the effects of the H-abstraction reactions and disproportionation reactions

reaction index 6:
Combustion and Flame
Applications of hydrazine for the study of NH2 kinetics-II: Self-reaction of NH2 radicals


7-12 : Green group calculation
13-14: Klippenstein et al. Theory and modeling of relevance to prompt-NO formation at high pressure

"""



entry(
    index = 1,
    label = "NCN + CH3 <=> CH2NH + CN",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.44e+19, 'cm^3/(mol*s)'),
        n = -1.76,
        Ea = (3632.0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"",
    longDesc = u"""
T
ΔH = -88.6 kcal/mol.
""",
)



entry(
    index = 2,
    label = "H + CH2 <=> CH3",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (6.0e+14, 'cm^3/(mol*s)'),
            n = 0.0,
            Ea = (0.0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.04e+26, 'cm^6/(mol^2*s)'),
            n = -2.76,
            Ea = (1600.0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.562,
        T3 = (91.0, 'K'),
        T1 = (5836.0, 'K'),
        T2 = (8552.0, 'K'),

    efficiencies = {
        "[Ar]": 0.7,
        "[C-]#[O+]": 1.5,
        "O=C=O": 2.0,
        "C": 2.0,
        "[H][H]": 2.0,
        "CC": 3.0,
        "O": 6.0,
    },
    ),
)

entry(
    index = 3,
    label = "CH + H2 <=> CH3",
    degeneracy = 1,
    elementary_high_p = True,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.97e+12, 'cm^3/(mol*s)'),
            n = 0.43,
            Ea = (-370.0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.82e+25, 'cm^6/(mol^2*s)'),
            n = -2.8,
            Ea = (590.0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.578,
        T3 = (122.0, 'K'),
        T1 = (2535.0, 'K'),
        T2 = (9365.0, 'K'),

       efficiencies = {
        "[Ar]": 0.7,
        "[C-]#[O+]": 1.5,
        "O=C=O": 2.0,
        "C": 2.0,
        "[H][H]": 2.0,
        "CC": 3.0,
        "O": 6.0,
    },
    ),
)

entry(
    index = 4,
    label = "CH2O + NH2 <=> HCO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+2, 'cm^3/(mol*s)'),
        n = 3.0,
        Ea = (3770, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"",
    longDesc = u"""
T
ΔH = .
""",
)


entry(
    index = 5,
    label = "HCO + NH2 <=> CO + NH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.826e+13, 'cm^3/(mol*s)'),
        n = 0.41,
        Ea = (-215.572, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    shortDesc = u"",
    longDesc = u"""
T
ΔH = .
""",
)


entry(
    index=6,
    label="NH2 + NH2 <=> NH3 + NH",
    degeneracy=1,
    kinetics=Arrhenius(A=(14.7e+00, 'cm^3/(mol*s)'), n=0, Ea=(19200, 'cal/mol'),
                       T0=(1, 'K'), Tmin=(1290, 'K'), Tmax=(2860, 'K')),
    shortDesc=u"""[Rault2026]""",
    longDesc = u"""
T
ΔH = .
""",
)




entry(
    index=7,
    label="CH2NH <=> CHNH2",

    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(1.28E+13, 's^-1'), n=-1.40, Ea=(71530, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.37E+14, 's^-1'), n=-1.40, Ea=(73350, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(3.47E+15, 's^-1'), n=-1.50, Ea=(75430, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.13E+17, 's^-1'), n=-1.64, Ea=(77620, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.64E+17, 's^-1'), n=-1.47, Ea=(79280, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc=u"""Yujie""",
    longDesc=u"""
    MRCI(+Q)/CBS//CASPT2(12,11)/cc-pVTZ
    """,
)

entry(
    index=8,
    label="CH2NH <=> H2CN + H",

    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(5.18E+21, 's^-1'), n=-3.32, Ea=(87740, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(3.61E+31, 's^-1'), n=-5.86, Ea=(92140, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.37E+27, 's^-1'), n=-4.33, Ea=(90810, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.42E+21, 's^-1'), n=-2.25, Ea=(88940, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(3.92E+16, 's^-1'), n=-0.71, Ea=(87870, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc=u"""Yujie""",
    longDesc=u"""
    MRCI(+Q)/CBS//CASPT2(12,11)/cc-pVTZ
    """,
)

entry(
    index=9,
    label="CH2NH <=> HNC + H2",

    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(7.11E+28, 's^-1'), n=-5.38, Ea=(87690, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(5.55E+28, 's^-1'), n=-5.11, Ea=(88550, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.80E+24, 's^-1'), n=-3.61, Ea=(87630, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(9.40E+18, 's^-1'), n=-1.77, Ea=(86240, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.11E+14, 's^-1'), n=-0.22, Ea=(85140, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc=u"""Yujie""",
    longDesc=u"""
    MRCI(+Q)/CBS//CASPT2(12,11)/cc-pVTZ
    """,
)

entry(
    index=10,
    label="HCN <=> HNC",

    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(2.83E+14, 's^-1'), n=-2.19, Ea=(38070, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.48E+17, 's^-1'), n=-2.74, Ea=(40230, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.02E+18, 's^-1'), n=-2.70, Ea=(41330, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(6.67E+18, 's^-1'), n=-2.55, Ea=(42290, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.46E+18, 's^-1'), n=-2.11, Ea=(42880, 'cal/mol'), T0=(1, 'K'), Tmin=(400, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc=u"""Yujie""",
    longDesc=u"""
    CCSD(T)/CBS + T/Q correction
    """,
)

entry(
    index=12,
    label="H2CN <=> HCN + H",

    degeneracy=1,
    kinetics=PDepArrhenius(
        pressures=([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius=[
            Arrhenius(A=(2.33E+26, 's^-1'), n=-5.57, Ea=(32680, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.34E+26, 's^-1'), n=-5.18, Ea=(32920, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(5.78E+25, 's^-1'), n=-4.77, Ea=(33180, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(2.05E+25, 's^-1'), n=-4.32, Ea=(33490, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
            Arrhenius(A=(1.01E+25, 's^-1'), n=-3.93, Ea=(34010, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2000, 'K')),
        ],
    ),
    shortDesc=u"""Yujie""",
    longDesc=u"""
    MRCI(+Q)/CBS//CASPT2(11,10)/cc-pVTZ
    """,
)




entry(
    index=13,
    label="H + NCN <=> HNCN",
    
    degeneracy=1,
    kinetics=PDepArrhenius(
    pressures=([0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100], 'atm'),
    arrhenius=[
        Arrhenius(A=(3.9E+23, 'cm^3/(mol*s)'), n=-4.340, Ea=(5347, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(3.3E+25, 'cm^3/(mol*s)'), n=-4.710, Ea=(4102, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(5.6E+27, 'cm^3/(mol*s)'), n=-5.130, Ea=(3741, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.7E+29, 'cm^3/(mol*s)'), n=-5.360, Ea=(3947, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.5E+30, 'cm^3/(mol*s)'), n=-5.430, Ea=(4415, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(2.6E+30, 'cm^3/(mol*s)'), n=-5.340, Ea=(4870, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.2E+30, 'cm^3/(mol*s)'), n=-5.090, Ea=(5275, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.9E+29, 'cm^3/(mol*s)'), n=-4.720, Ea=(5476, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(5.1E+27, 'cm^3/(mol*s)'), n=-4.150, Ea=(5370, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        ],
    ),
    shortDesc=u"""Klippenstein""",
    longDesc = 
    u"""
    ( )
    """,
)


entry(
    index=14,
    label="CH + N2 <=> HNCN",
    
    degeneracy=1,
    kinetics=PDepArrhenius(
    pressures=([0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100], 'atm'),
    arrhenius=[
        Arrhenius(A=(6.0E+23, 'cm^3/(mol*s)'), n=-4.410, Ea=(14410, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(7.3E+23, 'cm^3/(mol*s)'), n=-4.300, Ea=(14760, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(7.3E+23, 'cm^3/(mol*s)'), n=-4.170, Ea=(15200, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(4.8E+23, 'cm^3/(mol*s)'), n=-4.000, Ea=(15570, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.4E+23, 'cm^3/(mol*s)'), n=-3.740, Ea=(15820, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.7E+22, 'cm^3/(mol*s)'), n=-3.380, Ea=(15840, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(6.8E+20, 'cm^3/(mol*s)'), n=-2.900, Ea=(15690, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(1.8E+19, 'cm^3/(mol*s)'), n=-2.370, Ea=(15430, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        Arrhenius(A=(3.1E+17, 'cm^3/(mol*s)'), n=-1.780, Ea=(15240, 'cal/mol'), T0=(1, 'K'), Tmin=(500, 'K'), Tmax=(2500, 'K')),
        ],
    ),
    shortDesc=u"""Klippenstein""",
    longDesc = 
    u"""
    (  )
    """,
)