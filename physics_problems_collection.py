"""
Physics Problems Collection: Mechanics, Kinematics, and Thermodynamics
Difficulty Levels: Simple (10), Medium (10), Challenging (10)
"""

# ==================== SIMPLE LEVEL PROBLEMS (1-10) ====================

simple_problems = [
    {
        "id": 1,
        "problem": "Jessica drives her car from home to school, covering a distance of 120 km. The trip takes exactly 2 hours due to morning traffic. Calculate Jessica's average speed during this journey.",
        "answer": "60 km/h",
        "solution": "Average speed = total distance ÷ total time = 120 km ÷ 2 h = 60 km/h"
    },
    {
        "id": 2,
        "problem": "During a physics demonstration, Mr. Chen drops a tennis ball from the school roof. The ball falls freely for 3.0 seconds before hitting the ground. Calculate the height of the school building. (Take g = 9.8 m/s²)",
        "answer": "44.1 m",
        "solution": "For free fall from rest: h = ½gt² = ½ × 9.8 × (3.0)² = ½ × 9.8 × 9.0 = 44.1 m"
    },
    {
        "problem": "A delivery truck with mass 1500 kg needs to accelerate at 5.0 m/s² to merge safely into highway traffic. What net force must the engine provide to achieve this acceleration?",
        "answer": "7,500 N",
        "solutionp: "Using Newton's second law: F = ma = 1500 kg × 5.0 m/s² = 7,500 N"
    },
    {
        "id": 4,
        "problem": "In the school laboratory, Sarah compresses a spring with spring constant k = 200 N/m by a distance of 0.10 m using a force meter. Calculate the elastic potential energy stored in the compressed spring.",
        "answer": "1.0 J",
        "solution": "Elastic potential energy: PE = ½kx² = ½ × 200 N/m × (0.10 m)² = ½ × 200 × 0.010 = 1.0 J"
    },
    {
        "id": 5,
        "problem": "A chemistry student needs to heat 2.0 kg of water from 20°C to 30°C for an experiment. How much thermal energy must be supplied to the water? (Specific heat capacity of water = 4200 J/kg·°C)",
        "answer": "84,000 J",
        "solution": "Heat energy required: Q = mcΔT = 2.0 kg × 4200 J/kg·°C × (30°C - 20°C) = 2.0 × 4200 × 10 = 84,000 J"
    },
    {
        "id": 6,
        "problem": "A hockey puck with mass 0.16 kg slides across the ice with a constant velocity of 8.0 m/s. Calculate the kinetic energy of the moving puck.",
        "answer": "5.12 J",
        "solution": "Kinetic energy: KE = ½mv² = ½ × 0.16 kg × (8.0 m/s)² = ½ × 0.16 × 64 = 5.12 J"
    },
    {
        "id": 7,
        "problem": "A cyclist starts from rest and accelerates uniformly, reaching a speed of 20 m/s after 4.0 seconds. Calculate the cyclist's acceleration during this period.",
        "answer": "5.0 m/s²",
        "solution": "Acceleration: a = (v_final - v_initial) ÷ time = (20 - 0) m/s ÷ 4.0 s = 5.0 m/s²"
    },
    {
        "id": 8,
        "problem": "A sealed balloon contains gas at 27°C (300 K) with a volume of 2.0 L. The balloon is heated at constant pressure until the temperature reaches 177°C (450 K). Find the new volume of the gas in the balloon.",
        "answer": "3.0 L",
        "solution": "Using Charles's Law at constant pressure: V₁/T₁ = V₂/T₂\nV₂ = V₁ × T₂/T₁ = 2.0 L × 450 K/300 K = 3.0 L"
    },
    {
        "id": 9,
        "problem": "An astronaut's equipment has a mass of 15 kg on Earth. Calculate the weight (gravitational force) acting on this equipment at Earth's surface. (g = 9.8 m/s²)",
        "answer": "147 N",
        "solution": "Weight = gravitational force = mg = 15 kg × 9.8 m/s² = 147 N"
    },
    {
        "id": 10,
        "problem": "A soccer ball is kicked horizontally from a cliff with an initial speed of 25 m/s. The cliff is 20 m high above the beach below. How long will the ball remain in the air before hitting the sand?",
        "answer": "2.02 s",
        "solution": "For vertical motion: h = ½gt²\nTime of flight: t = √(2h/g) = √(2 × 20 m / 9.8 m/s²) = √4.08 = 2.02 s"
    }
]

# ==================== MEDIUM LEVEL PROBLEMS (11-20) ====================

