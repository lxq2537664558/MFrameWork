# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DB_Option.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import DB_Base_pb2 as DB__Base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DB_Option.proto',
  package='PDB_Option',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x44\x42_Option.proto\x12\nPDB_Option\x1a\rDB_Base.proto\"9\n\x0fGD_GetDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x15\n\rulDBAccountid\x18\x02 \x01(\x04\"Z\n\x0f\x44G_GetDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\x12(\n\x0bstDBAccount\x18\x03 \x01(\x0b\x32\x13.PDB_Base.DBAccount\"O\n\x12GD_CreateDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12(\n\x0bstDBAccount\x18\x02 \x01(\x0b\x32\x13.PDB_Base.DBAccount\"]\n\x12\x44G_CreateDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\x12(\n\x0bstDBAccount\x18\x03 \x01(\x0b\x32\x13.PDB_Base.DBAccount\"O\n\x12GD_UpdateDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12(\n\x0bstDBAccount\x18\x02 \x01(\x0b\x32\x13.PDB_Base.DBAccount\"3\n\x12\x44G_UpdateDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\"<\n\x12GD_DeleteDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x15\n\rulDBAccountid\x18\x02 \x01(\x04\"3\n\x12\x44G_DeleteDBAccount\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\";\n\x10GD_GetDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x16\n\x0eulDBUserInfoid\x18\x02 \x01(\x04\"]\n\x10\x44G_GetDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\x12*\n\x0cstDBUserInfo\x18\x03 \x01(\x0b\x32\x14.PDB_Base.DBUserInfo\"R\n\x13GD_CreateDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12*\n\x0cstDBUserInfo\x18\x02 \x01(\x0b\x32\x14.PDB_Base.DBUserInfo\"`\n\x13\x44G_CreateDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\x12*\n\x0cstDBUserInfo\x18\x03 \x01(\x0b\x32\x14.PDB_Base.DBUserInfo\"R\n\x13GD_UpdateDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12*\n\x0cstDBUserInfo\x18\x02 \x01(\x0b\x32\x14.PDB_Base.DBUserInfo\"4\n\x13\x44G_UpdateDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05\">\n\x13GD_DeleteDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x16\n\x0eulDBUserInfoid\x18\x02 \x01(\x04\"4\n\x13\x44G_DeleteDBUserInfo\x12\x0f\n\x07uiaccid\x18\x01 \x01(\r\x12\x0c\n\x04iRet\x18\x02 \x01(\x05*\xb6\x03\n\x07\x45\x44\x42_CMD\x12\x0f\n\x0b\x44\x42_CMD_NONE\x10\x00\x12\x15\n\x10GD_GET_DBACCOUNT\x10\xca\x01\x12\x15\n\x10\x44G_GET_DBACCOUNT\x10\xcb\x01\x12\x18\n\x13GD_CREATE_DBACCOUNT\x10\xcc\x01\x12\x18\n\x13\x44G_CREATE_DBACCOUNT\x10\xcd\x01\x12\x18\n\x13GD_UPDATE_DBACCOUNT\x10\xce\x01\x12\x18\n\x13\x44G_UPDATE_DBACCOUNT\x10\xcf\x01\x12\x18\n\x13GD_DELETE_DBACCOUNT\x10\xd0\x01\x12\x18\n\x13\x44G_DELETE_DBACCOUNT\x10\xd1\x01\x12\x16\n\x11GD_GET_DBUSERINFO\x10\xd2\x01\x12\x16\n\x11\x44G_GET_DBUSERINFO\x10\xd3\x01\x12\x19\n\x14GD_CREATE_DBUSERINFO\x10\xd4\x01\x12\x19\n\x14\x44G_CREATE_DBUSERINFO\x10\xd5\x01\x12\x19\n\x14GD_UPDATE_DBUSERINFO\x10\xd6\x01\x12\x19\n\x14\x44G_UPDATE_DBUSERINFO\x10\xd7\x01\x12\x19\n\x14GD_DELETE_DBUSERINFO\x10\xd8\x01\x12\x19\n\x14\x44G_DELETE_DBUSERINFO\x10\xd9\x01\x62\x06proto3')
  ,
  dependencies=[DB__Base__pb2.DESCRIPTOR,])

