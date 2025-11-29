import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import io

def get_line_color(state):
    """Returns color based on logic state: Green for 1, Dark Grey for 0."""
    return '#22c55e' if state else '#475569'

def draw_logic_gate(gate_type, inputs, output_state):
    """
    Draws a simple logic gate representation using matplotlib.
    """
    fig, ax = plt.subplots(figsize=(8, 4), facecolor='none')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Gate symbol (simplified rectangle)
    gate_rect = patches.Rectangle((3.5, 2), 3, 2, fill=True, 
                               facecolor='#1e293b', edgecolor='#60a5fa', linewidth=2)
    ax.add_patch(gate_rect)
    
    # Gate label
    ax.text(5, 3, gate_type, ha='center', va='center', 
            fontsize=16, fontweight='bold', color='#60a5fa')
    
    # Input lines and labels
    if gate_type == 'NOT':
        color_in = get_line_color(inputs[0])
        ax.plot([1, 3.5], [3, 3], color=color_in, linewidth=3)
        ax.text(0.5, 3, f'A={inputs[0]}', ha='right', va='center', 
                fontsize=12, color='#e4e7eb', fontweight='bold')
    else:
        color_a = get_line_color(inputs[0])
        color_b = get_line_color(inputs[1])
        ax.plot([1, 3.5], [3.5, 3.5], color=color_a, linewidth=3)
        ax.plot([1, 3.5], [2.5, 2.5], color=color_b, linewidth=3)
        ax.text(0.5, 3.5, f'A={inputs[0]}', ha='right', va='center', 
                fontsize=12, color='#e4e7eb', fontweight='bold')
        ax.text(0.5, 2.5, f'B={inputs[1]}', ha='right', va='center', 
                fontsize=12, color='#e4e7eb', fontweight='bold')
    
    # Output line and label
    color_out = get_line_color(output_state)
    ax.plot([6.5, 9], [3, 3], color=color_out, linewidth=3)
    ax.text(9.5, 3, f'Out={output_state}', ha='left', va='center', 
            fontsize=12, color='#22c55e' if output_state else '#64748b', fontweight='bold')
    
    # Save to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True, facecolor='none', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

def draw_half_adder(a, b):
    """
    Draws a half adder circuit with dynamic coloring.
    """
    sum_val = a ^ b
    carry_val = a and b
    
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='none')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Colors
    c_a = get_line_color(a)
    c_b = get_line_color(b)
    c_sum = get_line_color(sum_val)
    c_carry = get_line_color(carry_val)
    
    # XOR gate for Sum
    xor_rect = patches.Rectangle((4, 4.5), 2.5, 1.5, fill=True, 
                              facecolor='#1e293b', edgecolor='#60a5fa', linewidth=2)
    ax.add_patch(xor_rect)
    ax.text(5.25, 5.25, 'XOR', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='#60a5fa')
    
    # AND gate for Carry
    and_rect = patches.Rectangle((4, 1.5), 2.5, 1.5, fill=True, 
                              facecolor='#1e293b', edgecolor='#a78bfa', linewidth=2)
    ax.add_patch(and_rect)
    ax.text(5.25, 2.25, 'AND', ha='center', va='center', 
            fontsize=12, fontweight='bold', color='#a78bfa')
    
    # Input A lines
    ax.plot([1, 4], [5.5, 5.5], color=c_a, linewidth=3) # To XOR
    ax.plot([2, 2], [5.5, 2.5], color=c_a, linewidth=2, linestyle='--') # Drop to AND
    ax.plot([2, 4], [2.5, 2.5], color=c_a, linewidth=3) # To AND
    ax.text(0.5, 5.5, f'A={a}', ha='right', va='center', fontsize=12, color='#e4e7eb', fontweight='bold')
    
    # Input B lines
    ax.plot([1, 4], [4.75, 4.75], color=c_b, linewidth=3) # To XOR
    ax.plot([2.5, 2.5], [4.75, 2], color=c_b, linewidth=2, linestyle='--') # Drop to AND
    ax.plot([2.5, 4], [2, 2], color=c_b, linewidth=3) # To AND
    ax.text(0.5, 4.75, f'B={b}', ha='right', va='center', fontsize=12, color='#e4e7eb', fontweight='bold')
    
    # Output Sum
    ax.plot([6.5, 10], [5.25, 5.25], color=c_sum, linewidth=3)
    ax.text(10.5, 5.25, f'Sum={sum_val}', ha='left', va='center', fontsize=12, color=c_sum, fontweight='bold')
    
    # Output Carry
    ax.plot([6.5, 10], [2.25, 2.25], color=c_carry, linewidth=3)
    ax.text(10.5, 2.25, f'Carry={carry_val}', ha='left', va='center', fontsize=12, color=c_carry, fontweight='bold')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True, facecolor='none', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

