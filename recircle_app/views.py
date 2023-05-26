from django.db.models import Sum
from django.views.generic import ListView
from .models import StateStats


class ViewCoveredRegions(ListView):
    model = StateStats
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ViewCoveredRegions, self).get_context_data(**kwargs)

        stats_list = StateStats.objects.all()
        stats_data = []

        total_rigid_waste = StateStats.objects.aggregate(rigid_waste=Sum('rigid'))['rigid_waste']
        total_flexible_waste = StateStats.objects.aggregate(flexible_waste=Sum('flexible'))['flexible_waste']
        total_mlp_waste = StateStats.objects.aggregate(mlp_waste=Sum('mlp'))['mlp_waste']

        for state_details in stats_list:
            total_waste = StateStats.total_waste(state_details)
            if total_waste > 2000:
                color = '#0E2433'
                recovery_rank = 1
            elif 1500 < total_waste <= 2000:
                color = '#296D9E'
                recovery_rank = 2
            else:
                color = '#45B6FE'
                recovery_rank = 3

            stats_data.append({
                "state_code": state_details.state_code,
                "state_name": state_details.state_name,
                "rigid": state_details.rigid,
                "flexible": state_details.flexible,
                "mlp": state_details.mlp,
                "total_waste": total_waste,
                "color": color,
                "recovery_rank": recovery_rank
            })

        # print(stats_list)
        context['stats_data'] = stats_data
        context['total_rigid_waste'] = total_rigid_waste
        context['total_flexible_waste'] = total_flexible_waste
        context['total_mlp_waste'] = total_mlp_waste
        return context
