# Dataset-8-DROPBEAR-Acceleration-vs-Roller-Displacement


This data set consists of acceleration data measured from the Reproduction of Projectiles in Ballistic Environments for Advanced Research (DROPBEAR) experimental testbed with movable roller support as shown in Figure 1. This dataset was developed as an extension to Dataset-2 <a href="https://github.com/High-Rate-SHM-Working-Group/Dataset-2-DROPBEAR-Acceleration-vs-Roller-Displacement">here</a> with an emphasis on the generation of data in the quality and quantity needed to apply machine learning approaches.


DROPBEAR consists of a 51 x 6 x 350 mm beam with a single accelerometer (model 393B04 manufactured by PCB Piezotronics) mounted at the free edge of the beam was used. A video of the test along can be found <a href="https://www.youtube.com/watch?v=ZB6AUWgWyJU&ab_channel=ARTS-LabattheUniversityofSouthCarolinaARTS-LabattheUniversityofSouthCarolina">here</a>.

<p align="center">
<a href="https://www.youtube.com/watch?v=ZB6AUWgWyJU&ab_channel=ARTS-LabattheUniversityofSouthCarolinaARTS-LabattheUniversityofSouthCarolina"><img src="media/DROPBEAR.png" alt="Shock test impact testing" width="800"></a>  
</p>
<p align="center">
Figure 1: The Dynamic Reproduction of Projectiles in Ballistic Environments for Advanced Research (DROPBEAR) experimental testbed with key components annotated (click the image to view the video on YouTube). This image is released under a CC-BY-SA-4.0 license and citable as [DROPBEAR Testbed, Austin Downey, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Github].
</p>

The roller followed a predefined profile that ranged from 48 mm (closest to the fixity) to 175 mm as presented in the inset of Figure 2. The beam is self-excited by the roller's movements and therefore no extraneous inputs are required, however, this does require an initial input to the beam, which consists of a small roller movement, to initiate vibrations in the beam. In addition to this initial input, the test profile consists of six square wave inputs of increasing amplitude in addition to six sinusoidal inputs and six impulse inputs. For the cases of the square and impulse inputs, the actuator velocity was maximized to the extent allowed by the actuator and associated controller (250 mm/s). The measured vibration data is shown in figure 3.

<p align="center">
<img src="media/pin_locatoin_data.png" alt="drawing" width="600"/>
</p>
<p align="center">
Figure 2: Displacement of roller used in the generation of this dataset. 
</p>

The measured vibration data is shown in figure 3.  Data acquisition was performed using a 14-bit ADC (PXI-6133) for the linear transducer (SPS-L225-HALS manufactured by Honeywell) while acceleration data was acquired using a 24-bit IEPE ADC (NI-9234).

<p align="center">
<img src="media/acceleration_data.png" alt="drawing" width="600"/>
</p>
<p align="center">
Figure 3: Measured acceleration data for this data set. 
</p>

<p align="center">
<img src="media/DROPBEAR_Setup.png" alt="drawing" width="600"/>
</p>
<p align="center">
Figure 4: DROPBEAR test setup with displacement input and measured acceleration.
</p>




## Licensing and Citation

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Where applicable and legal, this work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa]. This license is not intended to supersede government license requirements. In good faith, all images within the repository are assumed to be licensed under a cc-by-sa [Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].
 

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Cite this data as: 

Alexander Vereen, Austin Downey, Jacob Dodson, Adriane G Moura “Dataset-8-dropbearacceleration-vs-roller-displacement,” Aug. 2023. [Online]. Available: https://github.com/High-Rate-SHM-Working-Group/Dataset-8-DROPBEAR-Acceleration-vs-Roller-Displacement

@Misc{Downey2021Dataset2Dropbear,  
  author = {Alexander Vereen and Austin Downey and Jacob Dodson and Adriane G Moura},  
  month  = aug,  
  title  = {Dataset-8-DROPBEAR-Acceleration-vs-Roller-Displacement},  
  year   = {2023},  
  groups = {High-Rate-SHM-Working-Group},  
  url    = {https://github.com/High-Rate-SHM-Working-Group/Dataset-8-DROPBEAR-Acceleration-vs-Roller-Displacement},  
}  


