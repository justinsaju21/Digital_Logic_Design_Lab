import streamlit as st
import time

class SmartTutor:
    def __init__(self):
        if 'tutor_state' not in st.session_state:
            st.session_state.tutor_state = {}
        if 'tutor_progress' not in st.session_state:
            st.session_state.tutor_progress = {}

    def set_current_step(self, unit_id, step_index):
        st.session_state.tutor_state[unit_id] = step_index

    def get_current_step(self, unit_id):
        return st.session_state.tutor_state.get(unit_id, 0)

    def reset_progress(self, unit_id):
        if unit_id in st.session_state.tutor_state:
            del st.session_state.tutor_state[unit_id]

    def mark_step_complete(self, unit_id):
        current_step_idx = self.get_current_step(unit_id)
        self.set_current_step(unit_id, current_step_idx + 1)

    def mark_completed(self, unit_name, experiment_name):
        # Legacy method, kept for compatibility if needed
        key = f"{unit_name}_{experiment_name}"
        if not st.session_state.tutor_progress.get(key):
            st.session_state.tutor_progress[key] = True
            st.balloons()
            st.success(f"🎉 Experiment '{experiment_name}' Completed!")

    def guide(self, unit_id, steps_config, current_state_context):
        """
        Advanced Guide Method with Focus Mode.
        """
        current_step_idx = self.get_current_step(unit_id)
        total_steps = len(steps_config)
        
        # Progress Bar with Faculty Tone
        progress = min(current_step_idx / total_steps, 1.0)
        st.markdown(f"**Lab Progress**: {int(progress * 100)}%")
        st.progress(progress)
        
        # Completion State
        if current_step_idx >= total_steps:
            st.success("🎉 **Experiment Completed Successfully!**")
            st.markdown("""
            > *"Excellent work, student. You have verified all the logic gates as per the syllabus. 
            > Please proceed to the next experiment or review your observations."*
            > — **Prof. Antigravity**
            """)
            if st.button("Reset Experiment"):
                self.reset_progress(unit_id)
                st.rerun()
            return

        # Active Step Focus
        step = steps_config[current_step_idx]
        
        # Faculty Persona: Objective & Procedure
        st.markdown(f"### 📝 Step {current_step_idx + 1}: {step['title']}")
        
        with st.container():
            st.info(f"**Procedure**: {step['instruction']}")
            
            if "hint" in step:
                with st.expander("💡 Need a Hint?"):
                    st.write(step["hint"])

        # Dynamic Validation
        is_correct = False
        if "criteria" in step:
            try:
                is_correct = step["criteria"](current_state_context)
            except Exception as e:
                # st.error(f"Validation Error: {e}")
                pass

        # Feedback & Navigation
        if is_correct:
            st.markdown("---")
            st.markdown(f"### ✅ **Observation Verified**")
            st.success(step.get("success_msg", "Correct! Proceeding to next step..."))
            
            # Auto-advance or Manual Next
            if st.button("Next Step ➡️", key=f"next_{unit_id}_{current_step_idx}", type="primary"):
                self.mark_step_complete(unit_id)
                st.balloons() # Animation as requested
                st.rerun()
        else:
            st.markdown("---")
            st.caption("🔴 *Pending Verification... Perform the action above.*")

    def render_right_panel(self, steps, current_step_index):
        """
        Legacy method for backward compatibility.
        """
        st.warning("⚠️ This experiment is using the legacy syllabus. Please update to the new curriculum.")
        # Create a dummy config for legacy steps
        dummy_config = []
        for i, s in enumerate(steps):
            dummy_config.append({
                "title": s,
                "instruction": s,
                "criteria": lambda c: i < current_step_index # Hacky way to check progress
            })
        
        # We can't easily map legacy state to new state without refactoring the experiment.
        # So we just render the old list for now if we can't use guide.
        
        st.markdown("### 🤖 Smart Tutor (Legacy Mode)")
        total_steps = len(steps)
        if total_steps > 0:
            progress = min(current_step_index / total_steps, 1.0)
        else:
            progress = 0
        st.progress(progress)
        
        for i, step in enumerate(steps):
            if i < current_step_index:
                st.markdown(f"✅ ~~{step}~~")
            elif i == current_step_index:
                st.markdown(f"👉 **{step}**")
            else:
                st.markdown(f"⬜ {step}")

    def check_truth_table(self, user_func, truth_table_inputs, expected_outputs):
        pass
