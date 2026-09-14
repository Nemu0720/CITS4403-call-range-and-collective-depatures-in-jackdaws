# CITS4403-jackdaw-calls
Agent-based modelling of vocal coordination and collective departures in jackdaws.
CITS4403: Jackdaw Calls and Collective Departures

Individual research project for CITS4403.

Status: Initial proposal for Checkpoint 1.

Research System and Motivation

This project investigates vocal interactions among jackdaws at communal winter roosts and their role in coordinating collective departures.

Dibnah et al. (2022) combined field recordings with experimental manipulation to show that jackdaws use vocalisations to coordinate mass departures.

The project will explore how individual responses to acoustic information can produce group-level coordination, connecting agent-based modelling with self-organisation and emergence.

Proposed Research Question

How does the effective range of vocal interaction affect the timing and synchrony of collective departures in a jackdaw-inspired agent-based model?

Proposed Modelling Approach

A simplified agent-based model will be implemented in Python.

* Each agent represents one jackdaw.
* Agents occupy positions within a two-dimensional roost.
* Each agent has an individual readiness to depart and a current calling and departure state.
* Agents receive calls from other agents within an adjustable interaction radius.
* Calling and departure decisions depend on individual readiness and received acoustic information.

The decision rules and parameter values will be documented as modelling assumptions. Conclusions will be limited to the conditions explored in the simulations.

Planned Experiments and Analysis

* Vary the vocal interaction radius while keeping flock size, roost area and other parameter distributions consistent.
* Include a baseline in which agents do not respond to other agents’ calls.
* Repeat simulations using multiple random seeds.
* Compare the cumulative proportion of departed agents over time.
* Assess departure synchrony using the spread of departure times, alongside the proportion that departs within the simulation period.
* Visualise individual states and group-level time series.

Current Progress

* Project topic selected.
* GitHub repository established.
* Initial research question and modelling approach proposed.
* Model implementation and experiments are planned.

Reference

Dibnah, A. J., Herbert-Read, J. E., Boogert, N. J., McIvor, G. E., Jolles, J. W., & Thornton, A. (2022). Vocally mediated consensus decisions govern mass departures from jackdaw roosts. Current Biology, 32(10), R455–R456. https://doi.org/10.1016/j.cub.2022.04.032
