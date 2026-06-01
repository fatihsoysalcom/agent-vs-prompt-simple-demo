import time

# --- Demonstrating Prompt-Based Interaction ---
# A prompt is a single, direct instruction given to a system.
# The system processes it once and provides a response, without maintaining
# continuous state, making autonomous decisions, or adapting over time.
def execute_prompt(instruction):
    print(f"\n[Prompt System] Received instruction: '{instruction}'")
    # The 'system' simply processes the instruction directly.
    if "clean" in instruction.lower():
        return "[Prompt System] Task completed: The room is now clean (prompt-based action)."
    elif "status" in instruction.lower():
        return "[Prompt System] Current status: Unknown (prompt systems don't maintain continuous environment state)."
    else:
        return "[Prompt System] Instruction processed (prompt-based response)."

# --- Demonstrating Agent-Based Interaction ---
# An agent is an autonomous entity that perceives its environment,
# makes decisions based on its goals and perceptions, and takes actions
# over time, often in continuous cycles.

class Room:
    """Represents the environment for our agent."""
    def __init__(self):
        self.is_dirty = False # Initial state of the environment

    def make_dirty(self):
        self.is_dirty = True
        print("\n[Environment] Room became dirty (external event).")

    def __str__(self):
        return f"[Environment] Room state: {'Dirty' if self.is_dirty else 'Clean'}"

class CleaningAgent:
    """A simple agent designed to keep the room clean."""
    def __init__(self, name="CleanerBot", goal="keep room clean"):
        self.name = name
        self.goal = goal
        print(f"\n[{self.name}] Initialized with goal: '{self.goal}'.")

    def perceive(self, room):
        """Agent perceives its environment."""
        perception = {"room_is_dirty": room.is_dirty}
        print(f"  [{self.name}] Perceives: Room is {'dirty' if room.is_dirty else 'clean'}.")
        return perception

    def decide(self, perception):
        """Agent makes a decision based on perception and its goal."""
        if perception["room_is_dirty"]:
            print(f"  [{self.name}] Decides: Room is dirty, need to clean to achieve goal.")
            return "clean"
        else:
            print(f"  [{self.name}] Decides: Room is clean, no action needed.")
            return "idle"

    def act(self, room, decision):
        """Agent takes action based on its decision."""
        if decision == "clean":
            room.is_dirty = False # Agent modifies the environment
            print(f"  [{self.name}] Acts: Cleaning the room.")
        elif decision == "idle":
            print(f"  [{self.name}] Acts: Staying idle.")
        else:
            print(f"  [{self.name}] Acts: Unknown decision '{decision}'.")

    def run_cycle(self, room):
        """An agent continuously runs cycles of perceive-decide-act."""
        print(f"\n--- [{self.name}] Cycle Start ---")
        perception = self.perceive(room)
        decision = self.decide(perception)
        self.act(room, decision)
        print(f"--- [{self.name}] Cycle End ---")

# --- Demonstration Execution ---
if __name__ == "__main__":
    print("==========================================")
    print("  Demonstrating Prompt vs. Agent Concept  ")
    print("==========================================")

    # --- Prompt-Based Demonstration ---
    print("\n--- Prompt-Based Interaction ---")
    # Each prompt is a new, isolated instruction.
    print(execute_prompt("Please clean the living room."))
    print(execute_prompt("What is the current temperature?"))
    print(execute_prompt("Report room status.")) # Prompt system cannot give a meaningful status without continuous perception

    # --- Agent-Based Demonstration ---
    print("\n--- Agent-Based Interaction ---")
    my_room = Room()
    cleaner_agent = CleaningAgent()

    # Initial state: Room is clean
    print(f"\n{my_room}")
    cleaner_agent.run_cycle(my_room) # Agent perceives clean, decides idle
    print(f"\n{my_room}")

    # External event: Room becomes dirty
    my_room.make_dirty()
    print(f"\n{my_room}")
    cleaner_agent.run_cycle(my_room) # Agent perceives dirty, decides clean, acts
    print(f"\n{my_room}")

    # Room is now clean again, agent should remain idle
    cleaner_agent.run_cycle(my_room) # Agent perceives clean, decides idle
    print(f"\n{my_room}")

    # Another external event: Room becomes dirty
    my_room.make_dirty()
    print(f"\n{my_room}")
    cleaner_agent.run_cycle(my_room) # Agent perceives dirty, decides clean, acts
    print(f"\n{my_room}")

    print("\n==========================================")
    print("  Agent demonstrates continuous, autonomous, goal-seeking behavior.")
    print("  Prompt is a one-off instruction without autonomy or state.")
    print("==========================================")
