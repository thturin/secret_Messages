"""Secret Nessages

Hacks and Tweaks
    find another algorithm to swap the neighboring letters!
        use a bubble sort method to swap instead of putt even and odd letters into lists and separate functions
    add a reverse feature to the swapping function
"""
from tkinter import messagebox, simpledialog, Tk

#encrypt or decrypt
def get_task():
    task  = simpledialog.askstring('Task','Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message','Enter the secret message: ')
    return message

def is_even(number):
    return number % 2 == 0 # this will return true is number is even

def bubble_swap(message):
    if not is_even(len(message)):
        message = message + 'x'
    letter_list=list(message)
    for counter in range(0,len(message),2): # 3rd argument tells the loop the incremement by 2, default is 1
        temp = letter_list[counter]
        letter_list[counter]=letter_list[counter+1]
        letter_list[counter+1]=temp
    new_message = ''.join(letter_list)
    return new_message

def get_even_letters(message):
    even_letters=[]
    for counter in range (0,len(message)):
        if is_even(counter): #if the counter is an even number
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters=[]
    for counter in range(0,len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)): # checking to see if the message has an even number or odd number of letters, if odd, then ad an x to make even
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0,int(len(message)/2)): #loop through the list of odd and even letter lists, you only need ot loop half ofg the leng of the message
        letter_list.append(odd_letters[counter]) #put odd letter before even for the swapp ing
        letter_list.append(even_letters[counter])
    #print(letter_list)
    new_message = ''.join(letter_list)
    return new_message


root = Tk() # create Tkinter window
root.withdraw() # removes window

while True:
    task = get_task()

    if task == 'encrypt':
        message = get_message()
        #messagebox.showinfo('Message to encrypt is: ', message)
        encrypted = bubble_swap(message) #swap_letters(message)
        messagebox.showinfo('Cyphertext of the secret message is: ', encrypted)
        break
    elif task == 'decrypt':
        message = get_message()
        #messagebox.showinfo('Message to decrypt is: ', message)
        decrypted = bubble_swap(message)#swap_letters(message)
        messagebox.showinfo('Plaintext of the message is: ', decrypted)
        break
    else:
        messagebox.showinfo('Error','Please try again')

root.mainloop()

