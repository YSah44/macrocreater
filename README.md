![GitHub language count](https://img.shields.io/github/languages/count/YavuzSahbaz/macrocreater)
![GitHub repo size](https://img.shields.io/github/repo-size/YavuzSahbaz/macrocreater)
![Lines of code](https://img.shields.io/tokei/lines/github/YavuzSahbaz/macrocreater)
![GitHub](https://img.shields.io/github/license/YavuzSahbaz/macrocreater)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/YavuzSahbaz/macrocreater)

# YSSHellVBA Help Page macrocreater

 Reverse Shell Base64 PowerShell Payload Generator for Office Documents and Macros

This is a reverse shell payload generator written in Python by Y S. It generates a PowerShell base64 encoded command-line payload that connects to a specified IP address and port.

## Usage

Run the program with the following command:

- `python3 ysshellvba.py`

The script will ask for the following inputs:

IP address: Enter the IP address where you want the reverse shell to connect.
Port number: Enter the port number on which you want the reverse shell to connect.
The script will then create a file named "payload.txt" containing the PowerShell command line payload, which can be embedded in Office documents or macros.

At the end, the script will ask if you want to print the content of "payload.txt". If you choose to print the content, it will display the content in the console.

To use the generated payload, embed it in an Office document or macro, and execute the document or macro on the target system. The target system will initiate a reverse shell connection to the specified IP and port.


![Dog playing with ball](https://github.com/YavuzSahbaz/macrocreater/blob/main/ysshellvba.gif)


## Requirements

Python 3 
Please note that using reverse shells in Office documents and macros can have legal and ethical implications. Use this script only for legitimate purposes and with proper authorization. Be aware of the potential risks and ensure you have appropriate permissions before using this tool.


## License

This program is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

