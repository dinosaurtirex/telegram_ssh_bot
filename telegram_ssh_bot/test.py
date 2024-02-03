import threading
import subprocess
import time

def execute_command():
    while True:
        command_to_execute = input('your_command_here: ')
        try:
            # Run the command in the console
            result = subprocess.run(command_to_execute, shell=True, capture_output=True, text=True)

            # Print the command output
            print(f"Command: {command_to_execute}\nOutput:\n{result.stdout}")
        except Exception as e:
            print(f"Error executing command: {e}")

def main():
    # Replace 'your_command_here' with the actual command you want to execute

    # Create a thread to execute the command continuously
    command_thread = threading.Thread(target=execute_command)
    
    # Start the thread
    command_thread.start()

    # Do other work in the main thread if needed

    # Since the command thread is running indefinitely, no need to join it in this case

if __name__ == "__main__":
    main()
