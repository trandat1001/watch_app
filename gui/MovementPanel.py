# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 27 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from lib.DBConnection import *
###########################################################################
## Class MovementPanel
###########################################################################

class MovementPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Movement", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_txtName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_txtName, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnAdd = wx.Button( self, wx.ID_ANY, u"&Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_btnAdd, 0, wx.ALL, 5 )

		self.m_btnUpdate = wx.Button( self, wx.ID_ANY, u"&Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnUpdate.Enable( False )

		bSizer2.Add( self.m_btnUpdate, 0, wx.ALL, 5 )

		self.m_btnDelete = wx.Button( self, wx.ID_ANY, u"&Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnDelete.Enable( False )

		bSizer2.Add( self.m_btnDelete, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_lstMovementChoices = []
		self.m_lstMovement = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstMovementChoices, 0 )
		bSizer1.Add( self.m_lstMovement, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnAdd.Bind( wx.EVT_BUTTON, self.m_btnAdd_click )
		self.m_btnUpdate.Bind( wx.EVT_BUTTON, self.m_btnUpdate_click )
		self.m_btnDelete.Bind( wx.EVT_BUTTON, self.m_btnDelete_click )
		self.m_lstMovement.Bind( wx.EVT_LISTBOX, self.m_lstMovement_click )
		self.initData()

	def __del__( self ):
		pass

	def initData(self):
		engineList = []
		engines = DBConnection.fetchAll("SELECT * FROM tb_movement ORDER BY name")
		for item in engines:
			engineList.append(item[1])
		self.m_lstMovement.AppendItems(engineList)

		return  

	# Virtual event handlers, overide them in your derived class
	def m_btnAdd_click( self, event ):
		engineName = self.m_txtName.GetValue().strip()
		if (len(engineName) > 0):
			DBConnection.execute(
				"INSERT INTO tb_movement(name) VALUES(:_name)", {"_name": engineName})
			DBConnection.commit()
			self.m_lstMovement.Append(engineName)
			self.m_txtName.Clear()
		else:
			wx.MessageBox("Please input engine name", "Information", wx.OK)

		return

	def m_btnUpdate_click( self, event ):
		updateEngine = self.m_txtName.GetValue().strip()
		currentEngine = self.m_lstMovement.GetStringSelection()
		selectIndex = self.m_lstMovement.GetSelection()
		if (len(updateEngine) > 0):
			sql = '''
			UPDATE tb_movement
			SET name = :new_name
			WHERE name = :old_name
			'''
			DBConnection.execute(
				sql, {"new_name": updateEngine, "old_name": currentEngine})
			DBConnection.commit()
			self.m_lstMovement.SetString(selectIndex, updateEngine)
		else:
			wx.MessageBox("Please input engine name", "Information", wx.OK)

		return

	def m_btnDelete_click( self, event ):
		currentName = self.m_lstMovement.GetStringSelection()
		sql = '''
				DELETE FROM tb_movement 
				WHERE name = :current_name
				'''
		DBConnection.execute(sql, {"current_name": currentName})
		DBConnection.commit()
		self.m_lstMovement.Clear()
		self.m_txtName.Clear()
		self.initData()

		return

	def m_lstMovement_click( self, event ):
		selectName = self.m_lstMovement.GetStringSelection()
		self.m_txtName.SetValue(selectName)
		self.m_btnUpdate.Enable(True)
		self.m_btnDelete.Enable(True)

		return


