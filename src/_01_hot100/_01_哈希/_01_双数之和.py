class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 保存 num => idx 的映射 字典
        hashtable = {}
        # 遍历数组
        for idx, num in enumerate(nums):
            # 如果缺失的值已经在 字典中，直接返回下标
            if target - num in hashtable:
                return [hashtable[target - num], idx]
            # 如果缺失的值不在 字典中，则添加 num => idx 的映射
            else:
                hashtable[num] = idx
        # 没找到 target，返回空列表
        return []