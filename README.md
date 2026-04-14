# manim-blackhole-lensing

Educational Manim animation illustrating gravitational lensing around a black hole.  
Includes event horizon, photon sphere, and approximate ray bending using a simplified physics model.  
⚠️ Note: This is **not** a full general relativity solver — it’s a pedagogical visualization.

---

## About

This repository only contains the **code snippet** for the animation.  
It is meant as an illustrative example of how Manim can be used to visualize gravitational lensing.  
I have not packaged it as a reproducible repo with environment setup, requirements, or documentation.  
If you want to run it, you’ll need to install [Manim](https://docs.manim.community/) and `numpy` yourself.

  
[▶ Watch the full animation](https://github.com/user-attachments/assets/9d486d9a-7b07-483b-9753-01e934b2d7f3)



## Scientific Background

Gravitational lensing is a prediction of Einstein’s General Relativity: massive objects curve spacetime, bending the paths of photons. Around black holes, this produces striking phenomena such as photon spheres, black hole shadows, and multiple images of background sources.

Recent research highlights several key aspects:

- **Dynamic Black Hole Shadows**  
  *He et al., "Dynamic shadows and lensing rings of Vaidya black holes," Phys. Rev. D (2026)*  
  Shows that black hole shadows evolve during accretion, with lensing rings forming and stabilizing as the accretion rate changes.

- **Photon Sphere and Light Echoes**  
  *Gao, "Photon spheres and echoes in black hole spacetimes," Class. Quantum Grav. (2025)*  
  Demonstrates that photons orbiting near the photon sphere can escape with time delays, producing observable echoes in light curves.

- **Strong-Field Lensing Equations**  
  *Araújo Filho et al., "Analytical deflection angles in strong gravitational lensing," Eur. Phys. J. C (2025)*  
  Provides exact deflection angle formulas for null geodesics in Schwarzschild spacetime, predicting multiple images and Einstein rings.

- **Magnetized Black Holes**  
  *Zhou et al., "Photon rings in Schwarzschild–Melvin spacetime," Phys. Rev. D (2024)*  
  Studies how external magnetic fields modify photon trajectories and lensing structures.

- **Machine Learning Approaches**  
  *Sun et al., "GravLensX: Neural network simulation of null geodesics," Astrophys. J. (2025)*  
  Introduces deep learning methods to efficiently simulate geodesics and lensing, reducing computational cost compared to traditional ray-tracing.

---

### Relation to This Visualization

The Manim animation here:
- Illustrates the **event horizon** and **photon sphere** correctly.  
- Uses a simplified bending approximation (\~1/r^5 force term) to show rays being trapped or escaping.  
- Captures the **qualitative behavior** of gravitational lensing, but does not solve the full geodesic equations.  

⚠️ **Disclaimer:** This code is an **educational visualization**, not a research-grade simulation. For quantitative accuracy, consult the cited papers above.

