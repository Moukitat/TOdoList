import sqlite3
import tkinter as tk

from tkinter import messagebox
from tkinter.tix import NoteBook

conn=sqlite3.connect("todolist.db")
cursor=conn.cursor()

#My duties
def add_duties(titre,description='', date_echeance=None):
    cursor.execute(""" 
    INSERT INTO todolist(titre,description,date_echeance) values (?,?,?) """,(titre,description,date_echeance))
    conn.commit()
    messagebox.showinfo("duties ajouter avec succes!")

def list_duties():
    cursor.execute("select * from todolist")
    duties=cursor.fetchall()
    for duty in duties:
        messagebox.showinfo(f" ID: {duty[0]},titre:{duty[1]},Statut:{duty[2]},description:{duty[3]},date_echeance{duty[4]}")


def update_duties(id,new_titre=None,new_description=None):
    if new_titre:
        cursor.execute("update todolist set titre= ? where id=?",(id,new_titre))
    if new_description:
        cursor.execute("update todolist set description=? where id =?", (id,new_description))
    conn.commit()
    messagebox.showinfo("Successful update!")

def delete_duties(id):
        cursor.execute("delete from todolist where id=? ", (id,))
        conn.commit()
        messagebox.showinfo("duties Successfully delete!")


def completed_duties(id):
    cursor.execute("update from todolist set statut='completed' where id = ? ",(id))
    conn.commit()
    messagebox.showinfo(tk.END,"duties marked as completed!")

#My Projets



def add_projet(titre, description='', date_echeance=None):
        cursor.execute(""" 
        INSERT INTO todolist(titre,description,date_echeance) values (?,?,?) """, (titre, description, date_echeance))
        conn.commit()
        messagebox.showinfo("projet ajouter avec succes!")

def list_projet():
        cursor.execute("select * from todolist")
        projet = cursor.fetchall()
        for proj in projet:
            messagebox.showinfo(
                f" ID: {proj[0]},titre:{proj[1]},Statut:{proj[2]},description:{proj[3]},date_echeance{proj[4]}")

def update_projet(id, new_titre=None, new_description=None):
        if new_titre:
            cursor.execute("update todolist set titre= ? where id=?", (id, new_titre))
        if new_description:
            cursor.execute("update todolist set description=? where id =?", (id, new_description))
        conn.commit()
        messagebox.showinfo("Successful update!")

def delete_projet(id):
        cursor.execute("delete from todolist where id=? ", (id,))
        conn.commit()
        messagebox.showinfo("projet Successfully delete!")

def completed_projet(id):
        cursor.execute("update from todolist set statut='completed' where id = ? ", (id))
        conn.commit()
        messagebox.showinfo(tk.END, "projet marked as completed!")

#My NoteBook


def add_Notes_Personnels(titre, description='', date_echeance=None):
            cursor.execute(""" 
            INSERT INTO todolist(titre,description,date_echeance) values (?,?,?) """,
                           (titre, description, date_echeance))
            conn.commit()
            messagebox.showinfo("Notes ajouter avec succes!")

def list_Notes_Personnels():
            cursor.execute("select * from todolist")
            Notes_Personnels = cursor.fetchall()
            for Note in Notes_Personnels:
                messagebox.showinfo(
                    f" ID: {Note[0]},titre:{Note[1]},Statut:{Note[2]},description:{Note[3]},date_echeance{Note[4]}")

def update_Notes_Personnels(id, new_titre=None, new_description=None):
            if new_titre:
                cursor.execute("update todolist set titre= ? where id=?", (id, new_titre))
            if new_description:
                cursor.execute("update todolist set description=? where id =?", (id, new_description))
            conn.commit()
            messagebox.showinfo("Successful update!")

def delete_Notes_Personnels(id):
            cursor.execute("delete from todolist where id=? ", (id,))
            conn.commit()
            messagebox.showinfo("Notes_Personnels Successfully delete!")

def completed_Notes_Personnels(id):
            cursor.execute("update from todolist set statut='completed' where id = ? ", (id))
            conn.commit()
            messagebox.showinfo(tk.END, "Notes_Personnels marked as completed!")