_EDB_CMD = _descriptor.EnumDescriptor(
  name='EDB_CMD',
  full_name='PDB_Option.EDB_CMD',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DB_CMD_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_GET_DBACCOUNT', index=1, number=202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_GET_DBACCOUNT', index=2, number=203,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_CREATE_DBACCOUNT', index=3, number=204,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_CREATE_DBACCOUNT', index=4, number=205,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_UPDATE_DBACCOUNT', index=5, number=206,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_UPDATE_DBACCOUNT', index=6, number=207,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_DELETE_DBACCOUNT', index=7, number=208,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_DELETE_DBACCOUNT', index=8, number=209,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_GET_DBUSERINFO', index=9, number=210,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_GET_DBUSERINFO', index=10, number=211,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_CREATE_DBUSERINFO', index=11, number=212,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_CREATE_DBUSERINFO', index=12, number=213,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_UPDATE_DBUSERINFO', index=13, number=214,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_UPDATE_DBUSERINFO', index=14, number=215,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GD_DELETE_DBUSERINFO', index=15, number=216,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DG_DELETE_DBUSERINFO', index=16, number=217,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1217,
  serialized_end=1655,
)
_sym_db.RegisterEnumDescriptor(_EDB_CMD)

EDB_CMD = enum_type_wrapper.EnumTypeWrapper(_EDB_CMD)
DB_CMD_NONE = 0
GD_GET_DBACCOUNT = 202
DG_GET_DBACCOUNT = 203
GD_CREATE_DBACCOUNT = 204
DG_CREATE_DBACCOUNT = 205
GD_UPDATE_DBACCOUNT = 206
DG_UPDATE_DBACCOUNT = 207
GD_DELETE_DBACCOUNT = 208
DG_DELETE_DBACCOUNT = 209
GD_GET_DBUSERINFO = 210
DG_GET_DBUSERINFO = 211
GD_CREATE_DBUSERINFO = 212
DG_CREATE_DBUSERINFO = 213
GD_UPDATE_DBUSERINFO = 214
DG_UPDATE_DBUSERINFO = 215
GD_DELETE_DBUSERINFO = 216
DG_DELETE_DBUSERINFO = 217



_GD_GETDBACCOUNT = _descriptor.Descriptor(
  name='GD_GetDBAccount',
  full_name='PDB_Option.GD_GetDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_GetDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ulDBAccountid', full_name='PDB_Option.GD_GetDBAccount.ulDBAccountid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=103,
)


_DG_GETDBACCOUNT = _descriptor.Descriptor(
  name='DG_GetDBAccount',
  full_name='PDB_Option.DG_GetDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_GetDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_GetDBAccount.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBAccount', full_name='PDB_Option.DG_GetDBAccount.stDBAccount', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=105,
  serialized_end=195,
)


_GD_CREATEDBACCOUNT = _descriptor.Descriptor(
  name='GD_CreateDBAccount',
  full_name='PDB_Option.GD_CreateDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_CreateDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBAccount', full_name='PDB_Option.GD_CreateDBAccount.stDBAccount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=276,
)


_DG_CREATEDBACCOUNT = _descriptor.Descriptor(
  name='DG_CreateDBAccount',
  full_name='PDB_Option.DG_CreateDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_CreateDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_CreateDBAccount.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBAccount', full_name='PDB_Option.DG_CreateDBAccount.stDBAccount', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=371,
)


_GD_UPDATEDBACCOUNT = _descriptor.Descriptor(
  name='GD_UpdateDBAccount',
  full_name='PDB_Option.GD_UpdateDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_UpdateDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBAccount', full_name='PDB_Option.GD_UpdateDBAccount.stDBAccount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=452,
)


_DG_UPDATEDBACCOUNT = _descriptor.Descriptor(
  name='DG_UpdateDBAccount',
  full_name='PDB_Option.DG_UpdateDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_UpdateDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_UpdateDBAccount.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=505,
)


_GD_DELETEDBACCOUNT = _descriptor.Descriptor(
  name='GD_DeleteDBAccount',
  full_name='PDB_Option.GD_DeleteDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_DeleteDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ulDBAccountid', full_name='PDB_Option.GD_DeleteDBAccount.ulDBAccountid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=507,
  serialized_end=567,
)


_DG_DELETEDBACCOUNT = _descriptor.Descriptor(
  name='DG_DeleteDBAccount',
  full_name='PDB_Option.DG_DeleteDBAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_DeleteDBAccount.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_DeleteDBAccount.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=620,
)


_GD_GETDBUSERINFO = _descriptor.Descriptor(
  name='GD_GetDBUserInfo',
  full_name='PDB_Option.GD_GetDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_GetDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ulDBUserInfoid', full_name='PDB_Option.GD_GetDBUserInfo.ulDBUserInfoid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=681,
)


_DG_GETDBUSERINFO = _descriptor.Descriptor(
  name='DG_GetDBUserInfo',
  full_name='PDB_Option.DG_GetDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_GetDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_GetDBUserInfo.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBUserInfo', full_name='PDB_Option.DG_GetDBUserInfo.stDBUserInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=683,
  serialized_end=776,
)


