from manim import *
import numpy as np

class BlackHole(Scene):
    def construct(self):
        # 1. SETUP DARK SPACE
        self.camera.background_color = "#020202"
        rs = 1.0  # Schwarzschild Radius
        
        # 2. BLACK HOLE ENTITIES
        singularity = Dot(color=BLACK, radius=0.01)
        event_horizon = Circle(radius=rs, color=BLACK, fill_opacity=1)
        photon_sphere = Circle(radius=1.5*rs, color=BLUE_E, stroke_width=1, stroke_opacity=0.3)
        
        # Accretion Disk (Glow)
        disk = Annulus(inner_radius=2*rs, outer_radius=4*rs, color=ORANGE, fill_opacity=0.2)
        
        self.add(disk, photon_sphere, event_horizon, singularity)

        # 3. RAY TRACING (Physics Engine)
        def get_ray_path(impact_parameter):
            """Simulates the curved path of a light ray near a mass."""
            path_points = []
            pos = np.array([-7.0, impact_parameter, 0])
            vel = np.array([1.0, 0, 0])
            dt = 0.05
            h2 = impact_parameter**2 # Conserved angular momentum squared
            
            for _ in range(300):
                r = np.linalg.norm(pos)
                if r < rs * 1.05: break # Ray trapped by horizon
                
                # Relativistic Correction Force (1/r^5)
                accel = -(1.5) * h2 * pos / (r**5)
                vel += accel * dt
                pos += vel * dt
                path_points.append(pos.copy())
                if r > 10: break # Escaped to infinity
            return path_points

        # 4. ANIMATE LIGHT BENDING
        # We fire multiple rays to show lensing
        rays = VGroup()
        for b in np.linspace(-3.5, 3.5, 25):
            points = get_ray_path(b)
            if len(points) > 1:
                # Color rays based on if they escape or fall in
                color = RED if np.linalg.norm(points[-1]) < 2 else WHITE
                ray = VMobject(color=color, stroke_width=1.5, stroke_opacity=0.6)
                ray.set_points_as_corners(points)
                rays.add(ray)

        # Labels
        labels = VGroup(
            Text("EVENT HORIZON", color=GREY).scale(0.3).next_to(event_horizon, UP),
            Text("PHOTON SPHERE", color=BLUE).scale(0.3).next_to(photon_sphere, DOWN),
            Text("GRAVITATIONAL LENSING", color=WHITE).scale(0.5).to_edge(UP)
        )

        self.play(Write(labels))
        self.play(Create(rays, lag_ratio=0.1), run_time=5)
        self.wait(2)

%manim -v WARNING -ql BlackHole