def draw_mux_4to1(d_inputs, select_lines):
    """
    Draws a 4:1 Multiplexer.
    d_inputs: list of 4 values (0/1)
    select_lines: list of 2 values [S1, S0]
    """
    s1, s0 = select_lines
    sel_idx = s1 * 2 + s0
    output_val = d_inputs[sel_idx]
    
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='none')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Mux Trapezoid
    verts = [(3, 1), (3, 7), (7, 6), (7, 2)]
    mux_poly = patches.Polygon(verts, closed=True, fill=True, 
                               facecolor='#1e293b', edgecolor='#f59e0b', linewidth=2)
    ax.add_patch(mux_poly)
    ax.text(5, 4, '4:1 MUX', ha='center', va='center', fontsize=14, fontweight='bold', color='#f59e0b')
    
    # Inputs D0-D3
    y_pos = [2.5, 3.8, 5.1, 6.4] # Positions for D0, D1, D2, D3 (bottom to top? usually D0 top)
    # Let's do D0 at top (6.4) to D3 at bottom (2.5) to match standard logic
    # Actually standard is often D0 top. Let's stick to D0 top.
    y_pos = [6.0, 5.0, 4.0, 3.0] 
    labels = ['D0', 'D1', 'D2', 'D3']
    
    for i in range(4):
        color = get_line_color(d_inputs[i])
        # Input line
        ax.plot([1, 3], [y_pos[i], y_pos[i]], color=color, linewidth=3)
        ax.text(0.5, y_pos[i], f'{labels[i]}={d_inputs[i]}', ha='right', va='center', 
                fontsize=12, color='#e4e7eb', fontweight='bold')
        
        # Internal connection (only if selected)
        if i == sel_idx:
            # Draw curve from input to output
            ax.plot([3, 7], [y_pos[i], 4], color=color, linewidth=2, linestyle=':')
            
    # Select Lines (Bottom)
    ax.plot([4.5, 4.5], [0.5, 1.5], color=get_line_color(s1), linewidth=2)
    ax.text(4.5, 0.2, f'S1={s1}', ha='center', va='center', fontsize=12, color='#e4e7eb')
    
    ax.plot([5.5, 5.5], [0.5, 1.5], color=get_line_color(s0), linewidth=2)
    ax.text(5.5, 0.2, f'S0={s0}', ha='center', va='center', fontsize=12, color='#e4e7eb')
    
    # Output
    c_out = get_line_color(output_val)
    ax.plot([7, 9], [4, 4], color=c_out, linewidth=3)
    ax.text(9.5, 4, f'Y={output_val}', ha='left', va='center', fontsize=14, color=c_out, fontweight='bold')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True, facecolor='none', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

