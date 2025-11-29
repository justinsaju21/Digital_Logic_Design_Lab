import streamlit as st
from utils import render_experiment_layout, render_circuit_image
from tutor import SmartTutor
from circuits import draw_flip_flop, draw_generic_block

def render():
    st.title("Unit 3: Sequential Circuits")
    
    tutor = SmartTutor()
    
    tab1, tab2, tab3 = st.tabs(["Ex 6: Flip-Flops", "Ex 7: Shift Registers", "Ex 8: Counters"])
    
    with tab1:
        run_experiment_6(tutor)
    with tab2:
        run_experiment_7(tutor)
    with tab3:
        run_experiment_8(tutor)

def run_experiment_6(tutor):
    tutor_config = [
        {
            "title": "Select SR Flip-Flop",
            "instruction": "Select **SR Flip-Flop** from the dropdown menu to begin sequential circuit analysis.",
            "criteria": lambda c: c.get('ff_type') == "SR",
            "success_msg": "✓ SR Flip-Flop selected. This is the fundamental memory element.",
            "hint": "SR stands for Set-Reset."
        },
        {
            "title": "Understand Initial State",
            "instruction": "Observe the current state **Q**. It should be 0 (reset state).",
            "criteria": lambda c: c.get('ff_type') == "SR",
            "success_msg": "✓ Initial state observed. Q stores the flip-flop's memory.",
        },
        {
            "title": "SET Operation: Configure Inputs",
            "instruction": "Set **S = 1** (Set) and **R = 0** (Not Reset). This prepares the SET operation.",
            "criteria": lambda c: c.get('ff_type') == "SR" and c.get('s') == 1 and c.get('r') == 0,
            "success_msg": "✓ Inputs configured for SET operation (S=1, R=0).",
            "hint": "SET means we want to store a '1' in the flip-flop."
        },
        {
            "title": "SET Operation: Trigger Clock",
            "instruction": "Click **Pulse Clock** to trigger the flip-flop on the rising edge.",
            "criteria": lambda c: c.get('ff_type') == "SR" and c.get('s') == 1 and c.get('r') == 0 and c.get('clk_pulsed') == 1,
            "success_msg": "✓ Clock pulsed! The rising edge is when data is captured.",
            "hint": "The clock pulse simulates a voltage transition from 0V to 5V."
        },
        {
            "title": "SET Operation: Verify State",
            "instruction": "Verify that **Q = 1** after the clock pulse. The flip-flop has 'remembered' the SET command.",
            "criteria": lambda c: c.get('ff_type') == "SR" and c.get('q') == 1,
            "success_msg": "✓ Excellent! Q=1 confirms the SET operation succeeded. The flip-flop now stores a '1' in memory.",
        },
        {
            "title": "RESET Operation: Configure Inputs",
            "instruction": "Now set **S = 0** and **R = 1** (Reset operation). Pulse the clock to reset Q to 0.",
            "criteria": lambda c: c.get('ff_type') == "SR" and c.get('s') == 0 and c.get('r') == 1 and c.get('q') == 0,
            "success_msg": "✓ RESET verified! Q returned to 0. The flip-flop was cleared.",
            "hint": "RESET forces Q to 0, clearing the stored bit."
        },
        {
            "title": "Explore D Flip-Flop",
            "instruction": "Switch to **D Flip-Flop** and set D=1. Pulse the clock and observe Q=1. D Flip-Flops are simpler: Q follows D.",
            "criteria": lambda c: c.get('ff_type') == "D" and c.get('q') == 1,
            "success_msg": "✓ D Flip-Flop mastered! This is the most common type in modern circuits (used in registers and memory).",
            "hint": "D Flip-Flops eliminate the invalid S=R=1 state of SR flip-flops."
        },
        {
            "title": "Explore T Flip-Flop (Toggle)",
            "instruction": "Switch to **T Flip-Flop**, set T=1, and pulse the clock twice. Observe Q toggling between 0 and 1.",
            "criteria": lambda c: c.get('ff_type') == "T",
            "success_msg": "✓ T Flip-Flop explored! Toggle flip-flops are used in counters and frequency dividers.",
            "hint": "Each clock pulse with T=1 inverts the output."
        }
    ]
    
    if 'u3_ex6_ctx' not in st.session_state: st.session_state.u3_ex6_ctx = {}

    def simulation():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            ff_type = st.selectbox("Flip-Flop Type", ["SR", "JK", "D", "T"])
            st.markdown("---")
            
            # State management
            if 'q' not in st.session_state: st.session_state.q = 0
            if 'clk_state' not in st.session_state: st.session_state.clk_state = 0 # 0 or 1
            
            # Inputs
            inputs = {}
            s, r, j, k, d, t_val = 0, 0, 0, 0, 0, 0
            
            if ff_type == "SR":
                s = st.radio("S", [0, 1], horizontal=True)
                r = st.radio("R", [0, 1], horizontal=True)
                inputs['S'] = s
                inputs['R'] = r
            elif ff_type == "JK":
                j = st.radio("J", [0, 1], horizontal=True)
                k = st.radio("K", [0, 1], horizontal=True)
                inputs['J'] = j
                inputs['K'] = k
            elif ff_type == "D":
                d = st.radio("D", [0, 1], horizontal=True)
                inputs['D'] = d
            elif ff_type == "T":
                t_val = st.radio("T", [0, 1], horizontal=True)
                inputs['T'] = t_val
                
            # Clock Button (Simulates a full pulse: 0 -> 1 -> 0)
            clk_pulsed = 0
            if st.button("Pulse Clock 🕰️"):
                # Logic update on rising edge
                q = st.session_state.q
                if ff_type == "SR":
                    if s==1 and r==0: q=1
                    elif s==0 and r==1: q=0
                    elif s==1 and r==1: st.error("⚠️ Invalid State (S=1, R=1) - Undefined behavior!")
                elif ff_type == "JK":
                    if j==1 and k==0: q=1
                    elif j==0 and k==1: q=0
                    elif j==1 and k==1: q = 1-q
                elif ff_type == "D":
                    q = d
                elif ff_type == "T":
                    if t_val: q = 1-q
                st.session_state.q = q
                st.session_state.clk_state = 1 # Visual feedback for pulse
                clk_pulsed = 1
            else:
                st.session_state.clk_state = 0
            
        with col2:
            img = draw_flip_flop(ff_type, inputs, st.session_state.q, 1-st.session_state.q, st.session_state.clk_state)
            render_circuit_image(img)
            
            st.markdown(f"""
            <div class='lab-box' style='text-align: center; background: rgba(59, 130, 246, 0.15);'>
                <h4 style='color: #60a5fa; margin-top: 0;'>Current State</h4>
                <p style='font-size: 2.5rem; font-family: "JetBrains Mono", monospace; 
                          color: #60a5fa; margin: 0; font-weight: 600;'>Q = {st.session_state.q}</p>
                <p style='color: #93c5fd; font-size: 0.9rem; margin-top: 0.5rem;'>
                    Q̄ (inverted) = {1 - st.session_state.q}
                </p>
            </div>
            """, unsafe_allow_html=True)

        return {
            "ff_type": ff_type,
            "s": s,
            "r": r,
            "clk_pulsed": clk_pulsed,
            "q": st.session_state.q
        }

    theory = """
    **Flip-Flops** are the fundamental building blocks of digital electronics systems used in computers and communications.
    They are **bistable devices** - they have two stable states (Q=0 or Q=1) and can store one bit of information.
    
    ### Types:
    *   **SR Flip-Flop**: Set/Reset. S=1 sets Q=1, R=1 resets Q=0. S=R=1 is invalid.
    *   **JK Flip-Flop**: Improved SR. J=1/K=1 toggles the output (eliminates invalid state).
    *   **D Flip-Flop**: Data/Delay. Q follows D on clock edge. Most common in modern systems.
    *   **T Flip-Flop**: Toggle. T=1 toggles Q on clock edge. Used in counters.
    
    ### Clock Signal:
    - **Edge-Triggered**: Data is captured ONLY on the rising edge (0→1 transition) of the clock.
    - **Level-Triggered**: Data is captured whenever clock is HIGH (used in latches, not flip-flops).
    
    **Applications**: Registers, RAM cells, state machines, frequency dividers.
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u3_ex6_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 6: Flip-Flop Fundamentals", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u3_ex6", tutor_steps_config=tutor_config, tutor_context=st.session_state.u3_ex6_ctx)

def run_experiment_7(tutor):
    tutor_config = [
        {
            "title": "Clear Register to Initial State",
            "instruction": "Press **Clear** to reset all register bits to `0000`.",
            "criteria": lambda c: c.get('reg') == [0, 0, 0, 0],
            "success_msg": "✓ Register cleared to 0000. This is the initialization step.",
            "hint": "The Clear button asynchronously resets all flip-flops regardless of clock."
        },
        {
            "title": "Understanding Shift Direction",
            "instruction": "This is a **Right-Shift** register. Data flows: Data In → Q3 → Q2 → Q1 → Q0. Observe the current state shows Q3=Q2=Q1=Q0=0.",
            "criteria": lambda c: c.get('reg') == [0, 0, 0, 0],
            "success_msg": "✓ Shift direction understood. Each clock pulse moves data one position to the right.",
        },
        {
            "title": "Load First Bit (1)",
            "instruction": "Set **Data In = 1** and click **Pulse Clock**. The bit enters Q3.",
            "criteria": lambda c: c.get('reg') == [1, 0, 0, 0],
            "success_msg": "✓ First bit loaded! Q3=1, others remain 0.",
            "hint": "After one clock: old Q3→Q2, old Q2→Q1, old Q1→Q0, Data In→Q3"
        },
        {
            "title": "Load Second Bit (0)",
            "instruction": "Set **Data In = 0** and **Pulse Clock**. Watch Q3's old value shift to Q2.",
            "criteria": lambda c: c.get('reg') == [0, 1, 0, 0],
            "success_msg": "✓ Second bit loaded! Q3=0, Q2=1 (the previous Q3 value).",
        },
        {
            "title": "Load Third Bit (1)",
            "instruction": "Set **Data In = 1** and **Pulse Clock**. Continue building the pattern.",
            "criteria": lambda c: c.get('reg') == [1, 0, 1, 0],
            "success_msg": "✓ Third bit loaded! Pattern emerging: 1010...",
        },
        {
            "title": "Complete Pattern 1010",
            "instruction": "Set **Data In = 0** and **Pulse Clock** one final time to complete the 1010 pattern.",
            "criteria": lambda c: c.get('reg') == [0, 1, 0, 1],
            "success_msg": "✓ Pattern incomplete. Try: Data=1, Pulse, Data=0, Pulse, Data=1, Pulse, Data=0, Pulse from clear state.",
            "hint": "To get 1010 in Q3Q2Q1Q0: Load bits in reverse order (0,1,0,1) due to right-shift."
        },
        {
            "title": "Alternative: Achieve 1010 Pattern",
            "instruction": "Starting from clear (0000), load: Data=1→Pulse, Data=0→Pulse, Data=1→Pulse, Data=0→Pulse to get Q3Q2Q1Q0=1010.",
            "criteria": lambda c: c.get('reg') == [1, 0, 1, 0],
            "success_msg": "✓ Perfect! 1010 pattern achieved. You've mastered serial data loading!",
            "hint": "Right-shift means: newest bit goes to Q3 (leftmost position)."
        },
        {
            "title": "Experiment with Other Patterns",
            "instruction": "Try loading different patterns like 1111 or 0101. Each pattern requires 4 clock pulses.",
            "criteria": lambda c: len(c.get('reg', [])) == 4,
            "success_msg": "✓ Experimentation complete! Shift registers are used in serial communication (UART, SPI) and data storage.",
        }
    ]
    
    if 'u3_ex7_ctx' not in st.session_state: st.session_state.u3_ex7_ctx = {}
    
    # Register State: [Q3, Q2, Q1, Q0] - SISO Left to Right: In -> Q3 -> Q2 -> Q1 -> Q0
    if 'u3_ex7_reg' not in st.session_state: st.session_state.u3_ex7_reg = [0, 0, 0, 0]
    
    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            Simulate a 4-bit Serial-In Serial-Out (SISO) Shift Register. Data enters at Q3 and shifts right towards Q0.
            This is how serial communication protocols (e.g., USB, SPI) transmit data one bit at a time.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 🎛️ Controls")
            data_in = st.radio("Data In (Serial)", [0, 1], horizontal=True)
            
            col_btns = st.columns(2)
            pulse = col_btns[0].button("Pulse Clock 🕰️", key="sr_pulse")
            clear = col_btns[1].button("Clear 🗑️", key="sr_clear")
            
            if clear:
                st.session_state.u3_ex7_reg = [0, 0, 0, 0]
                st.rerun()
                
            if pulse:
                # Shift Right: In -> Q3, Q3->Q2, Q2->Q1, Q1->Q0
                reg = st.session_state.u3_ex7_reg
                new_reg = [data_in] + reg[:-1]
                st.session_state.u3_ex7_reg = new_reg
                
        with col2:
            st.markdown("### 🔬 Register State")
            reg = st.session_state.u3_ex7_reg
            
            # Visualize as a generic block with active outputs showing the bits
            active_outs = {
                "Q3": reg[0],
                "Q2": reg[1],
                "Q1": reg[2],
                "Q0": reg[3]
            }
            img = draw_generic_block("4-Bit Shift Register", ["Data In", "Clk", "Clear"], ["Q3", "Q2", "Q1", "Q0"],
                                   active_inputs={"Data In": data_in},
                                   active_outputs=active_outs)
            render_circuit_image(img)
            
            st.markdown(f"""
            <div style='display: flex; justify-content: center; gap: 1rem; margin-top: 1rem;'>
                <div class='lab-box' style='padding: 1rem 1.5rem; background: {"rgba(59, 130, 246, 0.2)" if reg[0] else "rgba(30, 41, 59, 0.5)"};'>
                    <span style='color: #94a3b8; font-size: 0.9rem;'>Q3 (MSB)</span><br/>
                    <span style='font-size: 2rem; font-weight: bold; color: {"#60a5fa" if reg[0] else "#64748b"};'>{reg[0]}</span>
                </div>
                <div class='lab-box' style='padding: 1rem 1.5rem; background: {"rgba(139, 92, 246, 0.2)" if reg[1] else "rgba(30, 41, 59, 0.5)"};'>
                    <span style='color: #94a3b8; font-size: 0.9rem;'>Q2</span><br/>
                    <span style='font-size: 2rem; font-weight: bold; color: {"#a78bfa" if reg[1] else "#64748b"};'>{reg[1]}</span>
                </div>
                <div class='lab-box' style='padding: 1rem 1.5rem; background: {"rgba(236, 72, 153, 0.2)" if reg[2] else "rgba(30, 41, 59, 0.5)"};'>
                    <span style='color: #94a3b8; font-size: 0.9rem;'>Q1</span><br/>
                    <span style='font-size: 2rem; font-weight: bold; color: {"#ec4899" if reg[2] else "#64748b"};'>{reg[2]}</span>
                </div>
                <div class='lab-box' style='padding: 1rem 1.5rem; background: {"rgba(34, 197, 94, 0.2)" if reg[3] else "rgba(30, 41, 59, 0.5)"};'>
                    <span style='color: #94a3b8; font-size: 0.9rem;'>Q0 (LSB)</span><br/>
                    <span style='font-size: 2rem; font-weight: bold; color: {"#22c55e" if reg[3] else "#64748b"};'>{reg[3]}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        return {
            "reg": reg
        }

    theory = """
    **Shift Registers** are used for data storage and movement in digital systems.
    
    ### Types:
    *   **SISO**: Serial In Serial Out. Data is shifted in one bit at a time.
    *   **SIPO**: Serial In Parallel Out. Data is shifted in serially but available at all outputs simultaneously.
    *   **PISO**: Parallel In Serial Out. All data loaded at once, then shifted out one bit at a time.
    *   **PIPO**: Parallel In Parallel Out. Used as temporary storage (registers).
    
    ### Applications:
    - **Serial Communication**: UART, SPI, I2C protocols
    - **Data Conversion**: Serial-to-Parallel and vice versa
    - **Delay Lines**: Creating time delays in digital signals
    - **Ring Counters**: When output is fed back to input
    
    **Fun Fact**: Old computer monitors used shift registers to convert serial pixel data into parallel RGB signals!
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u3_ex7_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 7: Shift Registers", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u3_ex7", tutor_steps_config=tutor_config, tutor_context=st.session_state.u3_ex7_ctx)

def run_experiment_8(tutor):
    tutor_config = [
        {
            "title": "Observe Initial State",
            "instruction": "The counter starts at **0 (0000)**. This is the reset state.",
            "criteria": lambda c: True,
            "success_msg": "✓ Initial state observed.",
        },
        {
            "title": "First Count Increment",
            "instruction": "Click **Pulse Clock** to increment the counter to **1 (0001)**.",
            "criteria": lambda c: c.get('count') == 1,
            "success_msg": "✓ Counter incremented! Only the LSB (Q0) toggled from 0→1.",
            "hint": "Each clock pulse increases the binary value by 1."
        },
        {
            "title": "Continue to Count 2",
            "instruction": "Pulse the clock again to reach **2 (0010)**.",
            "criteria": lambda c: c.get('count') == 2,
            "success_msg": "✓ Count = 2. Notice Q1 is now HIGH, Q0 returned to LOW.",
        },
        {
            "title": "Observe Binary Carry",
            "instruction": "Pulse to count **3 (0011)**. Both Q0 and Q1 are now HIGH.",
            "criteria": lambda c: c.get('count') == 3,
            "success_msg": "✓ Binary addition observed: 11₂ = 3₁₀",
        },
        {
            "title": "Reach Count 5 (0101)",
            "instruction": "Continue pulsing until the counter reaches **5 (0101)**. This demonstrates the target value.",
            "criteria": lambda c: c.get('count') == 5,
            "success_msg": "✓ Count 5 reached! Binary: 0101. The 4-bit counter can count from 0 to 15.",
            "hint": "You may need to pulse multiple times. Watch the binary representation change!"
        },
        {
            "title": "Explore Higher Counts",
            "instruction": "Pulse several more times to see counts 6, 7, 8, 9, 10... Watch the MSB (Q3) activate at count 8 (1000).",
            "criteria": lambda c: c.get('count') >= 8,
            "success_msg": "✓ MSB activated! Q3=1 means the counter exceeded 7. The MSB represents the '8' place value.",
        },
        {
            "title": "Reach Maximum Count 15",
            "instruction": "Keep pulsing to reach **15 (1111)** - all bits HIGH. This is the maximum for a 4-bit counter.",
            "criteria": lambda c: c.get('count') == 15,
            "success_msg": "✓ Maximum count! All four bits are 1. Next pulse will cause overflow...",
            "hint": "The counter will wrap around to 0 on the next pulse (modulo-16 behavior)."
        },
        {
            "title": "Observe Rollover",
            "instruction": "Pulse once more. The counter should **rollover** from 15 back to **0**.",
            "criteria": lambda c: c.get('count') == 0,
            "success_msg": "✓ Rollover demonstrated! This is modulo-16 arithmetic (wraps at 2^4).",
        },
        {
            "title": "Reset Counter",
            "instruction": "Press **Reset** to asynchronously clear the counter to 0, regardless of current count.",
            "criteria": lambda c: c.get('count') == 0,
            "success_msg": "✓ Reset verified! Asynchronous reset immediately clears all flip-flops without waiting for the clock.",
        }
    ]
    
    if 'u3_ex8_ctx' not in st.session_state: st.session_state.u3_ex8_ctx = {}
    
    if 'u3_ex8_count' not in st.session_state: st.session_state.u3_ex8_count = 0
    if 'u3_ex8_history' not in st.session_state: st.session_state.u3_ex8_history = []
    
    def simulation():
        st.markdown("""
        <p style='color: #94a3b8; font-size: 1.05rem; margin-bottom: 2rem;'>
            Simulate a 4-bit Synchronous Up-Counter. It counts from 0 to 15 (0000 to 1111) and then wraps around.
            This is the foundation of CPU clock dividers and timers.
        </p>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("### 🎛️ Controls")
            col_btns = st.columns(2)
            pulse = col_btns[0].button("Pulse Clock 🕰️", key="ctr_pulse")
            reset = col_btns[1].button("Reset 🔄", key="ctr_reset")
            
            if reset:
                st.session_state.u3_ex8_count = 0
                st.session_state.u3_ex8_history = [] # Clear history
                st.rerun()
                
            if pulse:
                st.session_state.u3_ex8_count = (st.session_state.u3_ex8_count + 1) % 16
                # Log state to history
                count = st.session_state.u3_ex8_count
                binary_str = format(count, '04b')
                st.session_state.u3_ex8_history.append({
                    "Step": len(st.session_state.u3_ex8_history) + 1,
                    "Decimal": count,
                    "Binary": binary_str,
                    "Q3": binary_str[0], "Q2": binary_str[1], "Q1": binary_str[2], "Q0": binary_str[3]
                })
                
        with col2:
            st.markdown("### 🔬 Counter State")
            count = st.session_state.u3_ex8_count
            
            # Convert to binary string
            binary_str = format(count, '04b')
            b3, b2, b1, b0 = int(binary_str[0]), int(binary_str[1]), int(binary_str[2]), int(binary_str[3])
            
            active_outs = {
                "Q3": b3,
                "Q2": b2,
                "Q1": b1,
                "Q0": b0
            }
            
            img = draw_generic_block("4-Bit Counter", ["Clk", "Reset"], ["Q3", "Q2", "Q1", "Q0"],
                                   active_outputs=active_outs)
            render_circuit_image(img)
            
            st.markdown(f"""
            <div style='text-align: center; margin-top: 1rem;'>
                <div class='lab-box' style='display: inline-block; padding: 1.5rem 2.5rem; background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);'>
                    <span style='font-size: 1.2rem; color: #94a3b8;'>Decimal</span><br/>
                    <span style='font-size: 3.5rem; font-weight: bold; color: #60a5fa; font-family: "JetBrains Mono", monospace;'>{count}</span>
                </div>
                <div class='lab-box' style='display: inline-block; padding: 1.5rem 2.5rem; margin-left: 1rem; background: linear-gradient(135deg, rgba(236, 72, 153, 0.2) 0%, rgba(251, 191, 36, 0.2) 100%);'>
                    <span style='font-size: 1.2rem; color: #94a3b8;'>Binary (4-bit)</span><br/>
                    <span style='font-size: 3.5rem; font-weight: bold; color: #ec4899; font-family: "JetBrains Mono", monospace;'>{binary_str}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Trace Table Visualization
        if st.session_state.u3_ex8_history:
            st.markdown("### 📝 State Trace Table")
            st.markdown("This table records the state of the counter after each clock pulse, helping you visualize the counting sequence.")
            st.dataframe(st.session_state.u3_ex8_history, use_container_width=True)

        return {
            "count": count
        }

    theory = """
    **Counters** cycle through a sequence of states and are essential for:
    - Timekeeping and clock generation
    - Address generation in memory
    - Control sequencing in CPUs
    - Frequency division
    
    ### Types:
    *   **Asynchronous (Ripple)**: Flip-flops clocked by previous stage output. Slower due to propagation delay.
    *   **Synchronous**: All flip-flops clocked simultaneously by the same signal. Faster and more common in modern designs.
    
    ### 4-Bit Counter Specifications:
    - **Modulus**: 16 (counts from 0 to 15, then wraps to 0)
    - **States**: 2^4 = 16 unique states
    - **Application Example**: A 1 MHz clock with this counter outputs pulses at 1MHz/16 = 62.5 kHz (frequency divider)
    
    **Real-World**: Your CPU uses counters extensively - the Program Counter (PC) register that tracks which instruction to execute next is essentially a massive counter!
    """
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u3_ex8_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 8: Counters", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u3_ex8", tutor_steps_config=tutor_config, tutor_context=st.session_state.u3_ex8_ctx)