_GD_CREATEDBUSERINFO = _descriptor.Descriptor(
  name='GD_CreateDBUserInfo',
  full_name='PDB_Option.GD_CreateDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_CreateDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBUserInfo', full_name='PDB_Option.GD_CreateDBUserInfo.stDBUserInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=860,
)


_DG_CREATEDBUSERINFO = _descriptor.Descriptor(
  name='DG_CreateDBUserInfo',
  full_name='PDB_Option.DG_CreateDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_CreateDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_CreateDBUserInfo.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBUserInfo', full_name='PDB_Option.DG_CreateDBUserInfo.stDBUserInfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=958,
)


_GD_UPDATEDBUSERINFO = _descriptor.Descriptor(
  name='GD_UpdateDBUserInfo',
  full_name='PDB_Option.GD_UpdateDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_UpdateDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stDBUserInfo', full_name='PDB_Option.GD_UpdateDBUserInfo.stDBUserInfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=960,
  serialized_end=1042,
)


_DG_UPDATEDBUSERINFO = _descriptor.Descriptor(
  name='DG_UpdateDBUserInfo',
  full_name='PDB_Option.DG_UpdateDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_UpdateDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_UpdateDBUserInfo.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1044,
  serialized_end=1096,
)


_GD_DELETEDBUSERINFO = _descriptor.Descriptor(
  name='GD_DeleteDBUserInfo',
  full_name='PDB_Option.GD_DeleteDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.GD_DeleteDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ulDBUserInfoid', full_name='PDB_Option.GD_DeleteDBUserInfo.ulDBUserInfoid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1098,
  serialized_end=1160,
)


_DG_DELETEDBUSERINFO = _descriptor.Descriptor(
  name='DG_DeleteDBUserInfo',
  full_name='PDB_Option.DG_DeleteDBUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uiaccid', full_name='PDB_Option.DG_DeleteDBUserInfo.uiaccid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iRet', full_name='PDB_Option.DG_DeleteDBUserInfo.iRet', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1162,
  serialized_end=1214,
)

_DG_GETDBACCOUNT.fields_by_name['stDBAccount'].message_type = DB__Base__pb2._DBACCOUNT
_GD_CREATEDBACCOUNT.fields_by_name['stDBAccount'].message_type = DB__Base__pb2._DBACCOUNT
_DG_CREATEDBACCOUNT.fields_by_name['stDBAccount'].message_type = DB__Base__pb2._DBACCOUNT
_GD_UPDATEDBACCOUNT.fields_by_name['stDBAccount'].message_type = DB__Base__pb2._DBACCOUNT
_DG_GETDBUSERINFO.fields_by_name['stDBUserInfo'].message_type = DB__Base__pb2._DBUSERINFO
_GD_CREATEDBUSERINFO.fields_by_name['stDBUserInfo'].message_type = DB__Base__pb2._DBUSERINFO
_DG_CREATEDBUSERINFO.fields_by_name['stDBUserInfo'].message_type = DB__Base__pb2._DBUSERINFO
_GD_UPDATEDBUSERINFO.fields_by_name['stDBUserInfo'].message_type = DB__Base__pb2._DBUSERINFO
DESCRIPTOR.message_types_by_name['GD_GetDBAccount'] = _GD_GETDBACCOUNT
DESCRIPTOR.message_types_by_name['DG_GetDBAccount'] = _DG_GETDBACCOUNT
DESCRIPTOR.message_types_by_name['GD_CreateDBAccount'] = _GD_CREATEDBACCOUNT
DESCRIPTOR.message_types_by_name['DG_CreateDBAccount'] = _DG_CREATEDBACCOUNT
DESCRIPTOR.message_types_by_name['GD_UpdateDBAccount'] = _GD_UPDATEDBACCOUNT
DESCRIPTOR.message_types_by_name['DG_UpdateDBAccount'] = _DG_UPDATEDBACCOUNT
DESCRIPTOR.message_types_by_name['GD_DeleteDBAccount'] = _GD_DELETEDBACCOUNT
DESCRIPTOR.message_types_by_name['DG_DeleteDBAccount'] = _DG_DELETEDBACCOUNT
DESCRIPTOR.message_types_by_name['GD_GetDBUserInfo'] = _GD_GETDBUSERINFO
DESCRIPTOR.message_types_by_name['DG_GetDBUserInfo'] = _DG_GETDBUSERINFO
DESCRIPTOR.message_types_by_name['GD_CreateDBUserInfo'] = _GD_CREATEDBUSERINFO
DESCRIPTOR.message_types_by_name['DG_CreateDBUserInfo'] = _DG_CREATEDBUSERINFO
DESCRIPTOR.message_types_by_name['GD_UpdateDBUserInfo'] = _GD_UPDATEDBUSERINFO
DESCRIPTOR.message_types_by_name['DG_UpdateDBUserInfo'] = _DG_UPDATEDBUSERINFO
DESCRIPTOR.message_types_by_name['GD_DeleteDBUserInfo'] = _GD_DELETEDBUSERINFO
DESCRIPTOR.message_types_by_name['DG_DeleteDBUserInfo'] = _DG_DELETEDBUSERINFO
DESCRIPTOR.enum_types_by_name['EDB_CMD'] = _EDB_CMD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GD_GetDBAccount = _reflection.GeneratedProtocolMessageType('GD_GetDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _GD_GETDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_GetDBAccount)
  ))
