# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class NtupleInstance(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsNtupleInstance(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NtupleInstance()
        x.Init(buf, n + offset)
        return x

    # NtupleInstance
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NtupleInstance
    def Chunks(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Chunk import Chunk

            obj = Chunk()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # NtupleInstance
    def ChunksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NtupleInstance
    def ChunkOffsets(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # NtupleInstance
    def ChunkOffsetsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # NtupleInstance
    def ChunkOffsetsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0


def NtupleInstanceStart(builder):
    builder.StartObject(2)


def NtupleInstanceAddChunks(builder, chunks):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(chunks), 0
    )


def NtupleInstanceStartChunksVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NtupleInstanceAddChunkOffsets(builder, chunkOffsets):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(chunkOffsets), 0
    )


def NtupleInstanceStartChunkOffsetsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def NtupleInstanceEnd(builder):
    return builder.EndObject()
