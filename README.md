# 🎓 Virtual Digital Logic Design Lab

An interactive virtual laboratory for B.Tech 2nd-year ECE students to learn digital logic design through hands-on experiments with intelligent tutoring.

## ✨ Features

- **12 Comprehensive Experiments** covering digital logic fundamentals to advanced topics
- **Smart Tutor System** with 10+ micro-experiments per lab (~30 min engagement)
- **Interactive Visualizations** using schemdraw for circuits and graphviz for state machines
- **Professional Dark UI** with engineering aesthetics
- **State-Aware Guidance** with contextual hints and validation

## 📚 Curriculum Coverage

### Unit 1: Basics of Digital Logic
- **Experiment 1**: Logic Gates (16 steps)
- **Experiment 2**: K-Map Simplification (10 steps)

### Unit 2: Combinational Circuits
- **Experiment 3**: Adder/Subtractor (13 steps)
- **Experiment 4**: Multiplexer Logic (13 steps)
- **Experiment 5**: 7-Segment Display (12 steps)

### Unit 3: Sequential Circuits
- **Experiment 6**: Flip-Flops (8 steps)
- **Experiment 7**: Shift Registers (8 steps)
- **Experiment 8**: Counters (9 steps)

### Unit 4: Advanced Logic
- **Experiment 9**: FSM Sequence Detector (10 steps)
- **Experiment 10**: Vending Machine Controller (10 steps)

### Unit 5: PLDs & Memory
- **Experiment 11**: PLA Designer (10 steps)
- **Experiment 12**: FPGA LUT Configuration (9 steps)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Digital_Logic_Design_Lab.git
cd Digital_Logic_Design_Lab
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

4. Open your browser to `http://localhost:8501`

## 📦 Dependencies

- `streamlit` - Web application framework
- `matplotlib` - Circuit visualization
- `schemdraw` - Professional circuit diagrams
- `graphviz` - State machine diagrams
- `numpy`, `pandas` - Data processing

## 🎯 Pedagogical Approach

Each experiment uses the **Predict-Test-Verify** methodology:
1. **Setup**: Understand the circuit/concept
2. **Micro-Experiments**: Test specific input combinations
3. **Edge Cases**: Explore critical scenarios (overflow, boundaries)
4. **Synthesis**: Connect to real-world applications

## 🏗️ Architecture

```
Digital_Logic_Design_Lab/
├── main.py                 # Entry point & routing
├── tutor.py               # Smart Tutor engine
├── utils.py               # Shared UI components
├── circuits.py            # Circuit visualization
├── units/
│   ├── unit1_basics.py
│   ├── unit2_combinational.py
│   ├── unit3_sequential.py
│   ├── unit4_advanced.py
│   └── unit5_pld_memory.py
└── requirements.txt
```

## 🎨 Design Philosophy

- **Dark Mode First**: Reduces eye strain during long lab sessions
- **Glassmorphism**: Modern, professional aesthetic
- **Color-Coded Signals**: Blue (inputs), Purple (processing), Green (outputs)
- **Responsive Layout**: 3:1 split (main content : tutor panel)

## 📈 Learning Outcomes

Students will be able to:
- Design and analyze combinational and sequential circuits
- Understand state machines and memory elements
- Program PLDs and FPGAs using truth tables
- Apply Boolean algebra for circuit minimization
- Build mental models of how CPUs process information

## 🤝 Contributing

Contributions welcome! Please feel free to submit pull requests or open issues for:
- New experiments
- Improved visualizations
- Bug fixes
- Documentation enhancements

## 📄 License

MIT License - feel free to use this for educational purposes.

## 👨‍💻 Author

Created as a virtual lab replacement for hands-on digital logic experiments.

## 🙏 Acknowledgments

- Claude Shannon for Boolean algebra foundations
- Streamlit team for the amazing framework
- All ECE educators who inspired this project

---

**Note**: This is designed for educational use. Real hardware labs provide tactile learning that complements this virtual experience.
