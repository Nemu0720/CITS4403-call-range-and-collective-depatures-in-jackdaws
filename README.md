# CITS4403-call-range-and-collective-depatures-in-jackdaws
Agent-based modelling of vocal coordination and collective departures in jackdaws.
CITS4403: Jackdaw Calls and Collective Departures

Individual research project for CITS4403.

Status: Initial proposal for Checkpoint 2.

Research System and Motivation

This project investigates vocal interactions among jackdaws at communal winter roosts and their role in coordinating collective departures.

Dibnah et al. (2022) combined field recordings with experimental manipulation to show that jackdaws use vocalisations to coordinate mass departures.

The project will explore how individual responses to acoustic information can produce group-level coordination, connecting agent-based modelling with self-organisation and emergence.

Proposed Research Question

How does the effective range of vocal interaction affect the timing and synchrony of collective departures in a jackdaw-inspired agent-based model?

Proposed Modelling Approach

A simplified agent-based model will be implemented in Python.

* Agent : 
    Number of jackdaws: N.
    Call range: the area that bird's calls can reach.
    range growth: how quickly this area grows over time.
  
* Environment: Spatial environment.
    Jackdaws are placed on the 2D grid.
    Each jackdaw can hear calls and see other partner withn a set range.
    The hearing range and seeing range may be different.

* Interaction:
    Each jackdaws receives calls from nearby jackdaws within its hearing range.
    In model B , each jackdaws can also see nearby jackdaws that took off within its seeing range.
* Departure rules
      Moudle A:
        Each jackdaws receive calls from nearbys and take off when the current call level reaches its threshold.
      Moudle B:
        Use same spaces and calls from A. Each bird builds up its readiness from the call it receives over time.
        Jackdaws take off relative to environment changes or the nearby take-of  f jackdaws.


Planned Experiments and Analysis

*Aim
  We will test how call range affects depature time and how may birds leave together, with 2 possiable model.

* Call range
  Assume that stronger calling increases the area thad a bird's calls can reach.This area grow gradually from 8 to 24 of surrouding cells.
  4 conditions:
    8 cells.
    slow growth 8 to 24 cells.
    fast growth 8 to 24 cells.
    24 cells.

  *Measurements
      The time when half of birds left.
      How many birds left in certain time.
      Repeat each condition around 30 times with different random seeds.

  *Limitation
    The cell counts,grouth speeds and individual rules have not been measured for the study roost.
    Moudle explore what may happend under these assumptions.

    
Current Progress

* Project topic selected.
* GitHub repository established.
* Initial research question and modelling approach proposed.
* Model implementation and experiments are planned.

Reference

Dibnah, A. J., Herbert-Read, J. E., Boogert, N. J., McIvor, G. E., Jolles, J. W., & Thornton, A. (2022). Vocally mediated consensus decisions govern mass departures from jackdaw roosts. Current Biology, 32(10), R455–R456. https://doi.org/10.1016/j.cub.2022.04.032