def draw_seven_segment(value):
    """
    Draws a realistic 7-segment display using hexagonal polygons.
    value: int (0-9)
    """
    fig, ax = plt.subplots(figsize=(4, 6.5), facecolor='none')
    ax.set_xlim(-1, 13)
    ax.set_ylim(-1, 21)
    ax.axis('off')
    
    # Define hexagonal segments for a realistic look
    # Format: List of (x, y) tuples
    segments = {
        'a': [(2, 18), (3, 19), (9, 19), (10, 18), (9, 17), (3, 17)],
        'b': [(10, 18), (11, 17), (11, 10.5), (10, 9.5), (9, 10.5), (9, 17)],
        'c': [(10, 9.5), (11, 8.5), (11, 2), (10, 1), (9, 2), (9, 8.5)],
        'd': [(10, 1), (9, 0), (3, 0), (2, 1), (3, 2), (9, 2)],
        'e': [(2, 9.5), (3, 8.5), (3, 2), (2, 1), (1, 2), (1, 8.5)],
        'f': [(2, 18), (3, 17), (3, 10.5), (2, 9.5), (1, 10.5), (1, 17)],
        'g': [(2, 9.5), (3, 10.5), (9, 10.5), (10, 9.5), (9, 8.5), (3, 8.5)]
    }
    
    # Map digits to segments
    digit_map = {
        0: ['a', 'b', 'c', 'd', 'e', 'f'],
        1: ['b', 'c'],
        2: ['a', 'b', 'g', 'e', 'd'],
        3: ['a', 'b', 'g', 'c', 'd'],
        4: ['f', 'g', 'b', 'c'],
        5: ['a', 'f', 'g', 'c', 'd'],
        6: ['a', 'f', 'e', 'd', 'c', 'g'],
        7: ['a', 'b', 'c'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }
    
    active_segments = digit_map.get(value, [])
    
    for seg_name, verts in segments.items():
        if seg_name in active_segments:
            color = '#ef4444' # Red LED
            alpha = 1.0
            lw = 0
        else:
            color = '#1e293b' # Off state
            alpha = 0.2
            lw = 1
            
        poly = patches.Polygon(verts, closed=True, facecolor=color, edgecolor=color, alpha=alpha, linewidth=lw)
        ax.add_patch(poly)
        
    # Add invisible point to force bbox to include top area
    ax.plot([6], [20.5], color='none')
        
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1, transparent=True, facecolor='none', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

def draw_flip_flop(ff_type, inputs, q, q_bar, clk_state=0):
    """
    Draws a Flip-Flop (SR, JK, D, T).
    inputs: dict of input values e.g. {'J': 1, 'K': 0}
    """
    fig, ax = plt.subplots(figsize=(6, 5), facecolor='none')
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Main Block
    rect = patches.Rectangle((2.5, 1), 3, 4, fill=True, 
                             facecolor='#1e293b', edgecolor='#a78bfa', linewidth=2)
    ax.add_patch(rect)
    
    # Title
    ax.text(4, 3, f'{ff_type} FF', ha='center', va='center', fontsize=14, fontweight='bold', color='#a78bfa')
    
    # Inputs
    y_positions = {'S': 4, 'R': 2, 'J': 4, 'K': 2, 'D': 4, 'T': 4}
    
    for name, val in inputs.items():
        y = y_positions.get(name, 3)
        color = get_line_color(val)
        ax.plot([1, 2.5], [y, y], color=color, linewidth=3)
        ax.text(0.5, y, f'{name}={val}', ha='right', va='center', fontsize=12, color='#e4e7eb')
        
    # Clock
    ax.plot([1, 2.5], [3, 3], color=get_line_color(clk_state), linewidth=2)
    # Clock triangle
    ax.plot([2.5, 2.8], [3.2, 3], color='#a78bfa', linewidth=2)
    ax.plot([2.5, 2.8], [2.8, 3], color='#a78bfa', linewidth=2)
    ax.text(0.5, 3, f'CLK={clk_state}', ha='right', va='center', fontsize=12, color='#e4e7eb')

    # Outputs
    c_q = get_line_color(q)
    c_qb = get_line_color(q_bar)
    
    ax.plot([5.5, 7], [4, 4], color=c_q, linewidth=3)
    ax.text(7.5, 4, f'Q={q}', ha='left', va='center', fontsize=12, color=c_q, fontweight='bold')
    
    ax.plot([5.5, 7], [2, 2], color=c_qb, linewidth=3)
    ax.text(7.5, 2, f'Q\'={q_bar}', ha='left', va='center', fontsize=12, color=c_qb, fontweight='bold')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True, facecolor='none', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

def draw_generic_block(title, input_labels, output_labels, active_inputs=None, active_outputs=None):
    """
    Draws a generic block diagram (for FSM, PLA, FPGA).
    """
    if active_inputs is None: active_inputs = {}
    if active_outputs is None: active_outputs = {}
    
    fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Block
    rect = patches.Rectangle((3, 1), 4, 4, fill=True, 
                             facecolor='#1e293b', edgecolor='#60a5fa', linewidth=2)
    ax.add_patch(rect)
    ax.text(5, 3, title, ha='center', va='center', fontsize=12, fontweight='bold', color='#60a5fa', wrap=True)
    
    # Inputs
    dy = 4 / (len(input_labels) + 1)
    for i, label in enumerate(input_labels):
        y = 5 - (i + 1) * dy
        val = active_inputs.get(label, 0)
        color = get_line_color(val)
        ax.plot([1.5, 3], [y, y], color=color, linewidth=3)
        ax.text(1.2, y, label, ha='right', va='center', fontsize=10, color='#e4e7eb')
        
    # Outputs
    dy = 4 / (len(output_labels) + 1)
    for i, label in enumerate(output_labels):
        y = 5 - (i + 1) * dy
        val = active_outputs.get(label, 0)
        color = get_line_color(val)
        ax.plot([7, 8.5], [y, y], color=color, linewidth=3)
        ax.text(8.8, y, label, ha='left', va='center', fontsize=10, color='#e4e7eb')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True, facecolor='none', dpi=100)
    buf.seek(0)
    plt.close(fig)
    return buf

