"""autogenerated by genmsg_py from raven_jointmove.msg. Do not edit."""
import roslib.message
import struct

import std_msgs.msg

class raven_jointmove(roslib.message.Message):
  _md5sum = "c77744b32e84ca2df946f65f29601eb9"
  _type = "raven_2/raven_jointmove"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Header      hdr
float32[4]    specify

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['hdr','specify']
  _slot_types = ['Header','float32[4]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       hdr,specify
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(raven_jointmove, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.hdr is None:
        self.hdr = std_msgs.msg._Header.Header()
      if self.specify is None:
        self.specify = [0.,0.,0.,0.]
    else:
      self.hdr = std_msgs.msg._Header.Header()
      self.specify = [0.,0.,0.,0.]

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs))
      _x = self.hdr.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_4f.pack(*self.specify))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.hdr is None:
        self.hdr = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.hdr.frame_id = str[start:end]
      start = end
      end += 16
      self.specify = _struct_4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs))
      _x = self.hdr.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(self.specify.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.hdr is None:
        self.hdr = std_msgs.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.hdr.seq, _x.hdr.stamp.secs, _x.hdr.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.hdr.frame_id = str[start:end]
      start = end
      end += 16
      self.specify = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_4f = struct.Struct("<4f")
_struct_3I = struct.Struct("<3I")