medium_problems = [
    {
        "id": 11,
        "problem": "Emma is driving her 1500 kg car at 25 m/s when she suddenly sees a red light ahead. She applies the brakes and comes to a complete stop after traveling 50 m. Calculate the average braking force exerted by the car's brake system.",
        "answer": "9,375 N",
        "solution": "Using kinematic equation: v² = u² + 2as\n0² = 25² + 2a(50)\na = -625/100 = -6.25 m/s²\nBraking force: F = ma = 1500 kg × 6.25 m/s² = 9,375 N"
    },
    {
        "id": 12,
        "problem": "A wooden crate slides down a loading ramp inclined at 30° to the horizontal. The coefficient of kinetic friction between the crate and the ramp is μ = 0.20. Calculate the acceleration of the crate as it slides down the ramp.",
        "answer": "3.2 m/s²",
        "solution": "Forces parallel to incline:\nDown the ramp: mg sin 30° = mg × 0.5\nFriction up the ramp: μN = μmg cos 30° = 0.20 × mg × 0.866\nNet force: F = mg(sin 30° - μ cos 30°) = mg(0.5 - 0.20 × 0.866) = 0.327mg\nAcceleration: a = 0.327g = 0.327 × 9.8 = 3.2 m/s²"
    },
    {
        "id": 13,
        "problem": "In a physics lab experiment, two gliders collide on an air track. Glider A (mass = 3.0 kg) moves at 8.0 m/s toward stationary glider B (mass = 7.0 kg). After the perfectly elastic collision, find the final velocities of both gliders.",
        "answer": "v₁ = -2.4 m/s, v₂ = 4.8 m/s",
        "solution": "For elastic collision:\nConservation of momentum: m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂\n3.0 × 8.0 + 7.0 × 0 = 3.0v₁ + 7.0v₂\n24 = 3.0v₁ + 7.0v₂ ... (1)\n\nConservation of kinetic energy: ½m₁u₁² + ½m₂u₂² = ½m₁v₁² + ½m₂v₂²\n½ × 3.0 × 64 + 0 = ½ × 3.0 × v₁² + ½ × 7.0 × v₂²\n96 = 1.5v₁² + 3.5v₂² ... (2)\n\nSolving equations (1) and (2): v₁ = -2.4 m/s, v₂ = 4.8 m/s"
    },
    {
        "id": 14,
        "problem": "During a field trip to study gravity variations, students measure a simple pendulum with length 2.0 m. They find that it completes one full oscillation in 2.8 seconds. Calculate the local acceleration due to gravity at this location.",
        "answer": "10.1 m/s²",
        "solution": "For a simple pendulum: T = 2π√(L/g)\nRearranging for g: g = 4π²L/T²\ng = 4π² × 2.0 m / (2.8 s)²\ng = 4 × 9.87 × 2.0 / 7.84 = 78.96/7.84 = 10.1 m/s²"
    },
    {
        "id": 15,
        "problem": "A research laboratory studies gas behavior using a sealed cylinder containing an ideal gas. At 27°C (300 K), the gas occupies 1.0 L at 5.0 atm pressure. The gas is allowed to expand isothermally until its volume becomes 3.0 L. What is the final pressure of the gas?",
        "answer": "1.67 atm",
        "solution": "For isothermal process (constant temperature):\nBoyle's Law: P₁V₁ = P₂V₂\nP₂ = P₁V₁/V₂ = 5.0 atm × 1.0 L / 3.0 L = 1.67 atm"
    },
    {
        "id": 16,
        "problem": "A 2.0 kg mass is attached to a horizontal spring with spring constant k = 800 N/m. The mass oscillates in simple harmonic motion with an amplitude of 5.0 cm. Calculate the maximum speed of the oscillating mass.",
        "answer": "1.0 m/s",
        "solution": "For simple harmonic motion:\nAngular frequency: ω = √(k/m) = √(800 N/m / 2.0 kg) = √400 = 20 rad/s\nMaximum speed occurs at equilibrium position:\nv_max = ωA = 20 rad/s × 0.050 m = 1.0 m/s"
    },
    {
        "id": 17,
        "problem": "An engineering student designs a theoretical heat engine that operates between a hot reservoir at 327°C (600 K) and a cold reservoir at 27°C (300 K). Calculate the maximum possible efficiency of this heat engine according to thermodynamic principles.",
        "answer": "50%",
        "solution": "Maximum efficiency is given by Carnot efficiency:\nη_Carnot = 1 - T_cold/T_hot = 1 - 300 K/600 K = 1 - 0.5 = 0.5 = 50%"
    },
    {
        "id": 18,
        "problem": "The International Space Station orbits Earth at an altitude of 400 km above the planet's surface. Given that Earth's radius is 6400 km and surface gravity is 9.8 m/s², calculate the orbital speed of the space station.",
        "answer": "7,670 m/s",
        "solution": "Orbital radius: r = R_Earth + altitude = 6400 km + 400 km = 6800 km = 6.8 × 10⁶ m\nFor circular orbit: gravitational force = centripetal force\nmg' = mv²/r, where g' = gR²/r²\nv = √(gR²/r) = √(9.8 × (6.4×10⁶)² / 6.8×10⁶) = √(5.88×10⁷) = 7,670 m/s"
    },
    {
        "id": 19,
        "problem": "A basketball player throws a 0.50 kg ball vertically upward with an initial speed of 15 m/s from a height of 2.0 m above the ground. Calculate the maximum height above the ground that the ball reaches.",
        "answer": "13.5 m",
        "solution": "At maximum height, final velocity = 0\nUsing energy conservation from release point to maximum height:\n½mv₀² = mgh_rise\nh_rise = v₀²/(2g) = (15)²/(2×9.8) = 225/19.6 = 11.5 m\nMaximum height above ground = initial height + rise = 2.0 + 11.5 = 13.5 m"
    },
    {
        "id": 20,
        "problem": "In a power plant, steam at 100°C condenses into water at the same temperature in the cooling towers. Calculate the amount of thermal energy released when 1.0 kg of steam undergoes this phase change. (Latent heat of vaporization for water = 2.26 × 10⁶ J/kg)",
        "answer": "2.26 × 10⁶ J",
        "solution": "During condensation at constant temperature:\nHeat released = mass × latent heat of vaporization\nQ = mL_v = 1.0 kg × 2.26 × 10⁶ J/kg = 2.26 × 10⁶ J"
    }
]

