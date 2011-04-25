
%define realname   Wx-Perl-Dialog
%define version    0.04
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Abstract dialog class for simple dialog creation
Source:     http://www.cpan.org/modules/by-module/Wx/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(File::Copy::Recursive)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Wx)
BuildRequires: perl(Wx::Event)
BuildRequires: perl(Wx::STC)


BuildArch: noarch

%description
Abstract dialog class for simple dialog creation


%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf %buildroot
%makeinstall_std


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


