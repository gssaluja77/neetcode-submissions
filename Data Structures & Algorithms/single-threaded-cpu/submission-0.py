class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted((task[0], task[1], idx) for idx, task in enumerate(tasks))

        curr_time = 0
        task_idx = 0
        pending = []
        n = len(sorted_tasks)
        res = []

        while task_idx < n or pending:
            if not pending and curr_time < sorted_tasks[task_idx][0]:
                curr_time = sorted_tasks[task_idx][0]
            
            while task_idx < n and sorted_tasks[task_idx][0] <= curr_time:
                enq_time, proc_time, idx = sorted_tasks[task_idx]
                heapq.heappush(pending, (proc_time, idx))
                task_idx += 1
            
            if pending:
                proc_time, idx = heapq.heappop(pending)
                curr_time += proc_time
                res.append(idx)
        
        return res