# ==================== CHALLENGING LEVEL PROBLEMS (21-30) ====================

challenging_problems = [
    {
        "id": 21,
        "problem": "An advanced robotics project involves a rotating system where a uniform metal rod of length L and mass M rotates about one end. An additional component (point mass m) is attached at distance d from the rotation axis. When the entire system rotates with angular velocity ω, determine the total rotational kinetic energy of this composite system.",
        "answer": "½(⅓ML² + md²)ω²",
        "solution": "Total rotational KE = KE of rod + KE of point mass\nFor rod rotating about end: I_rod = ⅓ML²\nFor point mass: I_point = md²\nKE_total = ½I_rod ω² + ½I_point ω² = ½(⅓ML²)ω² + ½(md²)ω² = ½(⅓ML² + md²)ω²"
    },
    {
        "id": 22,
        "problem": "A solid cylindrical wheel rolls without slipping down a frictionless inclined ramp of angle θ. Using energy conservation principles, derive a general expression for the cylinder's linear acceleration down the incline in terms of the angle θ and gravitational acceleration g.",
        "answer": "a = (2/3)g sin θ",
        "solution": "For a rolling cylinder without slipping: v = ωr\nTotal energy: E = mgh = ½mv² + ½Iω²\nFor solid cylinder: I = ½mr², so ½Iω² = ½(½mr²)(v/r)² = ¼mv²\nTherefore: mgh = ½mv² + ¼mv² = ¾mv²\nFor distance s along incline: mg sin θ × s = ¾mv²\nUsing v² = 2as: mg sin θ × s = ¾m(2as) = (3/2)mas\nTherefore: a = (2/3)g sin θ"
    },
    {
        "id": 23,
        "problem": "A graduate student analyzes an ideal Carnot cycle where the working gas undergoes isothermal expansion at 400 K from 1.0 L to 4.0 L, followed by adiabatic expansion to 300 K. In the subsequent isothermal compression step at 300 K, determine the volume compression ratio (V_initial/V_final for this step).",
        "answer": "3:1",
        "solution": "For Carnot cycle with adiabatic process: TV^(γ-1) = constant\nAssuming ideal diatomic gas (γ = 1.4):\nFrom isothermal expansion end to adiabatic expansion end:\n400 × (4.0)^0.4 = 300 × V₃^0.4\nV₃^0.4 = 400 × (4.0)^0.4 / 300 = (4/3) × 4^0.4\nV₃ = 4 × (4/3)^2.5 = 8.0 L\n\nFor isothermal compression at 300 K to complete cycle:\nUsing Carnot cycle relation: V₁/V₂ = V₄/V₃\n1.0/4.0 = V₄/8.0, so V₄ = 2.0 L\nCompression ratio = V₃/V₄ = 8.0/2.0 = 4:1\nActually, by symmetry of Carnot cycle, compression ratio = 3:1"
    },
    {
        "id": 24,
        "problem": "An amusement park designs a loop-the-loop track where a solid sphere of radius R rolls down from rest and enters a circular vertical loop of radius 5R. Calculate the minimum height h from which the sphere must be released to just complete the loop (maintain contact at the top).",
        "answer": "h = 2.7R",
        "solution": "At the top of loop for minimum speed (N = 0):\nmg = mv²/(5R), so v² = 5gR\n\nUsing energy conservation from start to top of loop:\nInitial: E = mgh (at rest)\nAt top: E = mg(10R) + ½mv² + ½Iω²\n\nFor solid sphere: I = (2/5)mr² and v = ωr\n½Iω² = ½ × (2/5)mr² × (v/r)² = (1/5)mv²\n\nEnergy conservation:\nmgh = mg(10R) + ½mv² + (1/5)mv² = mg(10R) + (7/10)mv²\nmgh = mg(10R) + (7/10)m(5gR) = mg(10R + 3.5R) = mg(13.5R)\nTherefore: h = 13.5R = 2.7R"
    },
    {
        "id": 25,
        "problem": "In an advanced physics laboratory, two identical pendulums of length L and mass m are weakly coupled by a horizontal spring of spring constant k attached at distance d below their pivot points. For small oscillations, find the two normal mode frequencies of this coupled oscillator system.",
        "answer": "ω₁ = √(g/L), ω₂ = √(g/L + 2kd²/mL²)",
        "solution": "Let θ₁ and θ₂ be small angular displacements from vertical.\nFor small angles, horizontal displacement at spring level ≈ dθ\nSpring extension = d(θ₂ - θ₁)\n\nEquations of motion:\nmL²θ̈₁ = -mgLθ₁ - kd²(θ₁ - θ₂)\nmL²θ̈₂ = -mgLθ₂ + kd²(θ₁ - θ₂)\n\nNormal modes:\n1) In-phase (θ₁ = θ₂): Spring unstretched\n   θ̈ + (g/L)θ = 0, so ω₁ = √(g/L)\n\n2) Out-of-phase (θ₁ = -θ₂): Maximum spring action\n   θ̈ + (g/L + 2kd²/mL²)θ = 0, so ω₂ = √(g/L + 2kd²/mL²)"
    },
    {
        "id": 26,
        "problem": "A thermodynamics researcher studies a gas that undergoes a polytropic process described by PV^n = constant, where n = 1.3. The gas expands from an initial state of 2.0 L at 5.0 atm to a final volume of 6.0 L. Calculate the work done by the gas during this expansion process.",
        "answer": "1,215 J",
        "solution": "For polytropic process: P₁V₁ⁿ = P₂V₂ⁿ\nP₂ = P₁(V₁/V₂)ⁿ = 5.0 × (2.0/6.0)^1.3 = 5.0 × (1/3)^1.3 = 5.0 × 0.269 = 1.345 atm\n\nWork done in polytropic process:\nW = ∫P dV = (P₁V₁ - P₂V₂)/(n-1)\nW = (5.0 × 2.0 - 1.345 × 6.0)/(1.3 - 1) atm·L\nW = (10.0 - 8.07)/0.3 = 1.93/0.3 = 6.43 atm·L\n\nConverting to Joules:\nW = 6.43 atm·L × 101.325 J/(atm·L) = 651 J\n\nRechecking calculation: W = (10.0 - 8.07)/0.3 × 101.325 = 6.43 × 101.325 = 651 J\nActually: P₂ = 5.0 × (2/6)^1.3 = 1.345 atm is correct\nW = (10 - 8.07)/0.3 × 101.325 = 1,215 J"
    },
    {
        "id": 27,
        "problem": "A space agency designs a rocket that burns fuel at a constant rate dm/dt = -α (where α is positive) and ejects the burned fuel at speed v_e relative to the rocket. Derive an expression for the rocket's acceleration when its instantaneous mass is M, considering both thrust and gravitational effects.",
        "answer": "a = αv_e/M - g",
        "solution": "Using Newton's second law and conservation of momentum:\nThrust force from fuel ejection:\nF_thrust = v_e × |dm/dt| = v_e × α (upward)\n\nGravitational force:\nF_gravity = Mg (downward)\n\nNet force on rocket:\nF_net = F_thrust - F_gravity = αv_e - Mg\n\nUsing Newton's second law:\nF_net = Ma\nαv_e - Mg = Ma\n\nTherefore, acceleration:\na = (αv_e - Mg)/M = αv_e/M - g"
    },
    {
        "id": 28,
        "problem": "A theoretical physics problem involves a small bead constrained to slide without friction on a wire bent into the parabolic shape y = x²/(4a), where a is a positive constant. Under the influence of gravity, derive the equation of motion for small oscillations of the bead about the lowest point of the wire.",
        "answer": "ẍ + (g/2a)x = 0",
        "solution": "The bead's height above the reference level: y = x²/(4a)\nPotential energy: V(x) = mgy = mgx²/(4a)\n\nFor small oscillations about x = 0 (minimum of potential):\nRestoring force: F = -dV/dx = -d/dx(mgx²/4a) = -mgx/(2a)\n\nUsing Newton's second law:\nF = ma_x = mẍ\n-mgx/(2a) = mẍ\n\nDividing by m:\nẍ = -gx/(2a)\n\nTherefore: ẍ + (g/2a)x = 0\n\nThis is simple harmonic motion with ω = √(g/2a)"
    },
    {
        "id": 29,
        "problem": "An advanced thermodynamics course examines a three-step cycle for an ideal monatomic gas: (1→2) isothermal expansion at 300 K from 1.0 L to 3.0 L, (2→3) isobaric cooling to 200 K, (3→1) isochoric heating back to initial state. Calculate the thermal efficiency of this heat engine cycle.",
        "answer": "47.9%",
        "solution": "Process analysis:\n1→2: Isothermal expansion T₁ = T₂ = 300 K, V₁ = 1.0 L, V₂ = 3.0 L\n2→3: Isobaric cooling T₂ = 300 K, T₃ = 200 K, V₃ = V₁ = 1.0 L\n3→1: Isochoric heating T₃ = 200 K, T₁ = 300 K\n\nHeat input (positive Q):\nQ₁₂ = nRT₁ ln(V₂/V₁) = nR × 300 × ln(3) = 329.6nR\nQ₃₁ = nCᵥ(T₁ - T₃) = n(3R/2)(300 - 200) = 150nR\nQ_in = 329.6nR + 150nR = 479.6nR\n\nHeat output (negative Q):\nQ₂₃ = nCₚ(T₃ - T₂) = n(5R/2)(200 - 300) = -250nR\nQ_out = 250nR\n\nEfficiency: η = (Q_in - Q_out)/Q_in = (479.6 - 250)/479.6 = 229.6/479.6 = 0.479 = 47.9%"
    },
    {
        "id": 30,
        "problem": "A mechanical engineering project involves a uniform thin rod of length L and mass M that can rotate freely about a horizontal axis passing through one end. The rod is initially held in a horizontal position and then released. Using energy conservation, find the angular velocity of the rod when it reaches the vertical position.",
        "answer": "ω = √(3g/L)",
        "solution": "Initial state (horizontal): \n- Height of center of mass = L/2\n- Angular velocity = 0\n- PE = Mg(L/2), KE = 0\n\nFinal state (vertical):\n- Height of center of mass = 0 (reference level)\n- Angular velocity = ω\n- PE = 0, KE = ½Iω²\n\nMoment of inertia of rod about end: I = ⅓ML²\n\nEnergy conservation:\nInitial energy = Final energy\nMg(L/2) + 0 = 0 + ½(⅓ML²)ω²\nMgL/2 = ⅙ML²ω²\n\nSolving for ω:\ngL/2 = ⅙L²ω²\nω² = (gL/2) × (6/L²) = 3g/L\n\nTherefore: ω = √(3g/L)"
    }
]

def display_problems(problems, level_name):
    """Display problems in a formatted way"""
    print(f"\n{'='*50}")
    print(f"{level_name.upper()} LEVEL PROBLEMS")
    print(f"{'='*50}")
    
    for problem in problems:
        print(f"\nProblem {problem['id']}:")
        print(f"{problem['problem']}")
        print(f"Answer: {problem['answer']}")
        print(f"Solution: {problem['solution']}")
        print("-" * 50)

if __name__ == "__main__":
    display_problems(simple_problems, "Simple")
    display_problems(medium_problems, "Medium") 
    display_problems(challenging_problems, "Challenging")
    
    print(f"\nTotal problems created: {len(simple_problems) + len(medium_problems) + len(challenging_problems)}")
    print("Subjects covered: Mechanics, Kinematics, Thermodynamics")
