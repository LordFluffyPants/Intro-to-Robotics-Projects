''' HW2.6 data'''
'''  by David Conner CPSC 495 Spring 2016 '''

import numpy as np
from rotations import *

# Homework Hw2.6

#RESULTS: for pelvis to r_palm
#Chain is: r_palm -> r_hand -> r_arm_wrist_roll -> r_arm_wrist_yaw -> r_arm_elbow -> r_arm_shoulder_yaw -> r_arm_shoulder_roll -> r_arm_shoulder_pitch -> utorso -> waist -> pelvis
# plm-hnd-wr-wy-el-shy-shr-shp-tor-wst-pel
t_pel_wst = np.array([0.000, 0.000, 0.137])
q_pel_wst = np.array([1.000, 0.000, 0.000, -0.000]) # [w, (x,y,z)] form

t_wst_tor = np.array([0.000, 0.000, 0.000])
q_wst_tor= np.array([1.000, 0.000, 0.003, 0.000])# [w, (x,y,z)] form

t_tor_shp = np.array([0.000, -0.234, 0.165])
q_tor_shp = np.array([0.851, 0.000, -0.525, 0.000]) # [w, (x,y,z)] form

t_shp_shr = np.array([0.000, 0.000, 0.000])
q_shp_shr = np.array([0.960, -0.279, 0.000, 0.000])# [w, (x,y,z)] form

t_shr_shy = np.array([0.000, 0.000, 0.000])
q_shr_shy = np.array([0.842, 0.000, 0.000, 0.540])# [w, (x,y,z)] form

t_shy_el = np.array([0.030, 0.000, -0.246])
q_shy_el = np.array([0.863, 0.000, -0.506, 0.000])# [w, (x,y,z)] form

t_el_wy = np.array([-0.030, 0.000, -0.186])
q_el_wy = np.array([0.566, 0.000, 0.000, 0.824])# [w, (x,y,z)] form

t_wy_wr = np.array([0.000, 0.000, 0.000])
q_wy_wr = np.array([0.904, -0.428, 0.000, 0.000])# [w, (x,y,z)] form

t_wr_hnd = np.array([0.000, 0.000, 0.000])
q_wr_hnd = np.array([0.797, 0.000, 0.000, -0.605])# [w, (x,y,z)] form

t_hnd_plm = np.array([0.000, 0.000, -0.160])
q_hnd_plm = np.array([0.000, 0.707, 0.707, 0.000])# [w, (x,y,z)] form

Pel_To_Wst = Q2trans(t_pel_wst, q_pel_wst)
Wst_To_Tor = Q2trans(t_wst_tor, q_wst_tor)
Tor_To_Shp = Q2trans(t_tor_shp, q_tor_shp)
Shp_To_Shr = Q2trans(t_shp_shr, q_shp_shr)
Shr_To_Shy = Q2trans(t_shr_shy, q_shr_shy)
Shy_To_El = Q2trans(t_shy_el, q_shy_el)
El_To_Wy = Q2trans(t_el_wy, q_el_wy)
Wy_To_Wr = Q2trans(t_wy_wr, q_wy_wr)
Wr_To_Hnd = Q2trans(t_wr_hnd, q_wr_hnd)
Hnd_To_Plm = Q2trans(t_hnd_plm, q_hnd_plm)

Pel_To_Tor = np.dot(Pel_To_Wst, Wst_To_Tor)
Pel_To_Shp = np.dot(Pel_To_Tor, Tor_To_Shp)
Pel_To_Shr = np.dot(Pel_To_Shp, Shp_To_Shr)
Pel_To_Shy = np.dot(Pel_To_Shr, Shr_To_Shy)
Pel_To_El = np.dot(Pel_To_Shy, Shy_To_El)
Pel_To_Wy = np.dot(Pel_To_El, El_To_Wy)
Pel_To_Wr = np.dot(Pel_To_Wy, Wy_To_Wr)
Pel_To_Hnd = np.dot(Pel_To_Wr, Wr_To_Hnd)
Pel_To_Plm = np.dot(Pel_To_Hnd, Hnd_To_Plm)

print "Pelvis and Palm Matrix",Pel_To_Plm
Cyl = np.array([0.0, 0.0, 0.2, 1])
Pel_To_Cyl = np.dot(Pel_To_Plm, Cyl)
print"\n"
print "Cyl with respect to Pelvis",Pel_To_Cyl
