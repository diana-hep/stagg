# automatically generated by the FlatBuffers compiler, do not modify

# namespace: aghast_generated

import flatbuffers


class WeightedCounts(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsWeightedCounts(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WeightedCounts()
        x.Init(buf, n + offset)
        return x

    # WeightedCounts
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # WeightedCounts
    def SumwType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # WeightedCounts
    def Sumw(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # WeightedCounts
    def Sumw2Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # WeightedCounts
    def Sumw2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # WeightedCounts
    def Unweighted(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .UnweightedCounts import UnweightedCounts

            obj = UnweightedCounts()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None


def WeightedCountsStart(builder):
    builder.StartObject(5)


def WeightedCountsAddSumwType(builder, sumwType):
    builder.PrependUint8Slot(0, sumwType, 0)


def WeightedCountsAddSumw(builder, sumw):
    builder.PrependUOffsetTRelativeSlot(
        1, flatbuffers.number_types.UOffsetTFlags.py_type(sumw), 0
    )


def WeightedCountsAddSumw2Type(builder, sumw2Type):
    builder.PrependUint8Slot(2, sumw2Type, 0)


def WeightedCountsAddSumw2(builder, sumw2):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(sumw2), 0
    )


def WeightedCountsAddUnweighted(builder, unweighted):
    builder.PrependUOffsetTRelativeSlot(
        4, flatbuffers.number_types.UOffsetTFlags.py_type(unweighted), 0
    )


def WeightedCountsEnd(builder):
    return builder.EndObject()
