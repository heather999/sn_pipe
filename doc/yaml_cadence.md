SN parameters:  
   &nbsp; X1: -2.0        **# stretch**  
   &nbsp; Color: 0.2   **#color**  
Observations:   
   &nbsp; filename: ../flatiron/maf_local/sims_maf_contrib/tutorials/baseline2018a.db  **# Name of db obs file (full path)** 
   &nbsp; fieldtype: DD **#DD or WFD**  
   &nbsp; coadd: True **# this is the coaddition per night**  
   &nbsp; season: -1 **#season to simulate (-1 = all seasons)**  
   &nbsp; bands: 'riz' **#bands to consider**  
   &nbsp; SNR: [25., 25., 30., 35.] **#DDF SNR cut to estimate sum(Li^2)**  
   &nbsp; #SNR:  [30., 40., 30., 20.] **#WFD SNR cut to estimate sum(Li^2)**  
   &nbsp; mag_range: [23., 27.5] **#DDF mag range**  
   &nbsp; #mag_range: [21., 25.5] **#WFD mag range**    
   &nbsp; dt_range: [0.5, 25.] **# DDF dt range**  
   &nbsp; #dt_range: [0.5, 30.]  **# WFD dt range**    
Pixelisation:  
    &nbsp; nside: 64  
Li file : ['SN_MAF/Reference_Files/Li_SNSim_-2.0_0.2.npy','SN_MAF/Reference_Files/Li_SNCosmo_-2.0_0.2.npy']  **# Flux template files**  
Mag_to_flux file : ['SN_MAF/Reference_Files/Mag_to_Flux_SNSim.npy','SN_MAF/Reference_Files/Mag_to_Flux_SNCosmo.npy']  **#mag to flux files**  
names_ref: ['SNSim','SNCosmo']  **# reference names - should fit the two previous items**  
Metric: SN_Cadence_Metric **#name of the metric**  