from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *

class QuotationViewSet(viewsets.ViewSet):
    def list(self,request):
        client_name=request.GET.get('a')
        quote_no=request.GET.get('b')
        insurance_type=request.GET.get('c')
        registration_no = request.GET.get('d')
        date_form = request.GET.get('e')
        date_to = request.GET.get('f')
        status = request.GET.get('g')
        if client_name:
            quotlist=Quotation.objects.filter(client_name__icontains=client_name)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})
        elif quote_no:
            quotlist = Quotation.objects.filter(quote_no__icontains=quote_no)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})
        elif insurance_type:
            quotlist = Quotation.objects.filter(insurance_type__icontains=insurance_type)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})       
        elif registration_no:
            quotlist = Quotation.objects.filter(registration_no__icontains=registration_no)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})
        elif date_form:
            quotlist=Quotation.objects.filter(date_form__icontains=date_form)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})   
        elif date_to:
            quotlist=Quotation.objects.filter(date_to__icontains=date_to)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})     
        elif status:
            quotlist = Quotation.objects.filter(status__icontains=status)
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})             
        else:
            quotlist = Quotation.objects.all()
            data=[]
            for quotlists in quotlist:
                data.append({
                    'client_name':quotlists.client_name,
                    'quote_no':quotlists.quote_no,
                    'insurance_type':quotlists.insurance_type,
                    'registration_no':quotlists.registration_no,
                    'date_form':quotlists.date_form,
                    'date_to':quotlists.date_to,
                    'status':quotlists.status
                })
            return Response({'list':data})
    
    def create(self,request):
        quotcreate = Quotation()
        quotcreate.client_name = request.data.get('client_name')
        quotcreate.quote_no = request.data.get('quote_no')
        quotcreate.insurance_type = request.data.get('insurance_type')
        quotcreate.registration_no = request.data.get('registration_no')
        quotcreate.date_form = request.data.get('date_form')
        quotcreate.date_to = request.data.get('date_to')
        quotcreate.status = request.data.get('status')
        quotcreate.save()
        return Response({'Create Data'})
      
class Quotation2ViewSet(viewsets.ViewSet):
    def list(self,request):
        quolist = Quotations2.objects.all()        
        data=[]
        for loats in quolist:
            data.append({
                'branch':loats.branch,
                'quote':loats.quote,
                'client_name':loats.client_name,
                'insurance_type':loats.insurance_type,
                'cover_period':loats.cover_period,
                'insurance_name':loats.insurance_name,
                'amount':loats.amount,
                'status':loats.status
            })
        return Response({'list':data})
# class UpdateViewSet(viewsets.ViewSet):
#     def list(self,request):
#         forquo = Update.objects.all()
#         data=[]
#         for forqups in forquo:
#             data.append({
#                 'branch':forqups.quot2.branch,
#                 'quote':forqups.quot2.quote,
#                 'client_name':forqups.quot2.client_name,
#                 'insurance_type':forqups.quot2.insurance_type,
#                 'cover_period':forqups.quot2.cover_period,
#                 'insurance_name':forqups.quot2.insurance_name,
#                 'amount':forqups.quot2.amount,
#                 'status':forqups.quot2.status
#             })        
#         return Response({'list':data})  

class VehicleViewSet(viewsets.ViewSet):
    def list(self,request):
        quolist = Vehicle.objects.all()        
        data=[]
        for loats in quolist:
            data.append({
                'client_name':loats.client_name,
                'insurer':loats.insurer,
                'currency':loats.currency,
                'rate':loats.rate,
                'xrate':loats.xrate,
                'address':loats.address,
                'date_from':loats.date_from,
                'date_to':loats.date_to,
                'days':loats.days,
                'first_loss_payee':loats.first_loss_payee,
                'branch':loats.branch,
                'businee':loats.businee,
                'businee_type':loats.businee_type,
                'registration_no':loats.registration_no,
                'chassis_no':loats.chassis_no,
                'insured_name':loats.insured_name,
                'fuel_type':loats.fuel_type,
                'windscreen_sum_insured':loats.windscreen_sum_insured,
                'sum_insured':loats.sum_insured,
                'autual_premium':loats.autual_premium,
                'cover':loats.cover,
                'insurance':loats.insurance,
                'chassis':loats.chassis,
                'manufacture_Year':loats.manufacture_Year,
                'windscreen_premium':loats.windscreen_premium,
                'rate':loats.rate,
                'adjust':loats.adjust,
                'sticker':loats.sticker,
                'insurance_class':loats.insurance_class,
                'vehicle_make':loats.vehicle_make,
                'registration_year':loats.registration_year,
                'Accessories_sum_insured':loats.Accessories_sum_insured,
                'Override':loats.Override,
                'total_premium':loats.total_premium,
                'period_of_insurance':loats.period_of_insurance,
                'other_description':loats.other_description,
                'vehicle_model':loats.vehicle_model,
                'seat':loats.seat,
                'accessories_information':loats.accessories_information,
                'tppd_free_limit':loats.tppd_free_limit,
                'vehicle_type':loats.vehicle_type,
                'cc':loats.cc,
                'tppd_increase_limit':loats.tppd_increase_limit,
                'owner_category':loats.owner_category,
                'model_no':loats.model_no,
                'motar_category':loats.motar_category,
                'color':loats.color,
                'engine_no':loats.engine_no,
                'gross_weight':loats.gross_weight,
                'tare_weight':loats.tare_weight,
                'number_of_axel':loats.number_of_axel,
                'axel_distance':loats.axel_distance,
                'short_period':loats.short_period,
                'motar_category':loats.motar_category,
                'motar_usage':loats.motar_usage
            })
        return Response({'List':data})