_sym_db.RegisterMessage(GD_GetDBAccount)

DG_GetDBAccount = _reflection.GeneratedProtocolMessageType('DG_GetDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _DG_GETDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_GetDBAccount)
  ))
_sym_db.RegisterMessage(DG_GetDBAccount)

GD_CreateDBAccount = _reflection.GeneratedProtocolMessageType('GD_CreateDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _GD_CREATEDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_CreateDBAccount)
  ))
_sym_db.RegisterMessage(GD_CreateDBAccount)

DG_CreateDBAccount = _reflection.GeneratedProtocolMessageType('DG_CreateDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _DG_CREATEDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_CreateDBAccount)
  ))
_sym_db.RegisterMessage(DG_CreateDBAccount)

GD_UpdateDBAccount = _reflection.GeneratedProtocolMessageType('GD_UpdateDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _GD_UPDATEDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_UpdateDBAccount)
  ))
_sym_db.RegisterMessage(GD_UpdateDBAccount)

DG_UpdateDBAccount = _reflection.GeneratedProtocolMessageType('DG_UpdateDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _DG_UPDATEDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_UpdateDBAccount)
  ))
_sym_db.RegisterMessage(DG_UpdateDBAccount)

GD_DeleteDBAccount = _reflection.GeneratedProtocolMessageType('GD_DeleteDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _GD_DELETEDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_DeleteDBAccount)
  ))
_sym_db.RegisterMessage(GD_DeleteDBAccount)

DG_DeleteDBAccount = _reflection.GeneratedProtocolMessageType('DG_DeleteDBAccount', (_message.Message,), dict(
  DESCRIPTOR = _DG_DELETEDBACCOUNT,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_DeleteDBAccount)
  ))
_sym_db.RegisterMessage(DG_DeleteDBAccount)

GD_GetDBUserInfo = _reflection.GeneratedProtocolMessageType('GD_GetDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _GD_GETDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_GetDBUserInfo)
  ))
_sym_db.RegisterMessage(GD_GetDBUserInfo)

DG_GetDBUserInfo = _reflection.GeneratedProtocolMessageType('DG_GetDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _DG_GETDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_GetDBUserInfo)
  ))
_sym_db.RegisterMessage(DG_GetDBUserInfo)

GD_CreateDBUserInfo = _reflection.GeneratedProtocolMessageType('GD_CreateDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _GD_CREATEDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_CreateDBUserInfo)
  ))
_sym_db.RegisterMessage(GD_CreateDBUserInfo)

DG_CreateDBUserInfo = _reflection.GeneratedProtocolMessageType('DG_CreateDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _DG_CREATEDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_CreateDBUserInfo)
  ))
_sym_db.RegisterMessage(DG_CreateDBUserInfo)

GD_UpdateDBUserInfo = _reflection.GeneratedProtocolMessageType('GD_UpdateDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _GD_UPDATEDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_UpdateDBUserInfo)
  ))
_sym_db.RegisterMessage(GD_UpdateDBUserInfo)

DG_UpdateDBUserInfo = _reflection.GeneratedProtocolMessageType('DG_UpdateDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _DG_UPDATEDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_UpdateDBUserInfo)
  ))
_sym_db.RegisterMessage(DG_UpdateDBUserInfo)

GD_DeleteDBUserInfo = _reflection.GeneratedProtocolMessageType('GD_DeleteDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _GD_DELETEDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.GD_DeleteDBUserInfo)
  ))
_sym_db.RegisterMessage(GD_DeleteDBUserInfo)

DG_DeleteDBUserInfo = _reflection.GeneratedProtocolMessageType('DG_DeleteDBUserInfo', (_message.Message,), dict(
  DESCRIPTOR = _DG_DELETEDBUSERINFO,
  __module__ = 'DB_Option_pb2'
  # @@protoc_insertion_point(class_scope:PDB_Option.DG_DeleteDBUserInfo)
  ))
_sym_db.RegisterMessage(DG_DeleteDBUserInfo)


# @@protoc_insertion_point(module_scope)
