import streamlit as st
from utils import show_theory, show_success_message, render_experiment_layout, render_circuit_image
from tutor import SmartTutor
from circuits import draw_half_adder, draw_mux_4to1, draw_seven_segment, draw_generic_block

def render():
    st.title("Unit 2: Combinational Circuits")
    
    tutor = SmartTutor()
    
    tab1, tab2, tab3 = st.tabs(["Ex 3: Adder/Subtractor", "Ex 4: Mux/Demux", "Ex 5: Code Converters"])
    
    with tab1:
        run_experiment_3(tutor)
        
    with tab2:
        run_experiment_4(tutor)
        
    with tab3:
        run_experiment_5(tutor)

def run_experiment_3(tutor):
    tutor_config = [
        {
            "title": "🎯 Experiment Setup",
            "instruction": "Select **Half Adder** from the Circuit Type options. Half adders are the foundation of all arithmetic in computers.",
            "criteria": lambda c: c.get('circuit_type') == "Half Adder",
            "success_msg": "✓ Half Adder circuit initialized. This 2-gate circuit can add two binary digits!",
            "hint": "Half Adders use just an XOR gate (for sum) and an AND gate (for carry)."
        },
        {
            "title": "Micro-Experiment 1: Zero Addition (0 + 0)",
            "instruction": "Set both **Input A = 0** and **Input B = 0**. What happens when you add zero to zero?",
            "criteria": lambda c: c.get('circuit_type') == "Half Adder" and c.get('a') == 0 and c.get('b') == 0,
            "success_msg": "✓ Result: Sum=0, Carry=0. Adding zero to zero gives zero - the identity element of addition!",
        },
       {
            "title": "Verify Sum Component (XOR Behavior)",
            "instruction": "With inputs (0,0), observe **Sum = 0**. The XOR gate (A ⊕ B) produces the sum bit.",
            "criteria": lambda c: c.get('a') == 0 and c.get('b') == 0 and c.get('sum') == 0,
            "success_msg": "✓ XOR(0,0)=0 verified. The sum bit represents the modulo-2 addition.",
        },
        {
            "title": "Micro-Experiment 2: Adding 1 to 0",
            "instruction": "Set **Input A = 1** and **Input B = 0**. Predict: what will Sum and Carry be?",
            "criteria": lambda c: c.get('circuit_type') == "Half Adder" and c.get('a') == 1 and c.get('b') == 0,
            "success_msg": "✓ Result: Sum=1, Carry=0. One plus zero equals one - basic arithmetic!",
            "hint": "  1₂ + 0₂ = 1₂ in binary (same as decimal)."
        },
        {
            "title": "Verify No Carry Generated",
            "instruction": "With inputs (1,0), confirm **Carry = 0**. Carry only activates when Sum exceeds 1 (overflow to next bit position).",
            "criteria": lambda c: c.get('a') == 1 and c.get('b') == 0 and c.get('carry') == 0,
            "success_msg": "✓ AND(1,0)=0 verified. The AND gate detects when BOTH inputs are HIGH.",
        },
        {
            "title": "Micro-Experiment 3: Symmetric Test (0 + 1)",
            "instruction": "Now set **Input A = 0** and **Input B = 1**. Addition is commutative: does order matter?",
            "criteria": lambda c: c.get('circuit_type') == "Half Adder" and c.get('a') == 0 and c.get('b') == 1,
            "success_msg": "✓ Result: Sum=1, Carry=0 (same as before!). Commutativity confirmed: A+B = B+A.",
        },
        {
            "title": "Micro-Experiment 4: THE CRITICAL CASE (1 + 1)",
            "instruction": "Set **Input A = 1** and **Input B = 1**. This is where it gets interesting! What is 1+1 in binary?",
            "criteria": lambda c: c.get('circuit_type') == "Half Adder" and c.get('a') == 1 and c.get('b') == 1,
            "success_msg": "✓ Inputs set. Now observe the magic of binary overflow...",
            "hint": "In binary: 1₂ + 1₂ = 10₂ (which is 2 in decimal). We need TWO bits!"
        },
        {
            "title": "Verify Binary Overflow: Sum Bit",
            "instruction": "With inputs (1,1), observe **Sum = 0**. XOR(1,1)=0 because inputs are equal!",
            "criteria": lambda c: c.get('a') == 1 and c.get('b') == 1 and c.get('sum') == 0,
            "success_msg": "✓ Sum bit is 0 (the LSB of binary '10'). This is the 'ones place' of the result.",
        },
        {
            "title": "Verify Binary Overflow: Carry Bit",
            "instruction": "Confirm **Carry = 1**. This carry represents the '2' from 1+1=2. Together: Sum=0, Carry=1 → '10' in binary = 2 in decimal!",
            "criteria": lambda c: c.get('a') == 1 and c.get('b') == 1 and c.get('carry') == 1,
            "success_msg": "🎉 Perfect! Carry=1 (MSB of '10'). You've discovered bit overflow! This carry propagates to the next bit position in multi-bit addition.",
        },
        {
            "title": "Full Adder Introduction",
            "instruction": "Switch to **Full Adder** mode. Full Adders have a third input: **Carry-In (Cin)** from the previous stage. Set A=0, B=0, Cin=0.",
            "criteria": lambda c: c.get('circuit_type') == "Full Adder" and c.get('a') == 0 and c.get('b') == 0,
            "success_msg": "✓ Full Adder activated! This circuit is used to build n-bit adders by chaining multiple Full Adders together.",
            "hint": "Full Adders enable multi-bit arithmetic. A 32-bit adder uses 32 Full Adders!"
        },
        {
            "title": "Full Adder: Maximum Input Test",
            "instruction": "Set **A = 1**, **B = 1**, **Cin = 1**. This is the maximum possible input: 1+1+1. What's the result?",
            "criteria": lambda c: c.get('circuit_type') == "Full Adder" and c.get('a') == 1 and c.get('b') == 1,
            "success_msg": "✓ Result should be: Sum=1 (1+1+1 = 3 = 11₂), Carry-Out=1. This demonstrates carry propagation!",
            "hint": "1+1+1 = 3₁₀ = 11₂ in binary. So Sum=1 (LSB), Cout=1 (MSB)."
        },
        {
            "title": "Understanding Carry Propagation",
            "instruction": "With Full Adder at (1,1,1), observe how Cin contributes to the sum. This Cin would come from the previous bit position in a real CPU.",
            "criteria": lambda c: c.get('circuit_type') == "Full Adder",
            "success_msg": "✓ Carry chain understood! In a 4-bit adder, Cout from bit 0 becomes Cin for bit 1, and so on.",
        },
        {
            "title": "Final Challenge: Build Mental Model",
            "instruction": "Return to **Half Adder**, set A=1, B=1, and observe the outputs one final time. Now you understand how computers add numbers!",
            "criteria": lambda c: c.get('circuit_type') == "Half Adder" and c.get('a') == 1 and c.get('b') == 1 and c.get('sum') == 0 and c.get('carry') == 1,
            "success_msg": "🎓 MASTERY ACHIEVED! You've learned: (1) Half Adders add 2 bits, (2) XOR generates Sum, (3) AND generates Carry, (4) Full Adders chain for multi-bit arithmetic. Your CPU does exactly this billions of times per second!",
        }
    ]
    
    if 'u2_ex3_ctx' not in st.session_state: st.session_state.u2_ex3_ctx = {}

    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            🔬 <b>Lab Objective</b>: Build and test arithmetic circuits. Understand how binary addition is performed 
            at the hardware level using just 2 types of logic gates (XOR and AND).
        </p>
        """, unsafe_allow_html=True)
        
        circuit_type = st.radio("Select Circuit Type", ["Half Adder", "Full Adder"], horizontal=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown("### 🎛️ Input Controls")
            st.markdown("<br/>", unsafe_allow_html=True)
            
            a = st.number_input("Input A", 0, 1, 0, help="First binary input (0 or 1)")
            b = st.number_input("Input B", 0, 1, 0, help="Second binary input (0 or 1)")
            
            cin = 0
            if circuit_type == "Full Adder":
                cin = st.number_input("Carry In (Cin)", 0, 1, 0, help="Carry from previous bit position")
                st.info(f"💡 Decimal equivalent: {a} + {b} + {cin} = {a+b+cin}")
            else:
                st.info(f"💡 Decimal equivalent: {a} + {b} = {a+b}")
                
        with col2:
            st.markdown("### 🔬 Circuit Simulation")
            
            if circuit_type == "Half Adder":
                # Half Adder Logic
                sum_val = a ^ b
                carry_val = a and b
                
                img_buf = draw_half_adder(a, b)
                render_circuit_image(img_buf)
                
            else:
                # Full Adder Logic
                sum_val = (a ^ b) ^ cin
                carry_val = (a and b) or (cin and (a ^ b))
                
                # Use generic block for Full Adder
                active_out = {"Sum": sum_val, "Cout": carry_val}
                img_buf = draw_generic_block("Full Adder", ["A", "B", "Cin"], ["Sum", "Cout"], 
                                           active_inputs={"A": a, "B": b, "Cin": cin},
                                           active_outputs=active_out)
                render_circuit_image(img_buf)
            
            st.markdown("<br/>", unsafe_allow_html=True)
            
            # Results display with binary representation
            result_col1, result_col2 = st.columns(2)
            with result_col1:
                st.markdown(f"""
                <div class='lab-box' style='text-align: center; background: rgba(59, 130, 246, 0.15);'>
                    <h4 style='color: #60a5fa; margin-top: 0;'>Sum (LSB)</h4>
                    <p style='font-size: 2.5rem; font-family: "JetBrains Mono", monospace; 
                              color: #60a5fa; margin: 0; font-weight: 600;'>{sum_val}</p>
                    <p style='color: #93c5fd; font-size: 0.85rem; margin-top: 0.5rem;'>A ⊕ B{' ⊕ Cin' if circuit_type == 'Full Adder' else ''}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with result_col2:
                st.markdown(f"""
                <div class='lab-box' style='text-align: center; background: rgba(139, 92, 246, 0.15);'>
                    <h4 style='color: #a78bfa; margin-top: 0;'>Carry (MSB)</h4>
                    <p style='font-size: 2.5rem; font-family: "JetBrains Mono", monospace; 
                              color: #a78bfa; margin: 0; font-weight: 600;'>{carry_val}</p>
                    <p style='color: #c4b5fd; font-size: 0.85rem; margin-top: 0.5rem;'>Overflow</p>
                </div>
                """, unsafe_allow_html=True)
                
            # Show binary result
            binary_result = f"{carry_val}{sum_val}"
            decimal_result = carry_val * 2 + sum_val
            st.success(f"📊 **Binary Result**: {binary_result}₂ = **{decimal_result}₁₀** (decimal)")

        return {
            "circuit_type": circuit_type,
            "a": a,
            "b": b,
            "sum": sum_val,
            "carry": carry_val
        }

    theory = """
    ### Binary Addition: The Foundation of Computing
    
    **Half Adder (2-bit adder):**
    - **Inputs**: A, B (two binary digits)
    - **Outputs**: Sum (A ⊕ B), Carry (A · B)
    - **Gates Used**: 1 XOR + 1 AND
    - **Limitation**: Cannot handle carry from previous stage
    
    **Full Adder (3-bit adder):**
    - **Inputs**: A, B, Cin (carry from previous bit)
    - **Outputs**: Sum (A ⊕ B ⊕ Cin), Cout (majority function)
    - **Gates Used**: 2 XOR + 2 AND + 1 OR
    - **Application**: Chained together to build n-bit adders
    
    **Real-World Implementation:**
    - **Intel CPUs**: Use 64-bit ripple-carry or carry-lookahead adders
    - **Speed**: Modern adders complete in ~1 nanosecond
    - **Power**: Dynamic power = CV²f (capacitance × voltage² × frequency)
    
    **Advanced Architectures:**
    1. **Ripple-Carry Adder**: Simplest, slowest (O(n) delay)
    2. **Carry-Lookahead Adder**: Faster, more gates (O(log n) delay)
    3. **Carry-Select Adder**: Speedy compromise
    4. **Kogge-Stone Adder**: Fastest, highest area cost
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u2_ex3_ctx = ctx

    render_experiment_layout("Experiment 3: Adder Studio", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u2_ex3", tutor_steps_config=tutor_config, tutor_context=st.session_state.u2_ex3_ctx)


def run_experiment_4(tutor):
    tutor_config = [
        {
            "title": "Understanding Multiplexers",
            "instruction": "A 4:1 Multiplexer has 4 data inputs (D0-D3) and 2 select lines (S1, S0). The select lines choose which data input appears at the output.",
            "criteria": lambda c: True,
            "success_msg": "✓ Mux concept understood. Think of it as a digital switch with 4 positions!",
            "hint": "The 2-bit address S1S0 can represent 4 states: 00, 01, 10, 11."
        },
        {
            "title": "Observe Default Inputs",
            "instruction": "Note the default data: D0=1, D1=0, D2=1, D3=0. These are the signals available for routing.",
            "criteria": lambda c: c.get('d0') == 1,
            "success_msg": "✓ Input pattern observed: alternating 1010. This makes it easy to verify which input is selected.",
        },
        {
            "title": "Micro-Experiment 1: Select D0 (Address 00)",
            "instruction": "Set **S1 = 0** and **S0 = 0**. Binary 00 = decimal 0, which selects D0.",
            "criteria": lambda c: c.get('s1') == 0 and c.get('s0') == 0,
            "success_msg": "✓ Address 00 configured. The mux is now routing D0 to the output.",
            "hint": "Think of S1S0 as a 2-bit binary address pointing to one of 4 memory locations."
        },
        {
            "title": "Verify D0 Output",
            "instruction": "Confirm that **Output Y = 1** (matching D0's value). The signal has been routed!",
            "criteria": lambda c: c.get('s1') == 0 and c.get('s0') == 0 and c.get('output') == 1,
            "success_msg": "✓ Perfect! D0 → Output path verified. The multiplexer successfully routed the HIGH signal from D0.",
        },
        {
            "title": "Micro-Experiment 2: Select D1 (Address 01)",
            "instruction": "Change to **S1 = 0**, **S0 = 1**. Binary 01 = decimal 1 → selects D1.",
            "criteria": lambda c: c.get('s1') == 0 and c.get('s0') == 1,
            "success_msg": "✓ Address switched to 01. Now routing D1.",
        },
        {
            "title": "Verify D1 Output (Should be LOW)",
            "instruction": "Confirm **Output Y = 0** (D1's value). Notice how the output changed when you changed the select lines!",
            "criteria": lambda c: c.get('s1') == 0 and c.get('s0') == 1 and c.get('output') == 0,
            "success_msg": "✓ D1 → Output verified (Y=0). Instant switching demonstrated!",
        },
        {
            "title": "Micro-Experiment 3: Dynamic Data Change",
            "instruction": "While still at address 01 (selecting D1), change **D1 from 0 to 1**. Observe how the output immediately responds.",
            "criteria": lambda c: c.get('s1') == 0 and c.get('s0') == 1 and c.get('output') == 1,
            "success_msg": "✓ Dynamic routing verified! When D1 changes, the output changes instantly. This is how CPUs route data in real time.",
            "hint": "The mux is purely combinational - changes propagate in nanoseconds."
        },
        {
            "title": "Micro-Experiment 4: Select D2 (Address 10)",
            "instruction": "Set **S1 = 1**, **S0 = 0**. Binary 10 = decimal 2 → D2. Notice how S1 being HIGH means we're accessing the \"upper half\" of inputs (D2, D3).",
            "criteria": lambda c: c.get('s1') == 1 and c.get('s0') == 0,
            "success_msg": "✓ Address 10 (D2) selected. S1 acts as the MSB of the address.",
        },
        {
            "title": "Verify D2 Output",
            "instruction": "Confirm output matches D2's value.",
            "criteria": lambda c: c.get('s1') == 1 and c.get('s0') == 0 and c.get('output') == c.get('d0'),  # D2 default is 1
            "success_msg": "✓ D2 → Output path verified.",
        },
        {
            "title": "Micro-Experiment 5: Select D3 (Address 11)",
            "instruction": "Set **S1 = 1**, **S0 = 1**. Binary 11 = decimal 3 → D3. You've now tested all four paths!",
            "criteria": lambda c: c.get('s1') == 1 and c.get('s0') == 1,
            "success_msg": "✓ Maximum address 11 (D3) selected.",
        },
        {
            "title": "Complete Truth Table Verification",
            "instruction": "Observe the output matches D3's value. You've now verified all 4 selection states of the multiplexer!",
            "criteria": lambda c: c.get('s1') == 1 and c.get('s0') == 1 and c.get('output') == 0,
            "success_msg": "✓ D3 → Output verified. Complete truth table tested!",
        },
        {
            "title": "Advanced: Understand Multiplexer Applications",
            "instruction": "Muxes are used for: (1) Data routing in CPUs, (2) Selecting between ALU/Memory/Register outputs, (3) Implementing Boolean functions, (4) Time-division multiplexing in communication. Return to any address (00, 01, 10, or 11) to complete this experiment.",
            "criteria": lambda c: 's1' in c and 's0' in c,
            "success_msg": "🎉 EXPERIMENT COMPLETE! You've mastered the 4:1 multiplexer - a fundamental building block of computer architecture. Fun fact: A 64-bit CPU register file uses multiplexers to select which of 32+ registers to read!",
        }
    ]
    
    if 'u2_ex4_ctx' not in st.session_state: st.session_state.u2_ex4_ctx = {}

    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            🔬 <b>Lab Objective</b>: Understand data routing with multiplexers. Learn how CPUs select between multiple data sources using binary addressing.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 🎛️ Controls")
            
            st.markdown("#### Data Inputs (The Sources)")
            d0 = st.number_input("D0", 0, 1, 1, help="Data input 0")
            d1 = st.number_input("D1", 0, 1, 0, help="Data input 1")
            d2 = st.number_input("D2", 0, 1, 1, help="Data input 2")
            d3 = st.number_input("D3", 0, 1, 0, help="Data input 3")
            
            st.markdown("---")
            st.markdown("#### Select Lines (The Address)")
            s1 = st.radio("S1 (MSB - Most Significant Bit)", [0, 1], horizontal=True)
            s0 = st.radio("S0 (LSB - Least Significant Bit)", [0, 1], horizontal=True)
            
            # Show binary address
            address = f"{s1}{s0}"
            st.info(f"📍 **Current Address**: {address}₂ = {s1*2 + s0}₁₀")
            
        with col2:
            st.markdown("### 🔬 4:1 Mux Simulation")
            
            d_inputs = [d0, d1, d2, d3]
            select_lines = [s1, s0]
            
            img_buf = draw_mux_4to1(d_inputs, select_lines)
            render_circuit_image(img_buf)
            
            sel_idx = s1 * 2 + s0
            output = d_inputs[sel_idx]
            
            st.markdown(f"""
            <div class='lab-box' style='background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(16, 185, 129, 0.2) 100%); 
                        border: 1px solid rgba(34, 197, 94, 0.4); padding: 1.5rem; margin-top: 1rem;'>
                <h3 style='color: #22c55e; margin-top: 0; text-align: center;'>🎯 Signal Path</h3>
                <p style='text-align: center; font-size: 1.2rem; color: #86efac; margin: 0;'>
                    Address <span style='font-family: "JetBrains Mono"; font-weight: bold;'>{address}</span> 
                    → Selected: <span style='font-family: "JetBrains Mono"; font-weight: bold;'>D{sel_idx}</span> 
                    → Output: <span style='font-family: "JetBrains Mono"; font-weight: bold; color: {"#22c55e" if output else "#64748b"};'>{output}</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        return {
            "d0": d0,
            "d1": d1,
            "s1": s1,
            "s0": s0,
            "output": output
        }

    theory = """
    ### Multiplexers: Digital Data Switches
    
    **4:1 Multiplexer Specifications:**
    - **4 Data Inputs**: D0, D1, D2, D3
    - **2 Select Lines**: S1 (MSB), S0 (LSB)
    - **1 Output**: Y
    - **Function**: Y = D[S1S0] (output equals input at address S1S0)
    
    **Truth Table:**
    | S1 | S0 | Output Y |
    |----|----| ---------|
    | 0  | 0  | D0       |
    | 0  | 1  | D1       |
    | 1  | 0  | D2       |
    | 1  | 1  | D3       |
    
    **Real-World Applications:**
    1. **CPU Register File**: Selects which register to read (32-64 registers need 5-6 select lines)
    2. **ALU Input Selection**: Choose between register, memory, or immediate values
    3. **Bus Arbitration**: Decide which device gets access to shared data bus
    4. **Time-Division Multiplexing**: Telecommunications - multiple signals share one channel
    5. **Boolean Function Implementation**: Any logic function can be coded as a mux lookup table
    
    **Design Trade-offs:**
    - **Speed**: Mux adds propagation delay (~100ps in modern tech)
    - **Area**: Larger muxes (8:1, 16:1) need more gates
    - **Power**: Switching all paths wastes power; use mux only when needed
    
    **Fun Fact**: The first electronic multiplexer was built in 1938 for telephone switching!
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u2_ex4_ctx = ctx

    render_experiment_layout("Experiment 4: Multiplexer Logic", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u2_ex4", tutor_steps_config=tutor_config, tutor_context=st.session_state.u2_ex4_ctx)

def run_experiment_5(tutor):
    tutor_config = [
        {
            "title": "Understanding 7-Segment Displays",
            "instruction": "7-segment displays use 7 LED segments (labeled a-g) to show digits 0-9. Each digit requires a unique pattern of lit segments.",
            "criteria": lambda c: True,
            "success_msg": "✓ Display technology understood. This is how digital clocks, calculators, and measuring instruments show numbers!",
        },
        {
            "title": "Micro-Experiment 1: Display ZERO",
            "instruction": "Set the slider to **0**. Observe which segments light up to form the digit '0'.",
            "criteria": lambda c: c.get('decimal') == 0,
            "success_msg": "✓ Zero displayed. Segments a,b,c,d,e,f are LIT (all except 'g', the middle bar). This forms the shape '0'.",
            "hint": "The middle segment (g) is OFF for zero."
        },
        {
            "title": "Verify Binary Encoding",
            "instruction": "Confirm the Binary (BCD) shows **0000**. This 4-bit code is the input to the decoder circuit.",
            "criteria": lambda c: c.get('decimal') == 0 and c.get('binary') == '0000',
            "success_msg": "✓ BCD verified: 0₁₀ = 0000₂. The decoder translates this binary code to segment patterns.",
        },
        {
            "title": "Micro-Experiment 2: Display ONE",
            "instruction": "Set to **1**. Notice which segments light up. '1' uses the fewest segments!",
            "criteria": lambda c: c.get('decimal') == 1,
            "success_msg": "✓ One displayed using only segments b,c (the right vertical bars). Very efficient!",
        },
        {
            "title": "Micro-Experiment 3: Display EIGHT (Test Pattern)",
            "instruction": "Set to **8**. This is the universal test digit - it uses ALL seven segments!",
            "criteria": lambda c: c.get('decimal') == 8,
            "success_msg": "✓ Eight displayed with ALL segments lit! This tests that every LED is working.",
            "hint": "8 is used in manufacturing to test displays because it activates every segment."
        },
        {
            "title": "Verify Binary for 8",
            "instruction": "Confirm Binary shows **1000** (MSB is HIGH, others LOW). This is the BCD encoding for 8.",
            "criteria": lambda c: c.get('decimal') == 8 and c.get('binary') == '1000',
            "success_msg": "✓ BCD verified: 8₁₀ = 1000₂ (binary 8).",
        },
        {
            "title": "Micro-Experiment 4: Tricky Digit FIVE",
            "instruction": "Set to **5**. This is an interesting shape! Observe segments a,c,d,f,g are lit.",
            "criteria": lambda c: c.get('decimal') == 5,
            "success_msg": "✓ Five displayed. Notice it's similar to 'S' shape. Decoder logic for 5 is complex!",
        },
        {
            "title": "Micro-Experiment 5: Digit SIX",
            "instruction": "Set to **6**. Notice how similar it looks to 5, but with an extra bottom LED (segment e).",
            "criteria": lambda c: c.get('decimal') == 6,
            "success_msg": "✓ Six displayed. Segments a,c,d,e,f,g are lit. Minimalist design philosophy!",
        },
        {
            "title": "Micro-Experiment 6: Lucky SEVEN",
            "instruction": "Set to **7**. This vertical-right shape uses segments a,b,c.",
            "criteria": lambda c: c.get('decimal') == 7,
            "success_msg": "✓ Seven displayed. Top + right side segments. Different from '1' by including the top bar.",
        },
        {
            "title": "Micro-Experiment 7: Digit NINE",
            "instruction": "Set to **9**. All segments except 'e' are lit.",
            "criteria": lambda c: c.get('decimal') == 9,
            "success_msg": "✓ Nine displayed. Mirror image of 6 in some sense!",
        },
        {
            "title": "Explore Remaining Digits",
            "instruction": "Cycle through digits 2, 3, 4 to complete your exploration. Each has a unique segment pattern!",
            "criteria": lambda c: c.get('decimal') in [2, 3, 4],
            "success_msg": "✓ Additional digits explored! Each digit has a carefully designed pattern for clarity.",
        },
        {
            "title": "Final Challenge: Understand the Decoder",
            "instruction": "The BCD-to-7-Segment decoder is a combinational circuit with 4 inputs (BCD) and 7 outputs (segments). It's implemented using Boolean logic (AND/OR/NOT gates) or a lookup table. Review all 10 digits (0-9) to complete the experiment.",
            "criteria": lambda c: 'decimal' in c and 'binary' in c,
            "success_msg": "🎉 COMPLETE! You've learned how binary data becomes human-readable displays. This decoder circuit is in every digital clock, calculator, and measuring instrument. Fun fact: The first 7-segment displays were used in telephones in the 1960s!",
        }
    ]
    
    if 'u2_ex5_ctx' not in st.session_state: st.session_state.u2_ex5_ctx = {}

    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            🔬 <b>Lab Objective</b>: Understand how binary data is converted to human-readable visual formats. 
            Learn the BCD-to-7-Segment decoding process used in billions of devices worldwide.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 🎛️ Input Encoder")
            decimal_val = st.slider("Select Decimal Digit", 0, 9, 0, 
                                    help="Choose a decimal digit (0-9) to encode and display")
            
            binary_val = format(decimal_val, '04b')
            
            st.markdown(f"""
            <div class='lab-box' style='background: rgba(59, 130, 246, 0.15); padding: 1.5rem;'>
                <h4 style='color: #60a5fa; margin-top: 0;'>Binary Coded Decimal (BCD)</h4>
                <p style='font-size: 2rem; font-family: "JetBrains Mono"; color: #60a5fa; margin: 0; font-weight: bold;'>{binary_val}</p>
                <p style='color: #93c5fd; font-size: 0.9rem; margin-top: 0.5rem;'>
                    Bits: D₃={binary_val[0]} D₂={binary_val[1]} D₁={binary_val[2]} D₀={binary_val[3]}
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.info(f"💡 This 4-bit BCD code is fed to the decoder circuit, which converts it to 7 segment control signals.")
            
        with col2:
            st.markdown("### 📺 7-Segment Display Output")
            
            img_buf = draw_seven_segment(decimal_val)
            render_circuit_image(img_buf)
            
            # Show which segments are active
            segment_map = {
                0: "a,b,c,d,e,f",
                1: "b,c",
                2: "a,b,d,e,g",
                3: "a,b,c,d,g",
                4: "b,c,f,g",
                5: "a,c,d,f,g",
                6: "a,c,d,e,f,g",
                7: "a,b,c",
                8: "a,b,c,d,e,f,g",
                9: "a,b,c,d,f,g"
            }
            
            active_segments = segment_map.get(decimal_val, "")
            st.caption(f"**Active Segments**: {active_segments}")
            
        return {
            "decimal": decimal_val,
            "binary": binary_val
        }

    theory = """
    ### BCD to 7-Segment Decoder: Digital Display Technology
    
    **Components:**
    - **Input**: 4-bit BCD (Binary Coded Decimal): D₃ D₂ D₁ D₀
    - **Output**: 7 control signals (one per segment): a, b, c, d, e, f, g
    - **Segments Layout**:
      ```
          a
         ---
      f |   | b
         -g-
      e |   | c
         ---
          d
      ```
    
    **Implementation Methods:**
    1. **Combinational Logic**: Design using K-maps for each segment
       - Example: Segment 'a' = D₃ + D₁ + (D₂ · D₀) + (D₂' · D₀')
    2. **ROM/LUT**: 16-word lookup table (stores pattern for each digit)
    3. **Decoder IC**: Pre-fabricated chips (e.g., 7447, CD4511)
    
    **Truth Table Example** (partial):
    | D₃ | D₂ | D₁ | D₀ | Decimal | a | b | c | d | e | f | g |
    |----|----|----|----| --------|---|---|---|---|---|---|---|
    | 0  | 0  | 0  | 0  | 0       | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
    | 0  | 0  | 0  | 1  | 1       | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
    | 0  | 0  | 1  | 0  | 2       | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
    | 1  | 0  | 0  | 0  | 8       | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
    
    **Real-World Applications:**
    - Digital clocks and watches
    - Calculators
    - Multimeters and measuring instruments
    - Microwave ovens
    - Gas station pumps
    - Scoreboards
    
    **Display Types:**
    - **Common Cathode**: All cathodes tied to ground, anodes controlled
    - **Common Anode**: All anodes tied to VCC, cathodes controlled
    - **LED vs LCD**: LEDs are brighter, LCDs use less power
    
    **Modern Evolution**: OLED and LCD displays have replaced 7-segments in most consumer electronics, but they remain popular for industrial applications due to reliability and low cost
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u2_ex5_ctx = ctx

    render_experiment_layout("Experiment 5: Code Converters", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u2_ex5", tutor_steps_config=tutor_config, tutor_context=st.session_state.u2_ex5_ctx)
