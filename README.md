**Title**

*Python Caesar Cipher*

**Description**

This Python program implements the Caesar Cipher algorithm, a classic technique for shifting letters in a message for basic encryption and decryption. Users can input a message and a shift value to perform these operations.

**Caesar Cipher**

The Caesar Cipher is a simple yet historical encryption method that shifts each letter in a message by a certain number of positions (the shift value) along the alphabet. For instance, with a shift value of 3, "hello" becomes "khoor." While a valuable learning tool for cryptography concepts, Caesar Cipher is not secure for real-world use due to its ease of decryption.

**How to Use**

1. Save this code as a Python file (e.g., `caesar_cipher.py`).
2. Run the script from your terminal:

   ```bash
   python caesar_cipher.py
   ```

3. The program will prompt you to enter a message and a shift value. Enter your desired values and press Enter.
4. The program will display the encrypted or decrypted message based on your selection.

**Example Usage**

```
Enter the message: hello world
Enter the shift value: 3
Encrypted message: khoor zruog

Enter the message: khoor zruog
Enter the shift value: -3
Decrypted message: hello world
```

**Disclaimer**

The Caesar Cipher is a weak encryption method and should not be used for sensitive information. Modern encryption techniques offer much stronger security guarantees.

**License**

This project is licensed under the MIT License.

**Feel free to use this code for educational purposes!**

**Additional Notes**

* This implementation handles uppercase and lowercase letters appropriately.
* It preserves non-alphabetic characters in the message.