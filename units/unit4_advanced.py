import streamlit as st
import graphviz
from utils import render_experiment_layout, render_circuit_image
from tutor import SmartTutor
from circuits import draw_generic_block

def render():
    st.title("Unit 4: Advanced Logic")
    
    tutor = SmartTutor()
    
    tab1, tab2 = st.tabs(["Ex 9: FSM Design", "Ex 10: Vending Machine"])
    
    with tab1:
        run_experiment_9(tutor)
    with tab2:
        run_experiment_10(tutor)

def run_experiment_9(tutor):
    # Advanced Tutor Configuration for FSM
    tutor_config = [
        {
            "title": "Initialize FSM",
            "instruction": "Click **Reset** to ensure the Sequence Detector is in the starting state (State A).",
            "criteria": lambda c: c.get('current_state') == 'A',
            "success_msg": "✓ FSM Reset. We are ready to detect the sequence '101'."
        },
        {
            "title": "Understanding the Goal",
            "instruction": "We want to detect the sequence **1-0-1**. This requires memory of the past 2 bits. State A means 'Start/Reset'.",
            "criteria": lambda c: c.get('current_state') == 'A',
            "success_msg": "✓ Goal understood. Let's start the sequence.",
        },
        {
            "title": "Step 1: Input First Bit '1'",
            "instruction": "Set **Input X = 1** and click **Clock Pulse**. We need to detect the first '1'.",
            "criteria": lambda c: c.get('current_state') == 'B',
            "success_msg": "✓ State B reached! The FSM has 'remembered' the first 1.",
            "hint": "State B represents 'Have seen 1'."
        },
        {
            "title": "Verify State B Meaning",
            "instruction": "Observe the diagram. State B means we have the prefix '1'. If we get a '0' next, we progress. If we get '1', we stay in B (still have a '1').",
            "criteria": lambda c: c.get('current_state') == 'B',
            "success_msg": "✓ State logic confirmed.",
        },
        {
            "title": "Step 2: Input Second Bit '0'",
            "instruction": "Set **Input X = 0** and click **Clock Pulse**. We are looking for '10'.",
            "criteria": lambda c: c.get('current_state') == 'C',
            "success_msg": "✓ State C reached! The FSM has now seen '10'.",
            "hint": "State C represents 'Have seen 10'."
        },
        {
            "title": "Verify State C Meaning",
            "instruction": "State C means we are one bit away from success. If we get '1', we finish '101'. If we get '0', we break the sequence (100... start over).",
            "criteria": lambda c: c.get('current_state') == 'C',
            "success_msg": "✓ Critical moment reached.",
        },
        {
            "title": "Step 3: Input Third Bit '1' (Success)",
            "instruction": "Set **Input X = 1** and click **Clock Pulse**. This completes '101'. Watch Output Z!",
            "criteria": lambda c: c.get('last_output') == 1,
            "success_msg": "🎉 SEQUENCE DETECTED! Output Z went HIGH (1). The FSM recognized '101'.",
        },
        {
            "title": "Observe Overlap Handling",
            "instruction": "Notice the FSM went back to **State B**, not A. Why? Because the last '1' of '101' can also be the *start* of a new '101' sequence.",
            "criteria": lambda c: c.get('current_state') == 'B',
            "success_msg": "✓ Overlap logic verified. This is a key feature of this Mealy machine.",
        },
        {
            "title": "Test Broken Sequence",
            "instruction": "Reset (State A). Try entering **0**. The state should stay at A because '0' cannot start '101'.",
            "criteria": lambda c: c.get('current_state') == 'A' and c.get('last_input') == 0 and c.get('clocked'),
            "success_msg": "✓ Correct. '0' is ignored at the start.",
        },
        {
            "title": "Final Challenge: Detect '101' Again",
            "instruction": "Enter the full sequence **1 → 0 → 1** again to confirm reliable operation.",
            "criteria": lambda c: c.get('last_output') == 1,
            "success_msg": "✓ Mastery achieved! You've successfully implemented and tested a Sequence Detector FSM.",
        }
    ]

    if 'u4_ex9_state' not in st.session_state:
        st.session_state.u4_ex9_state = 'A'
    if 'u4_ex9_clocked' not in st.session_state:
        st.session_state.u4_ex9_clocked = False
    if 'u4_ex9_last_in' not in st.session_state:
        st.session_state.u4_ex9_last_in = 0
    
    def simulation():
        st.markdown("### 🕵️ Sequence Detector (Mealy Machine)")
        st.markdown("Detects the overlapping sequence **'101'**.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("#### Controls")
            input_x = st.radio("Input X", [0, 1], horizontal=True, key="u4_ex9_x")
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("Clock Pulse 🟢"):
                    # State Transition Logic for '101' Detector
                    curr = st.session_state.u4_ex9_state
                    next_s = curr
                    out_z = 0
                    
                    if curr == 'A':
                        if input_x == 1: next_s = 'B'; out_z = 0
                        else: next_s = 'A'; out_z = 0
                    elif curr == 'B':
                        if input_x == 0: next_s = 'C'; out_z = 0
                        else: next_s = 'B'; out_z = 0
                    elif curr == 'C':
                        if input_x == 1: next_s = 'B'; out_z = 1 # Sequence Detected!
                        else: next_s = 'A'; out_z = 0
                        
                    st.session_state.u4_ex9_state = next_s
                    st.session_state.u4_ex9_last_out = out_z
                    st.session_state.u4_ex9_clocked = True
                    st.session_state.u4_ex9_last_in = input_x
                    
                    if out_z == 1:
                        st.success(f"🚨 SEQUENCE DETECTED! Output Z = 1")
                    else:
                        st.info(f"Clocked. State: {curr} → {next_s}")
                    
            with c2:
                if st.button("Reset 🔴"):
                    st.session_state.u4_ex9_state = 'A'
                    st.session_state.u4_ex9_last_out = 0
                    st.session_state.u4_ex9_clocked = False
                    st.rerun()

            st.metric("Current State", st.session_state.u4_ex9_state)
            
            # Preview Mealy Output (depends on current state AND input)
            preview_out = 0
            if st.session_state.u4_ex9_state == 'C' and input_x == 1:
                preview_out = 1
            st.metric("Output Z (Next Pulse)", preview_out)

        with col2:
            # Visualization using Graphviz
            import graphviz
            dot = graphviz.Digraph()
            dot.attr(rankdir='LR')
            
            # Define States
            states = ['A', 'B', 'C']
            for s in states:
                if s == st.session_state.u4_ex9_state:
                    dot.node(s, s, style='filled', fillcolor='#60a5fa', fontcolor='white')
                else:
                    dot.node(s, s)
            
            # Define Transitions (Label: X/Z)
            dot.edge('A', 'A', label='0/0')
            dot.edge('A', 'B', label='1/0')
            dot.edge('B', 'B', label='1/0')
            dot.edge('B', 'C', label='0/0')
            dot.edge('C', 'A', label='0/0')
            dot.edge('C', 'B', label='1/1', color='green' if st.session_state.u4_ex9_state == 'C' and input_x == 1 else 'black')
            
            st.graphviz_chart(dot)

        return {
            "current_state": st.session_state.u4_ex9_state,
            "last_output": st.session_state.get('u4_ex9_last_out', 0),
            "clocked": st.session_state.u4_ex9_clocked,
            "last_input": st.session_state.u4_ex9_last_in
        }

    theory = """
    ### Finite State Machines (FSM)
    
    **Definition**: A computational model used to design sequential logic circuits. An FSM consists of a finite number of states, transitions, and outputs.
    
    **Two Main Architectures:**
    
    1.  **Mealy Machine**:
        -   **Output depends on**: Current State AND Current Input.
        -   **Characteristics**: Output can change *asynchronously* in response to input changes.
        -   **Advantage**: Often requires fewer states.
        -   **Diagram**: Output is written on the *transition edge* (e.g., 1/0).
        
    2.  **Moore Machine**:
        -   **Output depends on**: Current State ONLY.
        -   **Characteristics**: Output is synchronous with the state.
        -   **Advantage**: Safer, glitch-free outputs.
        -   **Diagram**: Output is written inside the *state bubble* (e.g., State A / Out=0).
        
    **Sequence Detector Design:**
    -   To detect '101', we need states to track progress:
    -   **State A**: Reset (seen nothing)
    -   **State B**: Seen '1'
    -   **State C**: Seen '10'
    -   **Transition**: If in C and input is 1 → Sequence '101' found! Output 1.
    """
    
    if 'u4_ex9_ctx' not in st.session_state: st.session_state.u4_ex9_ctx = {}
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u4_ex9_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 9: Sequence Detector (FSM)", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u4_ex9", tutor_steps_config=tutor_config, tutor_context=st.session_state.u4_ex9_ctx)

