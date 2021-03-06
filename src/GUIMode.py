#!/usr/bin/env python
"""

Module that holds the GUI modes used by FloatCanvas

Note that this can only be imported after a wx.App() has been created.

This approach was inpired by Christian Blouin, who also wrote the initial
version of the code.

"""

import wx
import FloatCanvas
import numpy as N
import Resources
from wx.lib.floatcanvas.Utilities import BBox

LINE_WIDTH        =  3
LINE_COLOR_POSE   = (225,113,45)
LINE_COLOR_NAV    = (169,81,133)
LINE_COLOR_DONE   = (20,200,0)
EDGE_WIDTH        =  4
EDGE_COLOR_NORMAL = (110,110,105)
EDGE_COLOR_LOCKED = (255,106,54)
NODE_COLOR_NORMAL = (240,240,240)
NODE_COLOR_LOCKED = (255,106,54)

class Cursors(object):
    """
    Class to hold the standard Cursors
    
    """
    def __init__(self):
        if "wxMac" in wx.PlatformInfo: 
            # use 16X16 cursors for wxMac
            self.HandCursor = wx.CursorFromImage(Resources.getHand16Image())
            self.GrabHandCursor = wx.CursorFromImage(Resources.getGrabHand16Image())
        
            img = Resources.getMagPlus16Image()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 6)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 6)
            self.MagPlusCursor = wx.CursorFromImage(img)
        
            img = Resources.getMagMinus16Image()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 6)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 6)
            self.MagMinusCursor = wx.CursorFromImage(img)
        else: 
            # use 24X24 cursors for GTK and Windows
#             self.HandCursor = wx.CursorFromImage(Resources.getHandImage())
#             self.GrabHandCursor = wx.CursorFromImage(Resources.getGrabHandImage())
            self.PanCursor = wx.CursorFromImage(Resources.getAeroMoveCursorImage())            
            self.SelectCursor = wx.CursorFromImage(Resources.getSelectCursorImage())
            
            img = Resources.getCrossCursorImage()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 11)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 11)
            self.CrossCursor = wx.CursorFromImage(img)
            
            img = Resources.getAeroArrowCursorImage()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 6)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 1)
            self.ArrowCursor = wx.CursorFromImage(img)
            
            img = Resources.getAeroHandCursorImage()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 7)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 1)
            self.PointerHandCursor = wx.CursorFromImage(img)
        
            img = Resources.getZoomInCursorImage()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 9)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 9)
            self.MagPlusCursor = wx.CursorFromImage(img)
        
            img = Resources.getZoomOutCursorImage()
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_X, 9)
            img.SetOptionInt(wx.IMAGE_OPTION_CUR_HOTSPOT_Y, 9)
            self.MagMinusCursor = wx.CursorFromImage(img)


class GUIBase(object):
    """
    Basic Mouse mode and baseclass for other GUImode.

    This one does nothing with any event

    """
    def __init__(self, Canvas=None):
        self.Canvas = Canvas
        self.Cursors = Cursors()

    Cursor = wx.NullCursor
    def UnSet(self):
        pass
    def OnLeftDown(self, event):
        pass
    def OnLeftUp(self, event):
        pass
    def OnLeftDouble(self, event):
        pass
    def OnRightDown(self, event):
        pass
    def OnRightUp(self, event):
        pass
    def OnRightDouble(self, event):
        pass
    def OnMiddleDown(self, event):
        pass
    def OnMiddleUp(self, event):
        pass
    def OnMiddleDouble(self, event):
        pass
    def OnWheel(self, event):
        pass
    def OnMove(self, event):
        pass
    def OnKeyDown(self, event):
        pass
    def OnKeyUp(self, event):
        pass
    def UpdateScreen(self):
        pass

