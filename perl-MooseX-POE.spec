%define upstream_name    MooseX-POE
%define upstream_version 0.215

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	A Instance Metaclass for MooseX::POE
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-POE-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Async)
BuildRequires:	perl(POE)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Fatal)
Requires:	perl(MooseX::Async)
BuildArch:	noarch

%description
MooseX::POE is a Moose wrapper around a POE::Session.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu May 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.214.0-1mdv2011.0
+ Revision: 673816
- update to new version 0.214

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.211.0-2
+ Revision: 656944
- rebuild for updated spec-helper

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.211.0-1mdv2011.0
+ Revision: 612304
- update to new version 0.211

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2011.0
+ Revision: 596621
- update to 0.210

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.208.0-1mdv2011.0
+ Revision: 569940
- update to 0.208

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.207.0-1mdv2011.0
+ Revision: 562997
- update to 0.207

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.205.0-2mdv2011.0
+ Revision: 420167
- fix dependencies

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.205.0-1mdv2010.0
+ Revision: 393268
- update to 0.205 (for real this time)

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.205-1mdv2010.0
+ Revision: 389798
- update to new version 0.205

* Thu Jun 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.204.0-1mdv2010.0
+ Revision: 386973
- update to new version 0.204

* Tue Jun 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.203.0-1mdv2010.0
+ Revision: 382133
- adding missing buildrequires:
- adding missing buildrequires:
- import perl-MooseX-POE


* Mon Jun 01 2009 cpan2dist 0.203-1mdv
- initial mdv release, generated with cpan2dist


