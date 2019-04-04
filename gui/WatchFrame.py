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
from gui.BrandPanel import *
from gui.StrapMaterialPanel import *
from gui.MovementPanel import *
from gui.AddWatchPanel import *
from gui.ViewWatchPanel import *
###########################################################################
## Class WatchFrame
###########################################################################

class WatchFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Watch Management", pos = wx.DefaultPosition, size = wx.Size( 1200,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.ALWAYS_SHOW_SB|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_mnuFile = wx.Menu()
		self.m_mnuItem_StrapMaterial = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"&Strap Material", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItem_StrapMaterial )

		self.m_mnuItem_BrandName = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"&Brand Name", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItem_BrandName )

		self.m_mnuItem_Movement = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"&Movement", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItem_Movement )

		self.m_menuItem_AddWatch = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"&Add Watch", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_menuItem_AddWatch )

		self.m_mnuItem_ViewWatch = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"&View Watch", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItem_ViewWatch )

		self.m_mnuFile.AppendSeparator()

		self.m_mnuItem_Exit = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItem_Exit )

		self.m_menubar1.Append( self.m_mnuFile, u"&File" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_strap_material = wx.Button( self, wx.ID_ANY, u"Strap Material", wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer41.Add( self.btn_strap_material, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.btn_brand = wx.Button( self, wx.ID_ANY, u"Brand", wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer41.Add( self.btn_brand, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


		bSizer15.Add( bSizer41, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_movement = wx.Button( self, wx.ID_ANY, u"Movement", wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer411.Add( self.btn_movement, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.btn_add_watch = wx.Button( self, wx.ID_ANY, u"Add Watch", wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer411.Add( self.btn_add_watch, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.ALL, 5 )


		bSizer15.Add( bSizer411, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_view_watch = wx.Button( self, wx.ID_ANY, u"View Watch", wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer412.Add( self.btn_view_watch, 0, wx.ALL, 5 )

		self.btn_exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 250,50 ), 0 )
		bSizer412.Add( self.btn_exit, 0, wx.ALL, 5 )


		bSizer15.Add( bSizer412, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_mnuItem_StrapMaterial_click, id = self.m_mnuItem_StrapMaterial.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mnuItem_BrandName_click, id = self.m_mnuItem_BrandName.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mnuItem_Movement_click, id = self.m_mnuItem_Movement.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItem_AddWatch_click, id = self.m_menuItem_AddWatch.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mnuItem_ViewWatch_click, id = self.m_mnuItem_ViewWatch.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mnuItem_Exit_click, id = self.m_mnuItem_Exit.GetId() )
		self.btn_strap_material.Bind( wx.EVT_BUTTON, self.btn_strap_material_click )
		self.btn_brand.Bind( wx.EVT_BUTTON, self.btn_brand_click )
		self.btn_movement.Bind( wx.EVT_BUTTON, self.btn_movement_click )
		self.btn_add_watch.Bind( wx.EVT_BUTTON, self.btn_add_watch_click )
		self.btn_view_watch.Bind( wx.EVT_BUTTON, self.btn_view_watch_click )
		self.btn_exit.Bind( wx.EVT_BUTTON, self.btn_exit_click )

	def __del__(self):
		DBConnection.close()

		return


	# Virtual event handlers, overide them in your derived class
	def m_mnuItem_StrapMaterial_click( self, event ):
		self.showStrapMaterialPanel()

		return



	def m_mnuItem_BrandName_click( self, event ):
		self.showBrandPanel()

		return



	def m_mnuItem_Movement_click( self, event ):
		self.showMovementPanel()

		return


	def m_menuItem_AddWatch_click( self, event ):
		self.showAddWatchPanel()

		return


	def m_mnuItem_ViewWatch_click( self, event ):
		self.showViewWatchPanel()

		return


	def m_mnuItem_Exit_click( self, event ):
		self.Close(True)

		return

	def btn_strap_material_click( self, event ):
		self.showStrapMaterialPanel()

		return

	def btn_brand_click( self, event ):
		self.showBrandPanel()

		return

	def btn_movement_click( self, event ):
		self.showMovementPanel()

		return

	def btn_add_watch_click( self, event ):
		self.showAddWatchPanel()

		return

	def btn_view_watch_click( self, event ):
		self.showViewWatchPanel()

		return

	def btn_exit_click( self, event ):
		self.Close(True)

		return
    
	def showStrapMaterialPanel(self):
		frame = wx.Frame(None, title="Meterial", size=(600, 350))
		pannel = StrapMaterialPanel(frame)
		frame.Centre()
		frame.Show(True)

		return 

	def showBrandPanel(self):
		frame = wx.Frame(None, title="Brand Management", size=(600, 350))
		pannel = BrandPanel(frame)
		frame.Centre()
		frame.Show()

		return
	def showMovementPanel(self):
		frame = wx.Frame(None, title="Movement Management", size=(600, 350))
		pannel = MovementPanel(frame)
		frame.Centre()
		frame.Show()

		return
	
	def showAddWatchPanel(self):
		frame = wx.Frame(None, title="Add Watch", size=(750, 350))
		pannel = AddWatchPanel(frame)
		frame.Centre()
		frame.Show()

		return
	
	def showViewWatchPanel(self):
		frame = wx.Frame(None, title="View Watch", size=(850, 700))
		pannel = ViewWatchPanel(frame)
		frame.Centre()
		frame.Show()

		return 