class GUIMouse(GUIBase):
    """

    Mouse mode checks for a hit test, and if nothing is hit,
    raises a FloatCanvas mouse event for each event.

    """
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.Cursor = self.Cursors.ArrowCursor

    # Handlers
    def OnLeftDown(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnLeftUp(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnLeftDouble(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDown(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleUp(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDouble(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDown(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightUp(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDouble(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnWheel(self, event):
        EventType = FloatCanvas.EVT_FC_MOUSEWHEEL
        self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMove(self, event):
        ## The Move event always gets raised, even if there is a hit-test
        self.Canvas.MouseOverTest(event)
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
        
    def SwitchCursor(self, status):
        pc = self.Cursors.PointerHandCursor
        ac = self.Cursors.ArrowCursor
        if status == 'enter' or self.Cursor == ac:
            self.Canvas.SetCursor(pc)
            self.Cursor = pc
        else:
            self.Canvas.SetCursor(ac)
            self.Cursor = ac
        
class GUISelect(GUIBase):
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.Cursor = self.Cursors.CrossCursor
        self.PrevRBBox = None

    # Starts drawing the selection box when the left mouse button is pressed
    def OnLeftDown(self, event):
        self.StartRBBox = N.array( event.GetPosition() )
        self.PrevRBBox = None
        self.Canvas.CaptureMouse()
        
        EventType = FloatCanvas.EVT_FC_LEFT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)
    
    # Records the coordinates of the box when the left button is no longer held down
    def OnLeftUp(self, event):
        if event.LeftUp() and not self.StartRBBox is None:            
            self.PrevRBBox = None
            EndRBBox = event.GetPosition()
            StartRBBox = self.StartRBBox
            
            # if mouse has moved less that ten pixels, don't use the box.
            if ( abs(StartRBBox[0] - EndRBBox[0]) > 10
                    and abs(StartRBBox[1] - EndRBBox[1]) > 10 ):
                StartRBBox = self.Canvas.PixelToWorld(StartRBBox)
                EndRBBox = self.Canvas.PixelToWorld(event.GetPosition())
                self.Canvas.SelBoxStart = StartRBBox
                self.Canvas.SelBoxEnd   = EndRBBox
            else:
                self.Canvas.SelBoxStart = (0,0)
                self.Canvas.SelBoxEnd   = (0,0)
            self.StartRBBox = None
            self.Canvas.Draw(True)
            
            EventType = FloatCanvas.EVT_FC_LEFT_UP
            if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)
    
    # Keep track of the mouse position while the left button is held down
    def OnMove(self, event):
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
        if event.Dragging() and event.LeftIsDown() and not (self.StartRBBox is None):
            xy0 = self.StartRBBox
            xy1 = N.array( event.GetPosition() )
            wh  = abs(xy1 - xy0)
#             wh[0] = max(wh[0], int(wh[1]*self.Canvas.AspectRatio))
#             wh[1] = int(wh[0] / self.Canvas.AspectRatio)
            xy_c = (xy0 + xy1) / 2
            dc = wx.ClientDC(self.Canvas)
            dc.BeginDrawing()
            dc.SetPen(wx.Pen("GRAY", 2, wx.SHORT_DASH))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetLogicalFunction(wx.XOR)
            if self.PrevRBBox:
                dc.DrawRectanglePointSize(*self.PrevRBBox)
            self.PrevRBBox = ( xy_c - wh/2, wh )
            dc.DrawRectanglePointSize( *self.PrevRBBox )
            dc.EndDrawing()
            
    def UpdateScreen(self):
        #if False:
        if self.PrevRBBox is not None:
            dc = wx.ClientDC(self.Canvas)
            dc.SetPen(wx.Pen('WHITE', 2, wx.SHORT_DASH))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetLogicalFunction(wx.XOR)
            dc.DrawRectanglePointSize(*self.PrevRBBox)

    def OnLeftDouble(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDown(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleUp(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDouble(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDown(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightUp(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDouble(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnWheel(self, event):
        EventType = FloatCanvas.EVT_FC_MOUSEWHEEL
        self.Canvas._RaiseMouseEvent(event, EventType)
        
class GUIPoseEst(GUIBase):
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.Cursor = self.Cursors.ArrowCursor

    # Starts drawing the selection box when the left mouse button is pressed
    def OnLeftDown(self, event):
        self.StartPoint = N.array( event.GetPosition() )
        try:
            self.Canvas.RemoveObject(self.ArrowLine)
        except (ValueError, AttributeError):
                pass
        self.ArrowLine = None        
        self.PrevPoint = None
        self.Canvas.CaptureMouse()
    
    # Records the coordinates of the box when the left button is no longer held down
    def OnLeftUp(self, event):
        if event.LeftUp() and not self.StartPoint is None:            
            self.PrevPoint = None
            EndPoint = event.GetPosition()
            StartPoint = self.StartPoint
            
            # if mouse has moved less that ten pixels, don't use the box.
            if ( abs(StartPoint[0] - EndPoint[0]) > 5
                    or abs(StartPoint[1] - EndPoint[1]) > 5 ):
                StartPoint = self.Canvas.PixelToWorld(StartPoint)
                EndPoint = self.Canvas.PixelToWorld(event.GetPosition())
                
                try:
                    self.Canvas.RemoveObject(self.ArrowLine)
                except (ValueError, AttributeError):
                    pass
                self.ArrowLine = self.Canvas.AddArrowLine((StartPoint,EndPoint), 
                                                     LineWidth=LINE_WIDTH, LineColor=LINE_COLOR_DONE,
                                                     ArrowHeadSize=10, InForeground=True)
                
                self.Publish2DPoseEstimate(StartPoint, EndPoint, self.ArrowLine)
            else:
                self.Canvas.PoseEstStart = (0,0)
                self.Canvas.PoseEstEnd   = (0,0)
            self.StartPoint = None
            self.Canvas.Draw(True)
    
    # Keep track of the mouse position while the left button is held down
    def OnMove(self, event):
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
        if event.Dragging() and event.LeftIsDown() and not (self.StartPoint is None):
            xy0 = self.Canvas.PixelToWorld(self.StartPoint)
            xy1 = self.Canvas.PixelToWorld(N.array( event.GetPosition() ))
            
            try:
                self.Canvas.RemoveObject(self.ArrowLine)
            except (ValueError, AttributeError):
                pass
            self.ArrowLine = self.Canvas.AddArrowLine((xy0,xy1), 
                                                 LineWidth=LINE_WIDTH, LineColor=LINE_COLOR_POSE,
                                                 ArrowHeadSize=10, InForeground=True)
            self.PrevPoint = xy1
            self.Canvas.Draw(True)

    def Publish2DPoseEstimate(self, start, end, graphic_obj):        
        self.Canvas.GetParent().GetParent().Publish2DPoseEstimate(start,end, graphic_obj)

    def OnLeftDouble(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDown(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleUp(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDouble(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDown(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightUp(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDouble(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnWheel(self, event):
        EventType = FloatCanvas.EVT_FC_MOUSEWHEEL
        self.Canvas._RaiseMouseEvent(event, EventType)
        
class GUINavGoal(GUIBase):
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.Cursor = self.Cursors.ArrowCursor

    # Starts drawing the selection box when the left mouse button is pressed
    def OnLeftDown(self, event):
        self.StartPoint = N.array( event.GetPosition() )
        try:
            self.Canvas.RemoveObject(self.NGArrowLine)
        except (ValueError, AttributeError):
                pass
        self.NGArrowLine = None        
        self.PrevPoint = None
        self.Canvas.CaptureMouse()
    
    # Records the coordinates of the box when the left button is no longer held down
    def OnLeftUp(self, event):
        if event.LeftUp() and not self.StartPoint is None:            
            self.PrevPoint = None
            EndPoint = event.GetPosition()
            StartPoint = self.StartPoint
            
            # if mouse has moved less that ten pixels, don't use the box.
            if ( abs(StartPoint[0] - EndPoint[0]) > 5
                    or abs(StartPoint[1] - EndPoint[1]) > 5 ):
                StartPoint = self.Canvas.PixelToWorld(StartPoint)
                EndPoint = self.Canvas.PixelToWorld(event.GetPosition())
                
                try:
                    self.Canvas.RemoveObject(self.NGArrowLine)
                except (ValueError, AttributeError):
                    pass
                self.NGArrowLine = self.Canvas.AddArrowLine((StartPoint,EndPoint), 
                                                     LineWidth=LINE_WIDTH, LineColor=LINE_COLOR_DONE,
                                                     ArrowHeadSize=10, InForeground=True)
                
                self.Publish2DNavGoal(StartPoint, EndPoint, self.NGArrowLine)
            else:
                self.Canvas.PoseEstStart = (0,0)
                self.Canvas.PoseEstEnd   = (0,0)
            self.StartPoint = None
            self.Canvas.Draw(True)
    
    # Keep track of the mouse position while the left button is held down
    def OnMove(self, event):
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
        if event.Dragging() and event.LeftIsDown() and not (self.StartPoint is None):
            xy0 = self.Canvas.PixelToWorld(self.StartPoint)
            xy1 = self.Canvas.PixelToWorld(N.array( event.GetPosition() ))
            
            try:
                self.Canvas.RemoveObject(self.NGArrowLine)
            except (ValueError, AttributeError):
                pass
            self.NGArrowLine = self.Canvas.AddArrowLine((xy0,xy1), 
                                                 LineWidth=LINE_WIDTH, LineColor=LINE_COLOR_NAV,
                                                 ArrowHeadSize=10, InForeground=True)
            self.PrevPoint = xy1
            self.Canvas.Draw(True)

    def Publish2DNavGoal(self, start, end, graphic_obj):        
        self.Canvas.GetParent().GetParent().Publish2DNavGoal(start,end, graphic_obj)

    def OnLeftDouble(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDown(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleUp(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDouble(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDown(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightUp(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDouble(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnWheel(self, event):
        EventType = FloatCanvas.EVT_FC_MOUSEWHEEL
        self.Canvas._RaiseMouseEvent(event, EventType)
        

class GUIEdges(GUIBase):
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.Cursor = self.Cursors.ArrowCursor
        self.start_node = None
        self.locked = False     
        self.count = 0      

    # Starts drawing the selection box when the left mouse button is pressed
    def OnLeftDown(self, event):  
        mf = self.Canvas.GetParent().GetParent()
        EventType = FloatCanvas.EVT_FC_LEFT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            try:
                mf.graphics_nodes[ int(self.start_node) ].SetFillColor(NODE_COLOR_NORMAL)
            except (AttributeError, ValueError, TypeError, IndexError):
                pass
            self.start_node = None
            self.start_coords = None
            self.EraseCurrentEdge()
            self.Canvas.Draw(True)
            self.Canvas._RaiseMouseEvent(event, EventType)            
    
    # Records the coordinates of the box when the left button is no longer held down
    def OnLeftUp(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_UP
        if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)     

    def SetStartNode(self, n_id, n_coords):        
        mf = self.Canvas.GetParent().GetParent()
        self.start_node = n_id
        self.start_coords = n_coords
        mf.graphics_nodes[ int(n_id) ].SetFillColor(NODE_COLOR_LOCKED)
        self.curr_node = None
        self.Canvas.CaptureMouse()
    
    # Keep track of the mouse position while the left button is held down
    def OnMove(self, event):
        self.Canvas.MouseOverTest(event)
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
        if not (self.start_node is None):
            xy = self.Canvas.PixelToWorld(N.array( event.GetPosition() ))
            
            if self.locked is False:
                self.EraseCurrentEdge()
                self.edge = self.Canvas.AddLine((self.start_coords, xy), LineWidth=EDGE_WIDTH,
                                                LineColor=EDGE_COLOR_NORMAL)  
                self.Canvas.Draw(True)
            
    def LockEdge(self, status, n_id, n_coords):
        mf = self.Canvas.GetParent().GetParent()
        if (((status == 'l_node' and self.count==1) or status == 'e_node') and not self.locked): 
            self.locked = True
            self.count = 0
            if not (self.start_node is None) and n_id != -1:
                mf.graphics_nodes[ int(n_id) ].SetFillColor(NODE_COLOR_LOCKED)
                self.lock_node = n_id
                self.lock_coords = n_coords
                if self.lock_node != self.start_node:
                    self.EraseCurrentEdge()
                    self.edge = self.Canvas.AddLine((self.start_coords, self.lock_coords), LineWidth=EDGE_WIDTH,
                                                    LineColor=EDGE_COLOR_LOCKED)  
                    self.curr_node = n_id
                    self.Canvas.Draw(True)
                    
        elif status == 'l_node' and self.count == 0 and not self.locked:
            self.count = 1  
            
        else:
            try:
                mf.graphics_nodes[ int(self.curr_node) ].SetFillColor(NODE_COLOR_NORMAL)
            except (AttributeError, ValueError, TypeError):
                pass
            self.locked = False
            self.curr_node = None
            
    def SetEndNode(self, n_id):
        mf = self.Canvas.GetParent().GetParent()
        
#         if self.curr_node is not None:
        mf.SetModes('SetEndNode', {'auto_erase':False, 'manual_edges':True, 'redraw':False})
        mf.SelectOneNode(mf.graphics_nodes[int(self.start_node)], True)
        mf.SelectOneNode(mf.graphics_nodes[int(n_id) ], False)
        mf.CreateEdges(None)  
        mf.RestoreModes('SetEndNode')
        self.start_node = None
        self.start_coords = None      
        self.EraseCurrentEdge()
        mf.DeselectAll(None)
        self.Canvas.Draw(True)
        
    def EraseCurrentEdge(self):
        try:
            self.Canvas.RemoveObject(self.edge)
        except (ValueError,AttributeError):
            pass
        
    def SwitchCursor(self, status):
        pc = self.Cursors.PointerHandCursor
        ac = self.Cursors.ArrowCursor
        if status == 'enter' or self.Cursor == ac:
            self.Canvas.SetCursor(pc)
            self.Cursor = pc
        else:
            self.Canvas.SetCursor(ac)
            self.Cursor = ac      

    def OnLeftDouble(self, event):
        EventType = FloatCanvas.EVT_FC_LEFT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
                self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDown(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleUp(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnMiddleDouble(self, event):
        EventType = FloatCanvas.EVT_FC_MIDDLE_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDown(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DOWN
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightUp(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_UP
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnRightDouble(self, event):
        EventType = FloatCanvas.EVT_FC_RIGHT_DCLICK
        if not self.Canvas.HitTest(event, EventType):
            self.Canvas._RaiseMouseEvent(event, EventType)

    def OnWheel(self, event):
        EventType = FloatCanvas.EVT_FC_MOUSEWHEEL
        self.Canvas._RaiseMouseEvent(event, EventType)


class GUIPan(GUIBase):
    """
    Mode that moves the image (pans).
    It doesn't change any coordinates, it only changes what the viewport is
    """
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.Cursor = self.Cursors.PanCursor
        self.GrabCursor = self.Cursors.PanCursor
        self.StartMove = None
        self.MidMove = None
        self.PrevMoveXY = None
        
        ## timer to give a delay when moving so that buffers aren't re-built too many times.
        self.MoveTimer = wx.PyTimer(self.OnMoveTimer)

    def OnLeftDown(self, event):
        self.Canvas.SetCursor(self.GrabCursor)
        self.Canvas.CaptureMouse()
        self.StartMove = N.array( event.GetPosition() )
        self.MidMove = self.StartMove
        self.PrevMoveXY = (0,0)

    def OnLeftUp(self, event):
        self.Canvas.SetCursor(self.Cursor)
        if self.StartMove is not None:
            self.EndMove = N.array(event.GetPosition())
            DiffMove = self.MidMove-self.EndMove
            self.Canvas.MoveImage(DiffMove, 'Pixel', ReDraw=True)

    def OnMove(self, event):
        # Always raise the Move event.
        self.Canvas._RaiseMouseEvent(event, FloatCanvas.EVT_FC_MOTION)
        if event.Dragging() and event.LeftIsDown() and not self.StartMove is None:
            self.EndMove = N.array(event.GetPosition())
            self.MoveImage(event)
            DiffMove = self.MidMove-self.EndMove
            self.Canvas.MoveImage(DiffMove, 'Pixel', ReDraw=False)# reset the canvas without re-drawing
            self.MidMove = self.EndMove
            self.MoveTimer.Start(30, oneShot=True)

    def OnMoveTimer(self, event=None):
        self.Canvas.Draw()

    def UpdateScreen(self):
        ## The screen has been re-drawn, so StartMove needs to be reset.
        self.StartMove = self.MidMove

    def MoveImage(self, event ):
        #xy1 = N.array( event.GetPosition() )
        xy1 = self.EndMove
        wh = self.Canvas.PanelSize
        xy_tl = xy1 - self.StartMove
        dc = wx.ClientDC(self.Canvas)
        dc.BeginDrawing()
        x1,y1 = self.PrevMoveXY
        x2,y2 = xy_tl
        w,h = self.Canvas.PanelSize
        ##fixme: This sure could be cleaner!
        ##   This is all to fill in the background with the background color
        ##   without flashing as the image moves.
        if x2 > x1 and y2 > y1:
            xa = xb = x1
            ya = yb = y1
            wa = w
            ha = y2 - y1
            wb = x2-  x1
            hb = h
        elif x2 > x1 and y2 <= y1:
            xa = x1
            ya = y1
            wa = x2 - x1
            ha = h
            xb = x1
            yb = y2 + h
            wb = w
            hb = y1 - y2
        elif x2 <= x1 and y2 > y1:
            xa = x1
            ya = y1
            wa = w
            ha = y2 - y1
            xb = x2 + w
            yb = y1
            wb = x1 - x2
            hb = h - y2 + y1
        elif x2 <= x1 and y2 <= y1:
            xa = x2 + w
            ya = y1
            wa = x1 - x2
            ha = h
            xb = x1
            yb = y2 + h
            wb = w
            hb = y1 - y2

        dc.SetPen(wx.TRANSPARENT_PEN)
        dc.SetBrush(self.Canvas.BackgroundBrush)
        dc.DrawRectangle(xa, ya, wa, ha)
        dc.DrawRectangle(xb, yb, wb, hb)
        self.PrevMoveXY = xy_tl
        if self.Canvas._ForeDrawList:
            dc.DrawBitmapPoint(self.Canvas._ForegroundBuffer,xy_tl)
        else:
            dc.DrawBitmapPoint(self.Canvas._Buffer,xy_tl)
        dc.EndDrawing()
        #self.Canvas.Update()

    def OnWheel(self, event):
        """
           By default, zoom in/out by a 0.1 factor per Wheel event.
        """
        if event.GetWheelRotation() < 0:
            self.Canvas.Zoom(0.9)
        else:
            self.Canvas.Zoom(1.1)

class GUIZoomIn(GUIBase):
 
    def __init__(self, canvas=None):
        GUIBase.__init__(self, canvas)
        self.StartRBBox = None
        self.PrevRBBox = None
        self.Cursor = self.Cursors.MagPlusCursor

    def OnLeftDown(self, event):
        self.StartRBBox = N.array( event.GetPosition() )
        self.PrevRBBox = None
        self.Canvas.CaptureMouse()

    def OnLeftUp(self, event):
        if event.LeftUp() and not self.StartRBBox is None:
            self.PrevRBBox = None
            EndRBBox = event.GetPosition()
            StartRBBox = self.StartRBBox
            # if mouse has moved less that ten pixels, don't use the box.
            if ( abs(StartRBBox[0] - EndRBBox[0]) > 10
                    and abs(StartRBBox[1] - EndRBBox[1]) > 10 ):
                EndRBBox = self.Canvas.PixelToWorld(EndRBBox)
                StartRBBox = self.Canvas.PixelToWorld(StartRBBox)
                self.Canvas.ZoomToBB( BBox.fromPoints(N.r_[EndRBBox,StartRBBox]) )
            else:
                Center = self.Canvas.PixelToWorld(StartRBBox)
                self.Canvas.Zoom(1.5,Center)
            self.StartRBBox = None

    def OnMove(self, event):
        # Always raise the Move event.
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
        if event.Dragging() and event.LeftIsDown() and not (self.StartRBBox is None):
            xy0 = self.StartRBBox
            xy1 = N.array( event.GetPosition() )
            wh  = abs(xy1 - xy0)
            wh[0] = max(wh[0], int(wh[1]*self.Canvas.AspectRatio))
            wh[1] = int(wh[0] / self.Canvas.AspectRatio)
            xy_c = (xy0 + xy1) / 2
            dc = wx.ClientDC(self.Canvas)
            dc.BeginDrawing()
            dc.SetPen(wx.Pen('WHITE', 2, wx.SHORT_DASH))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetLogicalFunction(wx.XOR)
            if self.PrevRBBox:
                dc.DrawRectanglePointSize(*self.PrevRBBox)
            self.PrevRBBox = ( xy_c - wh/2, wh )
            dc.DrawRectanglePointSize( *self.PrevRBBox )
            dc.EndDrawing()
            
    def UpdateScreen(self):
        """
        Update gets called if the screen has been repainted in the middle of a zoom in
        so the Rubber Band Box can get updated
        """
        #if False:
        if self.PrevRBBox is not None:
            dc = wx.ClientDC(self.Canvas)
            dc.SetPen(wx.Pen('WHITE', 2, wx.SHORT_DASH))
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.SetLogicalFunction(wx.XOR)
            dc.DrawRectanglePointSize(*self.PrevRBBox)

    def OnRightDown(self, event):
        self.Canvas.Zoom(1/1.5, event.GetPosition(), centerCoords="pixel")

    def OnWheel(self, event):
        if event.GetWheelRotation() < 0:
            self.Canvas.Zoom(0.9)
        else:
            self.Canvas.Zoom(1.1)

class GUIZoomOut(GUIBase):

    def __init__(self, Canvas=None):
        GUIBase.__init__(self, Canvas)
        self.Cursor = self.Cursors.MagMinusCursor
        
    def OnLeftDown(self, event):
        self.Canvas.Zoom(1/1.5, event.GetPosition(), centerCoords="pixel")

    def OnRightDown(self, event):
        self.Canvas.Zoom(1.5, event.GetPosition(), centerCoords="pixel")

    def OnWheel(self, event):
        if event.GetWheelRotation() < 0:
            self.Canvas.Zoom(0.9)
        else:
            self.Canvas.Zoom(1.1)

    def OnMove(self, event):
        # Always raise the Move event.
        self.Canvas._RaiseMouseEvent(event,FloatCanvas.EVT_FC_MOTION)
