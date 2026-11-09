class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 用于保存 num => idx 的映射字典
        hashtable = {}
        # 遍历 num 数组
        for idx, num in enumerate(nums):
            # 如果 target - num，也就是缺失的另一个数字在 hashtable 中，那么返回对应的下标
            if target - num in hashtable:
                return [hashtable[target-num],idx]
            # 如果 target - num，也就是缺失的另一个数字不在 hashtable 中，将其添加到映射中即可
            else:
                hashtable[num] = idx
        # 未找到，返回空数组
        return []