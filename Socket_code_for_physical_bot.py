import socket
import time  # For adding delay between movements
import csv
import pandas as pd
def read_excel_to_list(file_name, sheet_name):
    """
    Reads an Excel file from the specified sheet and converts each row into a list.
    The entire data will be returned as a list of lists.

    :param file_name: Name of the Excel file to read
    :param sheet_name: Name of the sheet to read
    :return: A list of lists containing the data from the specified sheet
    """
    try:
        # Read the specified sheet from the Excel file into a DataFrame
        df = pd.read_excel(file_name, sheet_name=sheet_name)

        # Convert DataFrame to list of lists
        data = df.values.tolist()  # Convert DataFrame values into a list of lists

        print(f"Data successfully read from sheet '{sheet_name}' in {file_name}")
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
def send_tcp_packet(server_ip, server_port, message):
    """
    Sends a TCP packet to the robot with the given message.
    """
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")

        # Send the message
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        # Optionally receive a response (if server sends one)
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {response}")

    except socket.error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    # Server details
    SERVER_IP = "192.168.1.159"  # Replace with your robot's server IP
    SERVER_PORT = 5001  # Replace with your robot's server port
    SPEED = 500  # Speed for the movements

    # Define the CSV file path here
    file_path = "E:/RASLAB/PROJECT_RUN_THROUGH/Project_parameters_file.xlsx"
    angles = read_excel_to_list(file_path, "Joint_Angles")
    #angles = read_excel_to_list(file_path,"Initial_joint")
    #print(angles)
    DELAY = 2.0  # Delay between movements in seconds#send_tcp_packet(SERVER_IP, SERVER_PORT, message)

    try:
        print(f"\n MOVING TO - ")
        i = 1
        for angle in angles:
            angle.append(SPEED)
            
            message = f"set_angles{angle[0],angle[1], angle[2], angle[3], angle[4], angle[5], angle[6]}"
            print (f"Point {i}" )
            #send_tcp_packet(SERVER_IP, SERVER_PORT, message)
            time.sleep(DELAY)
            i=i+1
        print("\n Motion completed!")

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")