def run_experiment_10(tutor):
    # Advanced Tutor for Vending Machine
    tutor_config = [
        {
            "title": "Initialize System",
            "instruction": "Ensure the balance is **0¢**. If not, click **Reset**.",
            "criteria": lambda c: c.get('balance') == 0,
            "success_msg": "✓ System ready. Price is 15¢."
        },
        {
            "title": "Insert First Coin (Nickel)",
            "instruction": "Insert a **Nickel (5¢)**. The state should update to '5¢'.",
            "criteria": lambda c: c.get('balance') == 5,
            "success_msg": "✓ Coin accepted. Balance: 5¢. We need 10¢ more.",
        },
        {
            "title": "Insert Second Coin (Nickel)",
            "instruction": "Insert another **Nickel (5¢)**. Total should be 10¢.",
            "criteria": lambda c: c.get('balance') == 10,
            "success_msg": "✓ Balance: 10¢. Almost there!",
        },
        {
            "title": "Complete Purchase (Nickel)",
            "instruction": "Insert a third **Nickel (5¢)** to reach 15¢. The item should dispense.",
            "criteria": lambda c: c.get('dispensed') == True,
            "success_msg": "✓ 15¢ reached! Item dispensed.",
        },
        {
            "title": "Reset for Next Test",
            "instruction": "Click **Reset** to clear the machine for a new transaction.",
            "criteria": lambda c: c.get('balance') == 0 and not c.get('dispensed'),
            "success_msg": "✓ Machine reset.",
        },
        {
            "title": "Test Dime Path",
            "instruction": "Insert a **Dime (10¢)**. Balance should jump straight to 10¢.",
            "criteria": lambda c: c.get('balance') == 10,
            "success_msg": "✓ Dime accepted. Balance: 10¢.",
        },
        {
            "title": "Complete with Nickel",
            "instruction": "Insert a **Nickel (5¢)** to reach 15¢.",
            "criteria": lambda c: c.get('dispensed') == True,
            "success_msg": "✓ Transaction complete (10 + 5 = 15).",
        },
        {
            "title": "Reset Again",
            "instruction": "Click **Reset**.",
            "criteria": lambda c: c.get('balance') == 0,
            "success_msg": "✓ Ready for final test.",
        },
        {
            "title": "Test Overpayment (Dime + Dime)",
            "instruction": "Insert a **Dime (10¢)**, then another **Dime (10¢)**. Total 20¢. Should dispense (and ideally return change, but for this FSM we just dispense).",
            "criteria": lambda c: c.get('dispensed') == True,
            "success_msg": "✓ 20¢ >= 15¢. Item dispensed!",
        },
        {
            "title": "Final Challenge: State Diagram Analysis",
            "instruction": "Observe the graph. Notice how '15¢' is the accepting state. This is a Moore Machine because output depends only on state.",
            "criteria": lambda c: True,
            "success_msg": "🎉 EXPERIMENT COMPLETE! You've designed a sequential controller.",
        }
    ]

    if 'u4_ex10_bal' not in st.session_state: st.session_state.u4_ex10_bal = 0
    if 'u4_ex10_disp' not in st.session_state: st.session_state.u4_ex10_disp = False

    def simulation():
        st.markdown("### 🥤 Vending Machine Controller")
        st.markdown("Price: **15¢**. Accepts Nickels (5¢) and Dimes (10¢).")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.metric("Current Balance", f"{st.session_state.u4_ex10_bal}¢")
            
            if st.button("Insert Nickel (5¢)"):
                st.session_state.u4_ex10_bal += 5
            
            if st.button("Insert Dime (10¢)"):
                st.session_state.u4_ex10_bal += 10
                
            if st.button("Reset / Return Coins"):
                st.session_state.u4_ex10_bal = 0
                st.session_state.u4_ex10_disp = False
                
            # Logic
            if st.session_state.u4_ex10_bal >= 15:
                st.session_state.u4_ex10_disp = True
                # IMPORTANT: Do NOT auto-reset balance immediately, or tutor misses the state!
                # Let user reset manually or have a delay (simulated by requiring reset step)
                st.success("🍬 Item Dispensed!")
            else:
                st.session_state.u4_ex10_disp = False
                
        with col2:
            # State Diagram
            import graphviz
            dot = graphviz.Digraph()
            dot.attr(rankdir='LR')
            
            bal = st.session_state.u4_ex10_bal
            # States: 0, 5, 10, 15(Dispense)
            
            node_color = '#ec4899'
            
            # Map balance to nearest state for visualization
            vis_bal = bal
            if bal >= 15: vis_bal = 15
            
            dot.node('0', '0¢', style='filled' if vis_bal==0 else '', fillcolor=node_color)
            dot.node('5', '5¢', style='filled' if vis_bal==5 else '', fillcolor=node_color)
            dot.node('10', '10¢', style='filled' if vis_bal==10 else '', fillcolor=node_color)
            dot.node('15', 'Dispense', style='filled' if vis_bal==15 else '', fillcolor='#22c55e')
            
            dot.edge('0', '5', label='N')
            dot.edge('0', '10', label='D')
            dot.edge('5', '10', label='N')
            dot.edge('5', '15', label='D')
            dot.edge('10', '15', label='N/D')
            
            st.graphviz_chart(dot)
            
        return {
            "balance": st.session_state.u4_ex10_bal,
            "dispensed": st.session_state.u4_ex10_disp
        }

    theory = """
    ### State Machine Design
    This Vending Machine is a **Moore Machine** where the output (Dispense) depends only on the state (Balance >= 15).
    """
    
    if 'u4_ex10_ctx' not in st.session_state: st.session_state.u4_ex10_ctx = {}
    
    def wrapped_sim():
        ctx = simulation()
        st.session_state.u4_ex10_ctx = ctx
        return ctx

    render_experiment_layout("Experiment 10: Vending Machine", theory, wrapped_sim, tutor, 
                             tutor_unit_id="u4_ex10", tutor_steps_config=tutor_config, tutor_context=st.session_state.u4_ex10_ctx)
